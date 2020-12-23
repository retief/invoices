import uuid
import os

from django import forms
from django.http import JsonResponse

from indico import IndicoClient, IndicoConfig
from indico.queries import (
    RetrieveStorageObject,
    SubmissionResult,
    UpdateSubmission,
    WorkflowSubmission,
)

from api.invoices import parse_invoice
from api.models import Invoice

my_config = IndicoConfig(host="app.indico.io")
client = IndicoClient(config=my_config)
workflow_id = 933


class UploadFileForm(forms.Form):
    file = forms.FileField()


def upload(request):
    if request.method != "POST":
        return JsonResponse({"error": "Only POST here"}, status=400)

    form = UploadFileForm(request.POST, request.FILES)
    if not form.is_valid():
        return JsonResponse({"error": "invalid data"}, status=400)

    f = request.FILES["file"]
    if not os.path.exists("./tmp"):
        os.makedirs("./tmp")
    loc = "./tmp/%s.pdf" % str(uuid.uuid1())
    with open(loc, "wb+") as dest:
        for chunk in f.chunks():
            dest.write(chunk)

    submission_ids = client.call(
        WorkflowSubmission(workflow_id=workflow_id, files=[loc])
    )
    submission_id = submission_ids[0]

    result_url = client.call(SubmissionResult(submission_id, wait=True))
    parsed = parse_invoice(client.call(RetrieveStorageObject(result_url.result)))

    client.call(UpdateSubmission(submission_id, retrieved=True))
    db_result = Invoice.objects.create(
        vendor_name=parsed.get("Vendor Name", ""),
        vendor_street=parsed.get("Vendor Street", ""),
        vendor_city=parsed.get("Vendor City", ""),
        vendor_state=parsed.get("Vendor State", ""),
        vendor_zip=parsed.get("Vendor Zip", ""),
        invoice_number=parsed.get("Invoice #", ""),
        invoice_date=parsed.get("Invoice Date", ""),
        due_date=parsed.get("Due Date", ""),
        amount_due=parsed.get("Amount Due", ""),
    )
    return JsonResponse({"id": db_result.id})


def get_invoice(request, invoice_id):
    try:
        result = Invoice.objects.get(id=invoice_id)
    except Invoice.DoesNotExist:
        return JsonResponse({"error": "invalid id"}, status=404)
    return JsonResponse({"results": result.json()})


def search_invoices(request, search):
    return JsonResponse(
        {
            "results": [
                invoice.json()
                for invoice in Invoice.objects.filter(vendor_name__icontains=search)
            ]
        }
    )


def all_invoices(request):
    return JsonResponse(
        {
            "results": {
                invoice.id: invoice.vendor_name for invoice in Invoice.objects.all()
            }
        }
    )

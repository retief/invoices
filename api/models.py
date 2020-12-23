from django.db import models


class Invoice(models.Model):
    vendor_name = models.CharField(max_length=100, blank=True)
    vendor_street = models.CharField(max_length=100, blank=True)
    vendor_city = models.CharField(max_length=100, blank=True)
    vendor_state = models.CharField(max_length=100, blank=True)
    vendor_zip = models.CharField(max_length=100, blank=True)
    invoice_number = models.CharField(max_length=100, blank=True)
    invoice_date = models.CharField(max_length=100, blank=True)
    due_date = models.CharField(max_length=100, blank=True)
    amount_due = models.CharField(max_length=100, blank=True)

    def json(self):
        return {
            "Vendor Name": self.vendor_name,
            "Vendor Street": self.vendor_street,
            "Vendor City": self.vendor_city,
            "Vendor State": self.vendor_state,
            "Vendor Zip": self.vendor_zip,
            "Invoice #": self.invoice_number,
            "Invoice Date": self.invoice_date,
            "Due Date": self.due_date,
            "Amount Due": self.amount_due,
        }

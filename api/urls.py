from django.urls import path

from api import views

urlpatterns = [
    path("upload", views.upload, name="upload"),
    path("get/<int:invoice_id>", views.get_invoice, name="get_invoice"),
    path("search/<search>", views.search_invoices, name="search_invoices"),
    path("all", views.all_invoices, name="all_invoices"),
]

from decimal import Decimal

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.template.response import TemplateResponse
from payments import RedirectNeeded, get_payment_model


def index(request):
    return HttpResponse('<a href="/payment_create">Create payment</a>')


def payment_create(request):
    Payment = get_payment_model()
    payment = Payment.objects.create(
        variant="przelewy24",  # this is the variant from PAYMENT_VARIANTS
        description="Book purchase",
        total=Decimal(120.24),
        tax=Decimal(20),
        currency="PLN",
        delivery=Decimal(10),
        billing_first_name="Sherlock",
        billing_last_name="Holmes",
        billing_address_1="221B Baker Street",
        billing_address_2="",
        billing_city="London",
        billing_postcode="NW1 6XE",
        billing_country_code="GB",
        billing_country_area="Greater London",
        customer_ip_address="127.0.0.1",
    )
    return redirect(f"/payment_details/{payment.pk}")


def payment_details(request, payment_id):
    payment = get_object_or_404(get_payment_model(), id=payment_id)
    try:
        form = payment.get_form(data=request.POST or None)
    except RedirectNeeded as redirect_to:
        return redirect(str(redirect_to))
    return TemplateResponse(request, "payment.html", {"form": form, "payment": payment})

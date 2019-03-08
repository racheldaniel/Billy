from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.db import connection
from django.urls import reverse
from django.shortcuts import get_object_or_404, render
import requests
from website.models import *

# from website.forms import ProductForm
# from website.models import Product, ProductType, RecommendedProduct

def index(request):
    if request.method == "GET":
        url = 'https://api.propublica.org/congress/v1/115/both/bills/introduced.json'
        headers = {'X-API-Key': 'S6kqwpSxckFECU8hUHE3obzUfli28WzAOrNs1Qrh'}
        r = requests.get(url, headers=headers).json()
        bills = r["results"][0]["bills"]
        context={"bills": bills}
        template_name = 'index.html'
        return render(request, template_name, context)


def bill_details(request, bill_slug):
    """This function loads a specific bill's detail page.

    Parameters -- bill_slug: on proPublica api, bill_slug is the bill_id without the congress number
    """
    user = request.user
    if request.method == "GET":
            url = f'https://api.propublica.org/congress/v1/115/bills/{bill_slug}.json'
            headers = {'X-API-Key': 'S6kqwpSxckFECU8hUHE3obzUfli28WzAOrNs1Qrh'}
            r = requests.get(url, headers=headers).json()
            bill = r["results"][0]
            saved = ""
            saved_bills = UserBill.objects.filter(user_id=user)
            for saved_bill in saved_bills:
                if bill_slug == saved_bill.pp_bill_id:
                    saved = saved_bill
            context={"bill": bill, "user": user, "saved": saved}
            template_name = 'bill_details.html'
            return render(request, template_name, context)

def save_bill(request, bill_slug):
    user = request.user
    comment = request.POST["comment"]
    new_user_bill = UserBill(user=user, pp_bill_id=bill_slug, comment=comment)
    new_user_bill.save()
    return HttpResponseRedirect(reverse("website:bill_details", kwargs={"bill_slug": bill_slug}))

def edit_saved_bill(request, bill_slug):
    user = request.user
    saved_bill = UserBill.objects.filter(user_id=user, pp_bill_id=bill_slug)[0]
    saved_bill.comment = request.POST["editComment"]
    saved_bill.save()
    return HttpResponseRedirect(reverse("website:bill_details", kwargs={"bill_slug": bill_slug}))

def delete_bill(request, bill_slug):
    user = request.user
    saved_bill = UserBill.objects.filter(user_id=user, pp_bill_id=bill_slug)[0]
    saved_bill.delete()
    return HttpResponseRedirect(reverse("website:bill_details", kwargs={"bill_slug": bill_slug}))




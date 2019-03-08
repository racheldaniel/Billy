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
    if request.method == "GET":
            url = f'https://api.propublica.org/congress/v1/115/bills/{bill_slug}.json'
            headers = {'X-API-Key': 'S6kqwpSxckFECU8hUHE3obzUfli28WzAOrNs1Qrh'}
            r = requests.get(url, headers=headers).json()
            bill = r["results"][0]
            context={"bill": bill}
            template_name = 'bill_details.html'
            return render(request, template_name, context)

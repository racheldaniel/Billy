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
        url = 'https://api.propublica.org/congress/v1/115/both/bills/active.json'
        headers = {'X-API-Key': 'S6kqwpSxckFECU8hUHE3obzUfli28WzAOrNs1Qrh'}
        r = requests.get(url, headers=headers).json()
        context={}
        template_name = 'index.html'
        return render(request, template_name, context)


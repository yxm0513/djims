# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.views import login, logout
from django.contrib.auth.decorators import login_required
from models import Product

def home(request):
    if request.user.is_authenticated():
        return render_to_response("home.html")
    else:
        return redirect('login')

@login_required(login_url="/login")
def template(request):
    products = Product.objects.all()
    simon = "test"
    return render_to_response("template.html", \
        {'name' : simon, 'products' :products})

def test(request):
    return HttpResponse(_("Test"));


def add_product():
    pass
    # need check if category is empty

    # genetate product information, and add it.

    # redirect to index

def del_product():
    pass

    # check if product is there get_object_or_404

def add_category():
    pass

def remove_category():
    pass

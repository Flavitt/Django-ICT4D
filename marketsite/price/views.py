from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.template import loader
from django.views import generic
from django.utils import timezone


from .models import Choice, Crop

def index(request):
    latest_crop_list = Crop.objects.order_by('-pub_date')
    template = loader.get_template('price/index.html')
    context = {
        'latest_crop_list': latest_crop_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, price):
    return HttpResponse("The price of this crop is %f." % price)

def results(request, price):
    response = "You're looking at the results of crop %s."
    return HttpResponse(response % crop_id)

def giveprice(request, price):
    return HttpResponse("You're voting on crop %s." % crop_id)
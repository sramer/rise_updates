from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from .models import Prakasam, Gandhi, Polytechnic

def index(request):
    context = {
        "prakasams": Prakasam.objects.all().order_by('-id'),
        "gandhis": Gandhi.objects.all().order_by('-id'),
        "polytechnics": Polytechnic.objects.all().order_by('-id')
    }
    return render(request, "updates/index.html", context)

def prakasam(request, prakasam_id):
    try:
        prakasam = Prakasam.objects.get(pk=prakasam_id)
    except Prakasam.DoesNotExist:
        raise Http404("No updates here.")
    context = {
        "prakasam":prakasam,
    }
    return render(request, "updates/prakasam.html", context)



def gandhi(request, gandhi_id):
    try:
        gandhi = Gandhi.objects.get(pk=gandhi_id)
    except Gandhi.DoesNotExist:
        raise Http404("No updates here.")
    context = {
        "gandhi":gandhi,
    }
    return render(request, "updates/gandhi.html", context)
    return HttpResponseRedirect(reverse("prakasam", args=(prakasam_id,)))

def polytechnic(request, polytechnic_id):
    try:
        polytechnic = Polytechnic.objects.get(pk=polytechnic_id)
    except Polytechnic.DoesNotExist:
        raise Http404("No updates here.")
    context = {
        "polytechnic":polytechnic,
    }
    return render(request, "updates/polytechnic.html", context)

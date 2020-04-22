from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Pastors,Leadership,Ushering,Transport,Worshipper, Media
from .models import Deacon


def home(request):
    pastors = Pastors.objects.all()
    leaderships = Leadership.objects.all()
    return render(request,'home_page.html', {'pastors':pastors, 'leaderships':leaderships})


# ushering department function
def ushering(request):
    ushers = Ushering.objects.all()
    return render(request, 'ushering.html', {'ushers':ushers})


# transport department function
def transport(request):
    transports = Transport.objects.all()
    return render (request, 'transport.html', {'transports':transports})


# function for media department
def media(request):
    medias = Media.objects.all()
    return render (request, 'media.html', {'medias': medias})


# function for living voice department
def living_voice(request):
    worshippers = Worshipper.objects.all()
    return render (request, 'living_voice.html', {'worshippers': worshippers})


# function for extreme grace foundation
def extreme_grace(request):
    return render (request, 'extreme_grace.html', {})


# function for deacons and Deaconess
def deacon(request):
    deacons = Deacon.objects.all()
    return render (request, 'deacon.html', {'deacons': deacons})

# function for boa base School
def boa_base(request):
    return render(request, 'boa_base.html', {})
# functions for board of trustees
def board_of_trustee(request):
    return render (request, 'board_of_trustee.html', {})


def pastors(request):
    pastors = Pastors.objects.all()
    return render(request,'pastors.html', {'pastors':pastors})

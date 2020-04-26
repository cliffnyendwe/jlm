from django.shortcuts import render,redirect
from django.core.mail import EmailMessage
# Create your views here.
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from .models import Pastors,Leadership,Ushering,Transport,Worshipper, Media
from .models import Deacon,Trustee,Extreme,Event,Testimony
from .forms import ContactForm

def home(request):
    pastors = Pastors.objects.all()
    leaderships = Leadership.objects.all()
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request,'home_page.html', {'pastors':pastors, 'leaderships':leaderships, 'form': form})

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
    extremes = Extreme.objects.all()
    return render (request, 'extreme_grace.html', {'extremes':extremes})

# function for deacons and Deaconess
def deacon(request):
    deacons = Deacon.objects.all()
    return render (request, 'deacon.html', {'deacons': deacons})

# function for boa base School
def boa_base(request):
    return render(request, 'boa_base.html', {})

# functions for board of trustees
def board_of_trustee(request):
    trustees = Trustee.objects.all()
    return render (request, 'board_of_trustee.html', {'trustees':trustees})

# functions for pastors department
def pastors(request):
    pastors = Pastors.objects.all()
    return render(request,'pastors.html', {'pastors':pastors})

# functions for pastors department
def event(request):
    events = Event.objects.all()
    return render(request,'event.html', {'events':events})

def success(request):
    return HttpResponse('Success! Thank you for your message.')

# function for testimonies
def testimonies(request):
    testimonies = Testimony.objects.all()
    return render(request, 'testimonies.html', {'testimonies':testimonies})

# function for contact section
def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request,'contact.html', {'form': form})

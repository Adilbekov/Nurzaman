from django.shortcuts import render
from apps.base import models
from apps.secondary.models import Slide, Partners,Info, ImageGallery, One, SlideTwo, Environment, Street
from apps.contacts.models import Cotact, Contact_2
# Create your views here.

def index(request):
    settings=models.Setting.objects.latest('id')
    menu=models.Menu.objects.latest('id')
    logo=models.Logo.objects.latest('id')
    slide=Slide.objects.latest('id')
    partner=Partners.objects.all()
    about=models.About.objects.latest('id')
    blog=models.Blog.objects.latest('id')
    info=Info.objects.all()
    infoplus=models.InfoPlus.objects.latest('id')
    gellary=ImageGallery.objects.latest('id')
    one=One.objects.latest('id')
    two=SlideTwo.objects.all()
    enviroment=Environment.objects.all()
    street=Street.objects.latest('id')
    choise=models.Choice.objects.latest('id')
    if request.method == "POST":
        if 'call' in request.POST:
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            contact = Cotact.objects.create(name=name, email=email, phone=phone)

        if "base" in request.POST:
            name = request.POST.get("name")
            phone = request.POST.get("phone")
            contacts=Contact_2.objects.create(name=name, phone=phone)

    return render(request, 'index.html', locals())




def catalog(request):
    return render(request, 'catalog.html', locals())

def Gen_planing(requrements):
    return render(requrements, 'genPlaning.html', locals())
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.forms import *
from app.models import *

def insert_topic(request):
    LTO=topic()
    d={'LTO':LTO}
    if request.method=='POST':
        LOT=topic(request.POST)
        if LOT.is_valid():
            topic_name=LOT.cleaned_data['topic_name']
            TO=Topic.objects.get_or_create(topic_name=topic_name)[0]
            TO.save()
            TOL=Topic.objects.all()
            d1={'TOL':TOL}
            return render(request,'display.html',d1)
    return render(request,'topics.html',d)

def insert_webpage(request):
    LOW=webpage()
    d={'LOW':LOW}
    if request.method=='POST':
        LWO=webpage(request.POST)
        if LWO.is_valid():
            topic_name=LWO.cleaned_data['topic_name']
            name=LWO.cleaned_data['name']
            email=LWO.cleaned_data['email']
            url=LWO.cleaned_data['url']
            TO=Topic.objects.get_or_create(topic_name=topic_name)[0]
            TO.save()
            WO=Webpage.objects.get_or_create(topic_name=TO,name=name,email=email,url=url)[0]
            WO.save()
            LW=Webpage.objects.all()
            d1={'LW':LW}
            return render(request,'display_web.html',d1)
    return render(request,'webpage.html',d)

def insert_access(request):
    LOA=access()
    d={'LOA':LOA}
    if request.method=='POST':
        LAO=access(request.POST)
        if LAO.is_valid():
            name=LAO.cleaned_data['name']
            author=LAO.cleaned_data['author']
            date=LAO.cleaned_data['date']
            WO=Webpage.objects.get(name=name)
            WO.save()
            AO=AccessRecord.objects.get_or_create(name=WO,author=author,date=date)[0]
            AO.save()
            LA=AccessRecord.objects.all()
            d2={'LA':LA}
        return render(request,'display_access.html',d2)
    return render(request,'access.html',d)
from django.shortcuts import render, get_object_or_404
import requests
from .models import Sity
from .forms import SityForm

def index(request):
    apiid = '90f0ffc01314a28c380c79c96f0ff725'
    apiid1 = '0fedf62a4b48093d0fe6e0b95fe05ae2'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&&appid=' +apiid1
    sityes = Sity.objects.all()  
    sity_all = []
    name_sity_all = []
    for sity in sityes:
        res = requests.get(url.format(sity)).json()         
        sity_info = {
            'sity': sity,
            'temp': res['main']['temp'],
            'icon': res['weather'][0]['icon']    
            }
            
        sity_all.append(sity_info)
        name_sity_all.append(sity.name.lower())
        
    if request.method == 'POST':
        form = SityForm(request.POST)       
        if form.is_valid():
            name_sity = form.cleaned_data.get("name").lower()
            
            if not name_sity in name_sity_all:
                Sity.objects.create(**form.cleaned_data)    
    form = SityForm()        
    context = {'sity_all': sity_all, 'form': form, 'sityes': sityes, 'title':'Главная страница'}
    return render(request, 'wether_map/index.html', context)

def about_sity(request, sity):
    sityes = get_object_or_404(Sity, name=sity)
    apiid = '90f0ffc01314a28c380c79c96f0ff725'
    apiid1 = '0fedf62a4b48093d0fe6e0b95fe05ae2'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&&appid=' +apiid1
     
    
    res = requests.get(url.format(sityes.name)).json()         
    sity_info = {
        'sity': sityes.name,
        'temp': res['main']['temp'],
        'icon': res['weather'][0]['icon'],
        'wind': res['wind']['speed']
        
            }
    print(res)
    print(sity_info)
          
    
    return render(request, "wether_map/about_sity.html", {'sity_info':sity_info, 'title': sityes.name})

from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.
def home(request):
    city = request.GET.get('city','Pune')
    url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=69a616e50906b240ffb8e62ff169c663'
    data=requests.get(url).json()
    #print(data)
    alldata={
        'city'      :  data['name'],
        'weather'   :  data['weather'][0]['main'],
        'icon'      :  data['weather'][0]['icon'],
        'k_temprature':  data['main']['temp'],
        'c_temprature':  int(data['main']['temp']-273),

        'pressure'  :  data['main']['pressure'],
        'humidity'  :  data['main']['humidity'],
        'description':data['weather'][0]['description']
    }
    done = {'data':alldata}
    
    return render (request,'index.html',done)
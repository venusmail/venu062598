import requests
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import TrackedClick
from .models import Unsub
from django.shortcuts import render

def get_country_city_from_ip(ip):
    url = f"https://ipinfo.io/{ip}/json"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes
        data = response.json()
        country = data.get('country', '')
        city = data.get('city', '')
        print(city)
    except Exception as e:
        # Handle API request errors
        country = ''
        city = ''
    
    return country, city
def unsub(request, offer_id, user_id, list_id, aff_net, drop, ip_address=None):
    # Get user's IP address
    

    # Use a service or library to get country and city based on IP
    country, city = get_country_city_from_ip(ip_address)

    # Save the tracked click information
    Unsub.objects.create(
        
        offer_id=offer_id,
        user_id=user_id,
        ip_address=ip_address,
        country=country,
        city=city,
        list_id=list_id,
        aff_net=aff_net,
        drop=drop,
    )

    # Redirect the user to the original destination
    # You might want to use a template or another method to create the destination URL.
    if offer_id == 'You might want to use a template or another method to create the destination URL.':
        pass
    elif offer_id == '256' and aff_net == 'YnViYQ==':
        return redirect('https://www.youtube.com')
    
   
    
    else:
        return redirect('https://www.example.com')

# email_tracking_app/views.py
import requests
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import TrackedClick
from .models import Unsub
from django.shortcuts import render


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .serializers import TrackedClickSerializer
from .serializers import UnsubSerializer

@csrf_exempt  # For simplicity, but you should use proper CSRF protection in production
def tracked_clicks_api(request):
    if request.method == 'GET':
        tracked_clicks = TrackedClick.objects.all()
        serializer = TrackedClickSerializer(tracked_clicks, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt  # For simplicity, but you should use proper CSRF protection in production
def unsubs_api(request):
    if request.method == 'GET':
        unsubs = Unsub.objects.all()
        serializer = UnsubSerializer(unsubs, many=True)
        return JsonResponse(serializer.data, safe=False)
        
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

def track_click(request, offer_id, user_id, list_id, aff_net, drop, ip_address=None):
    # Get user's IP address
    

    # Use a service or library to get country and city based on IP
    country, city = get_country_city_from_ip(ip_address)

    # Save the tracked click information
    TrackedClick.objects.create(
        
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
    elif offer_id == '1536':
        return redirect('jkjbjkbkjb')
    elif offer_id == '1536':
        return redirect('jkjbjkbkjb')
    else:
        return redirect('https://www.example.com') 
    
    

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
    if offer_id == '1536':
        return redirect('https://www.google.com')
    else:
        return redirect('https://www.example.com')
    

def reunsub(request, offer_id, user_id, list_id, aff_net, drop):
    return render(request, 'reunsub.html', {'offer_id': offer_id, 'user_id': user_id, 'list_id': list_id, aff_net:'aff_net', drop:'drop' })

def re(request, offer_id, user_id, list_id, aff_net, drop):
    return render(request, 're.html', {'offer_id': offer_id, 'user_id': user_id, 'list_id': list_id, aff_net:'aff_net', drop:'drop' })


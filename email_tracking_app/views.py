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
    elif offer_id == '256' and aff_net == 'YnViYQ==':
        return redirect('https://www.youtube.com')
    
    else:
        return redirect('https://www.example.com')


from .abc import unsub

def reunsub(request, offer_id, user_id, list_id, aff_net, drop):
    return render(request, 'reunsub.html', {'offer_id': offer_id, 'user_id': user_id, 'list_id': list_id, aff_net:'aff_net', drop:'drop' })

def re(request, offer_id, user_id, list_id, aff_net, drop):
    return render(request, 're.html', {'offer_id': offer_id, 'user_id': user_id, 'list_id': list_id, aff_net:'aff_net', drop:'drop' })



@csrf_exempt  # Reminder: use proper CSRF protection in production
def tracked_clicks_range_api(request):
    if request.method == 'GET':
        # Retrieve start and end id from request query parameters
        start_id = request.GET.get('start_id', None)
        end_id = request.GET.get('end_id', None)
        
        # Validate presence of start_id and end_id
        if start_id is not None and end_id is not None:
            # Convert start_id and end_id to integers (consider adding try-except for error handling)
            start_id = int(start_id)
            end_id = int(end_id)
            
            # Filter tracked clicks within the specified range
            tracked_clicks = TrackedClick.objects.filter(click_id__range=(start_id, end_id))
            serializer = TrackedClickSerializer(tracked_clicks, many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            # If start_id or end_id are not provided, return an error response
            return JsonResponse({'error': 'Missing start_id or end_id query parameter'}, status=400)


@csrf_exempt  # Reminder: use proper CSRF protection in production
def tracked_nsub_range_api(request):
    if request.method == 'GET':
        # Retrieve start and end id from request query parameters
        start_id = request.GET.get('start_id', None)
        end_id = request.GET.get('end_id', None)
        
        # Validate presence of start_id and end_id
        if start_id is not None and end_id is not None:
            # Convert start_id and end_id to integers (consider adding try-except for error handling)
            start_id = int(start_id)
            end_id = int(end_id)
            
            # Filter tracked clicks within the specified range
            tracked_clicks = Unsub.objects.filter(click_id__range=(start_id, end_id))
            serializer = UnsubSerializer(tracked_clicks, many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            # If start_id or end_id are not provided, return an error response
            return JsonResponse({'error': 'Missing start_id or end_id query parameter'}, status=400)

# email_tracking_app/urls.py
from django.urls import path
from .views import track_click
from .views import re
from .views import reunsub
from .views import unsub
from .views import tracked_clicks_api
from .views import unsubs_api
from .abc import unsub
from .views import tracked_clicks_range_api
from .views import tracked_nsub_range_api



urlpatterns = [
    path('tr/<str:offer_id>/<str:user_id>/<str:list_id>/<str:aff_net>/<str:drop>/<str:ip_address>', track_click, name='tr'),
    path('re/<str:offer_id>/<str:user_id>/<str:list_id>/<str:aff_net>/<str:drop>', re, name='re'),

    path('trunsub/<str:offer_id>/<str:user_id>/<str:list_id>/<str:aff_net>/<str:drop>/<str:ip_address>', unsub, name='usub'),
    path('reunsub/<str:offer_id>/<str:user_id>/<str:list_id>/<str:aff_net>/<str:drop>', reunsub, name='reunsub'),

    path('tracked-clicks/xxx', tracked_clicks_api, name='tracked_clicks_api'),
    path('unsubs/xxxx', unsubs_api, name='unsubs_api'),
    path('api/tracked_clicks/', tracked_clicks_range_api, name='tracked_clicks_range_api'),
    path('api/tracked_unsub/', tracked_nsub_range_api, name='tracked_clicks_range_api'),




    
    # Add other URL patterns as needed
]

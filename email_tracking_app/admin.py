# email_tracking_app/admin.py
from django.contrib import admin
from .models import TrackedClick
from .models import Unsub

@admin.register(TrackedClick)
class TrackedClickAdmin(admin.ModelAdmin):
    list_display = ('click_id', 'offer_id', 'user_id', 'ip_address', 'country', 'city', 'list_id', 'aff_net', 'drop', 'timestamp')
    search_fields = ('click_id', 'user_id', 'ip_address', 'country', 'city')
    list_filter = ('timestamp',)

@admin.register(Unsub)
class unsubAdmin(admin.ModelAdmin):
    list_display = ('click_id', 'offer_id', 'user_id', 'ip_address', 'country', 'city', 'list_id', 'aff_net', 'drop', 'timestamp')
    search_fields = ('click_id', 'user_id', 'ip_address', 'country', 'city')
    list_filter = ('timestamp',)

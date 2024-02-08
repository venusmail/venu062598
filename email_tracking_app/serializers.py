from rest_framework import serializers
from .models import TrackedClick
from .models import Unsub

class TrackedClickSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackedClick
        fields = '__all__'



class UnsubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unsub
        fields = '__all__'

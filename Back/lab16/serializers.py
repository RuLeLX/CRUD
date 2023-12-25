from .models import *
from rest_framework import serializers
import datetime

class UserSerializer(serializers.ModelSerializer):
    time_create_token = serializers.SerializerMethodField()
    
    class Meta:
        model = Users
        fields = ['email', 'level_acces', 'time_create_token']

    def get_time_create_token(self, obj):
        date = []
        current_date = datetime.datetime.now()
        date.extend([
            current_date.year, current_date.month, current_date.day,
            current_date.hour, current_date.minute
        ])
        return date
    

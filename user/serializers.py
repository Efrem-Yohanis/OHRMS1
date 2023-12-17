from rest_framework import serializers
from .models import *

class unapprovedS(serializers.ModelSerializer):
    class Meta:
        model = unapproved
        fields = '__all__' 
from django.shortcuts import render
from rest_framework import serializers
from .models import SupportTicket
from rest_framework import viewsets
from .models import SupportTicket

# Serializers

class SupportTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupportTicket
        fields = '__all__'


# Viewsets

class SupportTicketViewSet(viewsets.ModelViewSet):
    queryset = SupportTicket.objects.all()
    serializer_class = SupportTicketSerializer
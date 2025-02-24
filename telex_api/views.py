from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import TelexIntegration
from .serializers import TelexIntegrationSerializer

class IntegrationJSONView(APIView):
    def get(self, request):
        integration = TelexIntegration.objects.first()
        serializer = TelexIntegrationSerializer(integration)
        return Response(serializer.data)
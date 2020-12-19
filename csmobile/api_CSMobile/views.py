from rest_framework import viewsets

from CSMobile_site.models import Message
from .serializers import MessageSerializer


# Create your views here.

class AddDataSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()

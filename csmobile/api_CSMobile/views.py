from rest_framework import viewsets, status
from rest_framework.response import Response
import requests

from CSMobile_site.models import Message
from .serializers import MessageSerializer


# Create your views here.

class AddDataSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        res = requests.post('http://127.0.0.1:8000/auth/jwt/verify/', data={"token": serializer.initial_data['token']})
        if not res.ok:
            print('Жопа')
            exit()
        else:
            print('Получилось')
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

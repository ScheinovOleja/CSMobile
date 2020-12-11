from django.urls import path, include
from . import views as view

urlpatterns = [
    path('add_data/', view.AddData.as_view(), name='api_data')
]
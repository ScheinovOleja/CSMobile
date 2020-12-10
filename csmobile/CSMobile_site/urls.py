from django.urls import path, include
from django.contrib.auth import views as views
from . import views as view

urlpatterns = [
    path('', view.Index.as_view(), name='first_page'),
]
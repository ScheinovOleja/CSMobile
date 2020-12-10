from django.shortcuts import render
from django.views import View, generic

# Create your views here.


class Index(generic.View):

    def __init__(self):
        super().__init__()
        self.template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name, {})

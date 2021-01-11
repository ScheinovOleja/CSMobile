from django.shortcuts import render
from django.views import generic

# Create your views here.


class Index(generic.View):

    def __init__(self):
        super().__init__()
        self.template_name = 'index.html'

    def get(self, request):
        if request.user.is_authenticated:
            print(f'Это авторизованный пользователь {request.user}')
        else:
            print('Это неавторизованный пользователь')

        return render(request, self.template_name, {})

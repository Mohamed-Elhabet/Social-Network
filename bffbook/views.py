from django.http import HttpResponse
from django.shortcuts import render 
from profiles.models import Profile 

def home_view(request):
  # return HttpResponse('hello world')
  user = request.user 
  hello = 'Hello world'

  context = {
    'user': user,
    'hello': hello,
  }

  return render(request, 'main/home.html', context)
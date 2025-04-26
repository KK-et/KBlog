from django.shortcuts import render, redirect
from django.template import loader
from .models import post
from django.http import HttpResponse

def index(request):
    posts = post.objects.all()  
    return render(request, 'home.html', {'posts': posts})  
    
def details(request, id):
  det = post.objects.get(id=id)
  template = loader.get_template('det.html')
  context = {
    'det': det,
  }
  return HttpResponse(template.render(context, request))


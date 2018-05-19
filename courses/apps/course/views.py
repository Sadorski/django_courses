from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
  # the index function is called when root is visited
from models import *
def index(request):
    context = {
      "courses": Course.objects.all()
    }
    return render(request, 'course/index.html', context )

def remove(request, id):
    Course.objects.get(id=id).delete()
    return redirect('/')

def add(request):
    if request.method == 'POST':
        errors = Course.objects.basic_validator(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
                return redirect('/')
        else:
            Course.objects.create(name = request.POST['name'], desc = request.POST['desc'])
            return redirect ('/')
    
def confirm(request, id):
    context = {
      'course': Course.objects.get(id=id)
    }
    return render(request, 'course/confirm.html', context)



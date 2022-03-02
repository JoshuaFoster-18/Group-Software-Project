from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import task

import json 

def index(request):
    return render(request, 'locationgameapp/index.html')

def signUp(request):
    return render(request, 'locationgameapp/signUp.html')

def Game(request):
    taskList = list(task.objects.order_by('taskName').values()) 
    taskJson = json.dumps(taskList)  
    context = {'tasks': taskJson} 
    return render(request, 'locationgameapp/game.html', context) 

@login_required
<<<<<<< HEAD
=======
def Settings(request):
    return render(request, 'locationgameapp/settings.html')

@login_required
>>>>>>> parent of fcb8a67 (Start of linting + Commenting)
def Leaderboards(request):
    return render(request, 'locationgameapp/Leaderboards.html')


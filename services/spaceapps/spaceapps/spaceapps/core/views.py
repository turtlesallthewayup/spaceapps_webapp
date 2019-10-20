
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import numpy as np
import io

from spaceapps.core.utils import base64_to_file

# Create your views here.
    
def index(request):
    context = {}
    return render(request, 'index.html', context)
    
def traning_step1(request):
    context = {}
    return render(request, 'traning_step1.html', context)
    
def traning_step2(request):
    context = {}
    return render(request, 'traning_step2.html', context)
    
def traning_step3(request):
    context = {}
    return render(request, 'traning_step3.html', context)
    
def traning_step4(request):
    context = {}
    return render(request, 'traning_step4.html', context)

def traning_step5(request):
    context = {}
    return render(request, 'traning_step5.html', context)
    
def traning_step6(request):
    context = {}
    return render(request, 'traning_step6.html', context)

def traning_step7(request):
    context = {}
    return render(request, 'traning_step7.html', context)
    
    
def traning_step8(request):
    context = {}
    return render(request, 'traning_step8.html', context)
    
def traning_step9(request):
    context = {}
    return render(request, 'traning_step9.html', context)
    
def traning_step10(request):
    context = {}
    return render(request, 'traning_step10.html', context)
    
def control(request):
    context = {}
    return render(request, 'control.html', context)
    
    
    
#=======================
@csrf_exempt
def receive_blob(request):
    data = request.POST.getlist("images[]")
    
    
    images_file = []
    for d in data:
        x=base64_to_file(d)
        images_file.append(np.asarray(x))
    
    print(images_file)
        
    return JsonResponse({"status":200})
    
def train(request):
    pass


def predict(request):
    pass
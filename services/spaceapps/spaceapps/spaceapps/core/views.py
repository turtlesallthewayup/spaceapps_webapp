from django.http import StreamingHttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

import io
import os

from spaceapps.core.utils import base64_to_file
from spaceapps.core.utils_ai_train import ai_train


DATA = []
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
    train()
    return render(request, 'control.html', context)
    
    
    
#=======================
@csrf_exempt
def receive_blob(request):
    data = request.POST.getlist("images[]")
    label = request.POST.get("label")
    images_file = []
    for i, d in enumerate(data):
        pillow_img=base64_to_file(d)
        
        file_name = 'img_{}.jpeg'.format(i)
        
        #pillow_img.save('datasets/{}/img_{}.jpeg'.format(label, i), 'JPEG')
        pillow_img.save(os.path.join(settings.BASE_DIR, 'spaceapps', 'core', 'datasets/'+label+'/' + file_name), "JPEG")

        images_file.append(pillow_img)
    
    DATA.append((label, images_file))
    print(DATA)    
    return JsonResponse({"status":200})
    
@csrf_exempt
def train():
    ai_train(DATA)
    

@csrf_exempt
def predict(request):
    #salvar imagem e mandar path
    path = ""
    ai_predict(path)

@csrf_exempt
def start_stream(request):
    drone_camera = 'video object'
    return StreamingHttpResponse(drone_camera)
    

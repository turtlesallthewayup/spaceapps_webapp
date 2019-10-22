from django.http import StreamingHttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

import io
import os
import time

from spaceapps.core.utils import base64_to_file
from spaceapps.core.utils_ai_train import ai_train
from spaceapps.core.utils_ai_preditc import ai_predict
from spaceapps.core import utils_drone_keyboard


keyboard = utils_drone_keyboard.DroneKeyboard()
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
        
        pillow_img.save(os.path.join(settings.BASE_DIR, 'spaceapps', 'core', 'datasets', label, file_name), "JPEG")

        images_file.append(pillow_img)
    
    DATA.append((label, images_file)) 
    print(DATA)    
    return JsonResponse({"status":200})
    
@csrf_exempt
def train():
    ai_train(DATA)
    

@csrf_exempt
def predict(request):
    
    time.sleep(2)
    data = request.POST.get("image")
    pillow_img=base64_to_file(data)

    path = os.path.join(settings.BASE_DIR, 'spaceapps', 'core', 'to_predict', 'img_to_predict.jpeg')

    pillow_img.save(path, "JPEG")
    
    command = ai_predict(path) 
    
    print(command)    
    
    if command == 0:
        pass
    elif command == 1:
        print('PREDICT DRONE START')
        keyboard._drone_start()
    elif command == 2:
        print('PREDICT ROTATE LEFT')
        keyboard._drone_rotate_left()
    elif command == 3:
        print('PREDICT ROTATE RIGHT')
        keyboard._drone_rotate_right()
    elif command == 4:
        print('PREDICT DRONE STOP')
        #print('PREDICT MOVE LEFT')
        keyboard._drone_move_left()
        
        
        
    elif command == 5:
        print('PREDICT MOVE LEFT')
        keyboard._drone_move_right()
    elif command == 6:
        print('PREDICT MOVE FRONT')
        keyboard._drone_move_front()
    elif command == 7:
        print('PREDICT MOVE BACK')
        keyboard._drone_move_back()
    elif command == 8:
        print('PREDICT ACCELERATE')
        keyboard._drone_accelerate()
    elif command == 9:
        print('PREDICT DECELERATE')
        keyboard._drone_decelerate()
    elif command == 10:
        print('PREDICT MOVE LEFT')
        #print('PREDICT DRONE STOP')
        keyboard._drone_stop()
    
    #count = 0
    #while True:
        #if keyboard.connected:
            #print('CONNECTED - SEND COMMAND')
            #keyboard._apply_clamp()
            #keyboard._send_cmd()
            #time.sleep(0.5)
            #count += 1
            #if count == 20:
                #break
    
    
    if keyboard.connected:
        print('CONNECTED - SEND COMMAND')
        keyboard._apply_clamp()
        keyboard._send_cmd()
        time.sleep(0.5)
    
    
    
    return JsonResponse({'command': command})

@csrf_exempt
def start_stream(request):
    drone_camera = 'video object'
    return StreamingHttpResponse(drone_camera)
    

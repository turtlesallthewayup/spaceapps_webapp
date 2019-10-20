from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

app_name = 'core'

urlpatterns = [
    path('', index, name='index'),
    path('traning_step1', traning_step1, name='traning_step1'),
    path('traning_step2', traning_step2, name='traning_step2'),
    path('traning_step3', traning_step3, name='traning_step3'),
    path('traning_step4', traning_step4, name='traning_step4'),
    path('traning_step5', traning_step5, name='traning_step5'),
    path('traning_step6', traning_step6, name='traning_step6'),
    path('traning_step7', traning_step7, name='traning_step7'),
    path('traning_step8', traning_step8, name='traning_step8'),
    path('traning_step9', traning_step9, name='traning_step9'),
    path('traning_step10', traning_step10, name='traning_step10'),
    path('control', control, name='control'),
    
    
    #===============================================================
    #Keras methods
    path('receive_blob', receive_blob, name='receive_blob'),
    path('predict', predict, name='predict'),
]
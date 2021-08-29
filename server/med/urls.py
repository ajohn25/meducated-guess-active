from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('intro', views.intro, name = 'intro'),
    path('convo', views.convo, name = 'convo'),
    path('predict', views.predict, name = 'predict'),
    path('question', views.question, name = 'question'),

]
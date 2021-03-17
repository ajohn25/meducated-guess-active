from django.shortcuts import render
from django.http import HttpResponse
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from med.models import Symptoms

# Create your views here.
def index(request):
    return HttpResponse("Hello, world")

def intro(request):
    return JsonResponse({'message': "Hi my name is Dr. Guess! How are you feeling today?"})

@csrf_exempt 
def convo(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        message = body["message"]

        if message.startswith("Thank you") or message.startswith("Bye") or message.startswith("Thanks"):
             return JsonResponse({'message': "You’re welcome, do you have any additional concerns?"})

        elif message.startswith("That's all"):
             return JsonResponse({'message': "Goodbye! Take care and hope you feel well soon!"})
        
        elif message == "I have a cold":
             return JsonResponse({'message': "Common Cold"})

        elif message.startswith("I feel") or message.startswith("I'm not") :
             return JsonResponse({'message': "What symptoms are you expressing?"})
             
        elif message.startswith("I'm coughing"):
            return JsonResponse({'message': "Do you have any of these symptoms: congestion, a fever, runny nose?"})
    
        elif message.startswith("I have all"):
            return JsonResponse({'message': "Have you eaten anything unusual lately?"})
    
        elif message.startswith("My stomach"):
            return JsonResponse({'message': "Have you eaten anything unusual lately?"})

        elif message.startswith("I think I did have"): 
            return JsonResponse({'message': "That makes sense! My prediction is that you have food poisoning"})

        elif message.endswith("normal diet"): 
            return JsonResponse({'message': "Got it! My prediction is that you have the common cold"})



        else:
            return JsonResponse({'message': "Sorry I didn't catch that. Could you phrase that differently?"})

@csrf_exempt 
def predict(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        symptoms = body["symptoms"]
        symptom1 = symptoms[0]

        disease = Symptoms.objects.filter(symptom_1__icontains = symptom1)[:1][0].disease
        return JsonResponse({'disease': disease})

        
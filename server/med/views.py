from django.shortcuts import render
from django.http import HttpResponse
import json
import asyncio
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from med.models import Symptoms, Questions
from med.serializers import QuestionsSerializer
from rasa.core.agent import Agent
from rest_framework.renderers import JSONRenderer




# Create your views here.

async def parseAgent(msg):
    return await myAgent.parse_message_using_nlu_interpreter(msg)

myAgent = Agent()
myAgent = myAgent.load('rasa/models/nlu4.tar.gz')

def index(request):
    return HttpResponse("Hello, world")

def intro(request):
    return JsonResponse({'message': "Hi my name is Dr. Guess! How are you feeling today?"})

@csrf_exempt 
def convo(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        message = body["message"]
        question = body["question"]
        textSymptoms = body["textSymptoms"]

        result = asyncio.run(parseAgent(message))
        intent = result['intent']['name']

        try:
            if intent == 'symptom' or intent == 'affirm':
                for entity in result['entities']: textSymptoms[entity['value']] = True
                answer = 'Yes'

            elif intent == 'no-symptom' or intent == 'deny':
                if len(result['entities']) > 0:
                    textSymptoms[result['entities'][0]['value']] = 'No'
                    
                    if len(result['entities']) > 1:
                        if 'but' in message: textSymptoms[result['entities'][1]['value']] = 'Yes'
                        else: textSymptoms[result['entities'][1]['value']] = 'No'

                answer = 'No'

            else: return JsonResponse({'message': "Sorry I didn't catch that"})
        except: return JsonResponse({'message': "Sorry I didn't catch that"})

        ds = Questions.objects.filter(prevQuestion = question, prevAnswer = answer).first()
        return writeResponse(ds, textSymptoms)

@csrf_exempt 
def predict(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        symptoms = body["symptoms"]
        symptom1 = symptoms[0]

        disease = Symptoms.objects.filter(symptom_1__icontains = symptom1)[:1][0].disease
        return JsonResponse({'disease': disease})

def predictQuestion(symptom1):
    disease = Symptoms.objects.filter(symptom_1__icontains = symptom1)[:1][0].disease
    if disease == 'GERD': disease = 'Heartburn'
    return JsonResponse({'disease': disease})

def checkTextSymptoms(ds, textSymptoms):
    symptomFound = ds.checkSymptom in textSymptoms
    while symptomFound:
        QuerySet = Questions.objects.filter(prevQuestion = ds.question, prevAnswer = textSymptoms[ds.checkSymptom])
        if len(QuerySet) > 1: ds = Questions.objects.filter(prevQuestion = ds.question, prevAnswer = textSymptoms[ds.checkSymptom], btn0UserText = 'pain').first()
        else: ds = Questions.objects.filter(prevQuestion = ds.question, prevAnswer = textSymptoms[ds.checkSymptom]).first()
        symptomFound = ds.checkSymptom in textSymptoms
    return ds

def writeResponse(ds, textSymptoms):
    if (ds.question == 'predict'): response = predictQuestion(ds.btn0UserText)
    elif (ds.question == 'Common Cold'): response = JsonResponse({'disease': ds.question})

    else:
        if ds.checkSymptom in textSymptoms: ds = checkTextSymptoms(ds, textSymptoms)
        data = QuestionsSerializer(ds).data
        data["textSymptoms"] = textSymptoms
        response = JsonResponse(data)
    return response

def NBCalc(pDisease, pSymptomsNon):
    return pDisease/(pDisease + pSymptomsNon * (1-pDisease))

@csrf_exempt 
def question(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        question = body["question"]
        answer = body["answer"]
        textSymptoms = body["textSymptoms"]

        QuerySet = Questions.objects.filter(prevQuestion = question, prevAnswer = answer)
        if len(QuerySet) > 1: ds = Questions.objects.filter(prevQuestion = question, prevAnswer = answer, checkSymptom = None).first()
        else: ds = Questions.objects.filter(prevQuestion = question, prevAnswer = answer).first()
        return writeResponse(ds, textSymptoms)



 # if message.startswith("Thank you") or message.startswith("Bye") or message.startswith("Thanks"):
        #      return JsonResponse({'message': "You’re welcome, do you have any additional concerns?"})

        # elif message.startswith("That's all"):
        #      return JsonResponse({'message': "Goodbye! Take care and hope you feel well soon!"})
        
        # elif message == "I have a cold":
        #      return JsonResponse({'message': "Common Cold"})

        # elif message.startswith("I feel") or message.startswith("I'm not") :
        #      return JsonResponse({'message': "What symptoms are you expressing?"})
             
        # elif message.startswith("I'm coughing"):
        #     return JsonResponse({'message': "Do you have any of these symptoms: congestion, a fever, runny nose?"})
    
        # elif message.startswith("I have all"):
        #     return JsonResponse({'message': "Have you eaten anything unusual lately?"})
    
        # elif message.startswith("My stomach"):
        #     return JsonResponse({'message': "Have you eaten anything unusual lately?"})

        # elif message.startswith("I think I did have"): 
        #     return JsonResponse({'message': "That makes sense! My prediction is that you have food poisoning"})

        # elif message.endswith("normal diet"): 
        #     return JsonResponse({'message': "Got it! My prediction is that you have the common cold"})

        # else:
        #     return JsonResponse({'message': "Sorry I didn't catch that. Could you phrase that differently?"})
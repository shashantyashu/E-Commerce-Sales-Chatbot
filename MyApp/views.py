from django.shortcuts import render, redirect
from django.http import JsonResponse
from datetime import datetime
from MyApp.models import Product
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer

intents = json.loads(open(r'C:\Users\user\Desktop\Projects\Assigment\E_Com\static\js\data.json').read())


bot =  ChatBot('chatbot', read_only=False, 
               logic_adapters=[
                   {
                   'import_path':'chatterbot.logic.BestMatch',
                   'default_response':'Sorry, Can you please tell me in brief',
                   'maximum_similarity_threshold':0.80,
                   }
                   ])

#chatterBotCorpusTrainer = ChatterBotCorpusTrainer(bot)
#chatterBotCorpusTrainer.train('chatterbot.corpus.english')
list_trainer = ListTrainer(bot)
list_trainer.train(intents['listToTrain'])


def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    products = Product.objects.all()
    return render(request, 'index.html',{'products': products } )

def show(request, id):
    if request.user.is_anonymous:
        return redirect("/login")
    products = Product.objects.all()
    context = {'id': id}
    data = {
        
        'context': context,
        'product': products,
    }
    
    return render(request, 'show.html', data)

def get_response(request):
    if request.user.is_anonymous:
        return redirect("/login")
    
    if request.method == "GET":
        
        user_message = request.GET.get('userMessage', None)
        if user_message:
            chatResponse = str(bot.get_response(user_message))
            return JsonResponse({"response": f"{chatResponse}"})
        else:
            return JsonResponse({"error": "No userMessage provided"}, status=400)

    
    return JsonResponse({"error": "Method not allowed"}, status=405)

def registerUser(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/explore')
    else:
        initial_data = {'username':"", 'password1':"", 'password2':""}
        
        
        form = UserCreationForm(initial=initial_data)
        print(form)
    return render(request, 'auth/register.html',{'form':form})


def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
           
            login(request, user)
            return redirect("/explore")
        else:
            
            return render(request, 'login.html')    
    
    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect('/login')
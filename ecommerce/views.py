from django.contrib.auth import authenticate, login, logout, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm

def home_page(request):
    print(request.session.get('first_name', 'Unknow'))
    context = {
        'title': 'Página principal',
        'content': 'Bem vindo apágina principal'
    }
    if request.user.is_authenticated:
        context['premiun_content'] = 'Voçê é um usuário Premiun'
    return render(request, 'home_page.html', context)

def about_page(request):
    context = {
        'title': 'Página sobre',
        'content': 'Bem vindo a página sobre'
    }    
    return render(request, 'about/view.html', context)

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        'title': 'Página de contato',
        'content': 'Bem vindo a página de contato',
        'form': contact_form
    }  
    if contact_form.is_valid():
        print(contact_form.cleaned_data) 
    return render(request, 'contact/view.html', context)

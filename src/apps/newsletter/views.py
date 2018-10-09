from django.shortcuts import render, redirect
from .models import dadosHome

# Imports do Newsletter
from .forms import UnirForm
# from django.http import HttpResponseRedirect

# Imports do Google Key
from django.conf import settings
from django.contrib import messages
import urllib
import json

from src.settings import AWS_S3_CUSTOM_DOMAIN


def home(request):
    info = dadosHome.objects.all()
    if request.method == 'POST':
        form = UnirForm(request.POST or None)
        if form.is_valid():
            ''' Começo da validação reCAPTCHA '''
            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response,
            }
            data = urllib.parse.urlencode(values).encode()
            req = urllib.request.Request(url, data=data)
            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode())
            ''' Final da reCAPTCHA '''
            if result['success']:
                form = form.save()
                messages.success(request, 'Contato cadastrado com sucesso!')
            else:
                messages.error(request, 'reCAPTCHA inválido. Por favor, tente novamente')
            return redirect('core:homepage')
    else:
        form = UnirForm()

    context = {
        'dados': info,
        'form': form,
        'aws': AWS_S3_CUSTOM_DOMAIN,
    }
    return render(request, 'home.html', context)

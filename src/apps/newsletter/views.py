from django.shortcuts import render
from .models import dadosHome

from .forms import UnirForm
from django.http import HttpResponseRedirect


def home(request):
    info = dadosHome.objects.all()
    if request.method == 'POST':
        form = UnirForm(request.POST or None)
        if form.is_valid():
            form = form.save(commit=True)
        return HttpResponseRedirect('/')
    else:
        form = UnirForm()

    context = {
        'info': info,
        'form': form,
    }
    return render(request, 'home.html', context)

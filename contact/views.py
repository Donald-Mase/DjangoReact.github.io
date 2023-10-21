from django.shortcuts import render
from django.utils.http import is_safe_url
from django.conf import settings
from django.shortcuts import render, redirect
from .models import contact
from .form import contactForm
from .serializer import contactSerializer

# Create your views here.

ALLOWED_HOSTS = settings.ALLOWED_HOSTS
def create_contact(request, *args, **kwargs):
    form = contactForm(request.POST or None)
    next_url = request.POST.get('next') or None
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        if next_url != None and is_safe_url(next_url,ALLOWED_HOSTS):
            return redirect(next_url)
        form = contactForm()
    return render(request, 'components/contactform.html', context={'form': form})
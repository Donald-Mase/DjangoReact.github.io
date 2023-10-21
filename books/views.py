from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse
from django.utils.http import is_safe_url
from django.conf import settings

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Books
from .form import BooksForm
from .serializer import BooksSerializer


ALLOWED_HOSTS = settings.ALLOWED_HOSTS


# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, 'pages/home.html', context= {},status =200)

@api_view(['GET'])
def book_detail_view(request, book_id, *args, **kwargs):
    data = {
        "id": book_id
    }
    status = 200
    try:
        obj =Books.objects.get(id =book_id)
        data['name'] = obj.name
        data['author'] = obj.author
        data['description'] = obj.description
    except:
        data['message'] = "Not found"
    status = 404
    return JsonResponse(data, status =status)

def books_list(request, *args, **kwargs):
    blist = Books.objects.all()
    books =[x.serialize() for x in blist]
    data = {"response": books }
    return JsonResponse(data)

@api_view(['POST'])
def book_create_view(request, *args, **kwargs):
    print(request.POST)
    serializer = BooksSerializer(data=request.data or None)
    if serializer.is_valid(raise_exception = True):
        serializer.save()
        return Response(serializer.data)
    return Response({}, status=400)

# without serializer
def book_create_view_pure(request, *args, **kwargs):
    form = BooksForm(request.POST or None)
    next_url = request.POST.get('next') or None
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        if next_url != None and is_safe_url(next_url,ALLOWED_HOSTS):
            return redirect(next_url)
        form = BooksForm()
    return render(request, 'components/form.html', context={'form': form})
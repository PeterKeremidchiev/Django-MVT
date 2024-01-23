from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


# Create your views here.


def response_for_empty_path(request):
    return HttpResponse("Enter something")
def response_to_pk(request, pk):
    return HttpResponse(f"hello customer with ID:{pk}")

def response_with_str(request, name):
    context = {
        'name': name,
        'path': request.path,
    }
    return render(request, 'core/index.html', context)

def response_to_name_and_pk(request, name, pk):
    context = {
        'name': name,
        'id': pk,
    }
    return render(request, 'core/index2.html', context)

def redirect_to_softuni(request):
    return redirect("https://softuni.bg")

def raise_error(request):
    return HttpResponseNotFound(status=404,)

def raise_exception(request):
    raise Http404
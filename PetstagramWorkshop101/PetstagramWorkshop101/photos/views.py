from django.shortcuts import render

# Create your views her

# Create your views here.
def add_photo_page(request):
    context = {}

    return render(request, 'photos/photo-add-page.html', context)


def photo_details_page(request, pk):
    context = {}

    return render(request, 'photos/photo-details-page.html', context)


def edit_photo_page(request, pk):
    context = {}

    return render(request, 'photos/photo-edit-page.html', context)
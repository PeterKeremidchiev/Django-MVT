from django.shortcuts import render, redirect


# Create your views here.
def register_page(request):
    context = {}

    return render(request, 'accounts/register-page.html', context)

def login_page(request):
    context = {}

    return render(request, 'accounts/login-page.html', context)

def sign_out_page(request):
    context = {}

    return redirect('home')

def show_profile_details(request, pk):
    context = {}

    return render(request, 'accounts/profile-details-page.html', context)

def edit_profile(request, pk):
    context = {}

    return render(request, 'accounts/profile-edit-page.html', context)

def delete_profile(request, pk):
    context = {}

    return render(request, 'accounts/profile-delete-page.html', context)
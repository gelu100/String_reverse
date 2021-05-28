from django.contrib import messages
from django.shortcuts import render
from .forms import *


# Create your views here.
def registerPage(request):
    form = CreateUserForm
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            Customer.objects.create(
                user=user,
                name=user.username,
            )

            messages.success(request, 'Account was created for ' + username)
    context = {'forms':form}
    return render(request, 'BookingPlaner/register.html',context)

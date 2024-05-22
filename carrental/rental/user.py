from django.shortcuts import render, redirect
from django.contrib import messages
from . import forms

def login(request):
    return render(request,'login.html.jinja')

def logout(request):
    return render(request,'logout.html.jinja')

def register(request):
    if request.method == 'POST':
        user_form = forms.RegistrationForm(request.POST)
        address_formset = forms.UserAddressFormSet(request.POST)
        if user_form.is_valid() and address_formset.is_valid():
            # Zapisz użytkownika
            user = user_form.save()
            # Zapisz adresy użytkownika
            addresses = address_formset.save(commit=False)
            for address in addresses:
                address.user = user
                addresses.save()
            return render(request,'register.html.jinja', {'message', 'Success!'})
        return render(request,'register.html.jinja', {'message', 'Coś poszło nie tak'})
    else:
        form = forms.RegistrationForm()
        form_address = forms.UserAddressFormSet()
        return render(request,'register.html.jinja', {'form': form, 'form_address': form_address})
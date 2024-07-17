from django.shortcuts import render, redirect
from . import views
from . import forms
# Create your views here.
def add_profile(request):
    if request.method == 'POST':
        profle_form = forms.ProfileForm(request.POST)
        if profle_form.is_valid():
            profle_form.save()
            return redirect('add_profile')
        
    else:
        profle_form = forms.ProfileForm()
    
    return render (request, 'add_profile.html', {'form': profle_form})
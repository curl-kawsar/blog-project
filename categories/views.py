from django.shortcuts import render, redirect
from . import views
from . import forms
# Create your views here.
def add_category(request):
    if request.method == 'POST':
        cate_form = forms.CateForm(request.POST)
        if cate_form.is_valid():
            cate_form.save()
            return redirect('add_category')
        
    else:
        cate_form = forms.CateForm()
    
    return render (request, 'add_category.html', {'form': cate_form})
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            new_name = form.cleaned_data['name']

            return HttpResponseRedirect('/thanks/')
    else:
        form = NameForm()

    return render(request, 'form.html', {'form': form})
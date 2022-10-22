from django import forms

class VoteForm(forms.Form):
    vote = forms.ChoiceField(label='choice',  widget=forms.RadioSelect)
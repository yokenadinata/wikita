from django import forms

class InputForm(forms.Form):
    input = forms.CharField(label='Masukkan nama', max_length=20)
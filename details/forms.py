from django import forms


class EditForm(forms.Form):
    color = forms.CharField(label="Color")

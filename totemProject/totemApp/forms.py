from django import forms
from totemApp.models import *

# The following two forms are commented out because they were only used to add a set number of
# continents (7) and classifications (11). 
# class ContinentsForm(forms.ModelForm):
#     class Meta:
#         model = Continents 
#         fields = ['continent']
#         labels = {'continent': "Continent"}

# class AnimalClassForm(forms.ModelForm):
#     class Meta:
#         model = AnimalClass
#         fields = ['classification']
#         labels = {'classification': "Classification"} 


# Credit to Rafiq Hilali for "forms.BooleanField(widget=forms.HiddenInput, initial=True)" in order to have multiple forms on one page
#  @ https://openclassrooms.com/en/courses/7107341-intermediate-django/7264795-include-multiple-forms-on-a-page
class CountriesForm(forms.ModelForm):
    c_r_u_dCountries = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = Countries
        fields = ['country', 'continent']
        labels = {'country': "Country", 'continent': "Continent"}

class VertebratesForm(forms.ModelForm):
    c_r_u_dVertebrates = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = Vertebrates
        fields = ['classification', 'animal', 'country', 'meaning']
        labels = {'classification': "Class", 'animal': "Animal", 'country': "Country", 'meaning': "Symbolic Meaning"}

class InvertebratesForm(forms.ModelForm):
    c_r_u_dInvertebrates = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    
    class Meta:
        model = Invertebrates
        fields = ['classification', 'animal', 'country', 'meaning']
        labels = {'classification': "Class", 'animal': "Animal", 'country': "Country", 'meaning': "Symbolic Meaning"}
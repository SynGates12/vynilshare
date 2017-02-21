from django import forms

class SearchForm(forms.Form):
    CHOICE_L = (
                ( 'TITOL', 'titol'),
                ( 'GRUP', 'grup'),
                ( 'GENERE', 'genere'),
                )
    tipus_de_recerca = forms.CharField(max_length=100,widget=forms.Select(choices=CHOICE_L),)
    text = forms.CharField(max_length=400)
    
    
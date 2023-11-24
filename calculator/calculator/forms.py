from django import forms

class userform(forms.Form):
    ch=(('+', '+'), ('-','-'),('*','*'),('/','/'))
    num1=forms.IntegerField(label="First Number", required=True, widget=forms.NumberInput())
    op=forms.ChoiceField(label='Operator', choices=ch, required=True)
    num2=forms.IntegerField(label='Second Number', required=True)
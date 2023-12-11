from django import forms
from . models import TicketBook

class TicketBookForm(forms.ModelForm):
    class Meta:
        model = TicketBook
        fields = ['first_name', 'last_name', 'email', 'countryName', 'pfrom', 'pto', 'depatureDate', 'returnDate', 'chosen_option']
        widgets = {
            'departure_date': forms.DateInput(attrs={'type': 'date'}),
            # 'chosen_option': forms.RadioSelect()
        }
    depatureDate = forms.DateField(
        # label='Task Assign Date',
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=True 
    )
    returnDate = forms.DateField(
        # label='Task Assign Date',
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=True 
    )
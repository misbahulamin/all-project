from django import forms
from . models import TaskModel

class TaskModelForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = '__all__'
        
    taskAssignDate = forms.DateField(
        label='Task Assign Date',
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=True  # Set this to True if the field is required
    )
from django import forms
from .models import Employee
from django.core.validators import RegexValidator
class EmployeeForm(forms.ModelForm):
    emp_contact = forms.CharField(max_length=10, validators=[RegexValidator(
        '\d{10}', message="Enter a Valid Indian Phone Number")])
 
    class Meta:
        model = Employee
        fields = ('emp_id','emp_name', 'emp_email', 'emp_contact', 'emp_role', 'emp_salary')

        widgets = {
            'emp_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'id'}),
            'emp_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'emp_email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'emp_contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact No.'}),
            'emp_role': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Role'}),
            'emp_salary': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Salary'}),
        }
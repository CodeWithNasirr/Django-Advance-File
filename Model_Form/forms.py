from django import forms
from test_study.models import Student
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields=['name','number']
        # fields = "__all__" 
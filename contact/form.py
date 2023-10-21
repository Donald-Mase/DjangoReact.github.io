from django import forms

from .models import contact

class contactForm(forms.ModelForm):
    class Meta:
        model = contact
        fields = ['Name','Email','Subject','Message']
    def clean_subject(self):
        subject = self.cleaned_data.get('subject')
        if len(subject) > 300:
            raise forms.ValidationError("This is too long")
        return subject
from django import forms
from .models import ContactPost
from .models import Subscribe

class ContactModelForm(forms.ModelForm):
    
    class Meta:
        
        model = ContactPost
        fields = ['user_name', 'user_email', 'company_name', 'user_message']


class SubscribeModelForm(forms.ModelForm):

    class Meta:

        model = Subscribe
        fields = ['subscribe_email']
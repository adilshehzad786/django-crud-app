from django import forms  
from contacts.models import Contacts

#Django allows us to create form based on Model/Schema design.
#To do so, we will create form based on 'Contact' model with all fields in it.
class ContactForm(forms.ModelForm):  
    class Meta:  
        model = Contacts
        fields = "__all__"
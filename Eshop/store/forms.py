from django import forms
from .models import ShippingAddress
from django_countries.fields import CountryField
from phonenumber_field.formfields import PhoneNumberField

PAYMENT_CHOICES = (
    ('S', 'Stripe'),
    ('P', 'Paypal')
)
DELIVERY_CHOICES = (
    ('S', 'Standard'),
    ('P', 'Premium')
)

class ShippingForm(forms.ModelForm):
    add1 = forms.CharField(label='Addresse1 :', widget=forms.TextInput(attrs={'placeholder':'1234 Main St'}))
    add2 = forms.CharField(label='Addresse2 :', widget=forms.TextInput(attrs={'placeholder':'Apartment or suite'}))
    number_phone = PhoneNumberField(label='Phone Number :', widget=forms.TextInput(attrs={'placeholder':'Phone Number us +xxx'}))
    country = CountryField(blank_label='Select country').formfield()
    zip_code = forms.CharField(label='Zip code :', widget=forms.TextInput(attrs={'placeholder':'Zip Code'}))
    city = forms.CharField(label='City :', widget=forms.TextInput(attrs={'placeholder': 'City'}))
    payment_option = forms.ChoiceField(widget=forms.RadioSelect, choices=PAYMENT_CHOICES, initial='S')
    delivery_option = forms.ChoiceField(widget=forms.RadioSelect, choices=DELIVERY_CHOICES, initial='S')
    class Meta:
        model = ShippingAddress
        fields = ['add1', 'delivery_option', 'add2', 'city', 'country', 'number_phone', 'zip_code', 'payment_option']


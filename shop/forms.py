from django.forms import ModelForm, FileInput
from shop.models import Payment, Supplier
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class PaymentForm(ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'
        exclude = ['supplier']



class SupplierForm(ModelForm):
    class Meta:
        model = Supplier
        fields = '__all__'        
        


class CreateUserForm(UserCreationForm):
    class Meta:
        model  = User
        fields = ['username','email','password1','password2']
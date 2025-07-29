from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *

class CreateUserForm (UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class CustomerForm (ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user', 'name']

class DepositForm (ModelForm):
    class Meta:
        model = Deposit
        fields = '__all__'
        exclude = ['user', 'name']

class WalletForm (ModelForm):
    class Meta:
        model = Wallet
        fields = '__all__'
        exclude = ['user', 'name']

class WithdrawalertForm (ModelForm):
    class Meta:
        model = Withdrawalert
        fields = '__all__'
        exclude = ['user', 'name']

class GeneralalertForm (ModelForm):
    class Meta:
        model = Generalalert
        fields = '__all__'
        exclude = ['user', 'name']

class PinForm (ModelForm):
    class Meta:
        model = Pin
        fields = '__all__'
        exclude = ['user', 'name']
    
class TransactionForm (ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'
        exclude = ['user', 'name']
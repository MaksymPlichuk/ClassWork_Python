from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.forms import AuthenticationForm

from users.models import CustomUser 


class CustomUserRegisterForm(UserCreationForm):
    email = forms.EmailField(
       label="Email from form.py",
       required=True,
       widget=forms.TextInput(attrs={
          'class': 'w-full rounded-lg border border-gray-700 bg-gray-900 px-4 py-3 text-white placeholder-gray-500 focus:border-indigo-500 focus:outline-none', 
          'placeholder': 'example@gmail.com'
         })
      )
    first_name = forms.CharField(
       label="Ім\'я",
       required=True,
       widget=forms.TextInput(attrs={
          'class': 'w-full rounded-lg border border-gray-700 bg-gray-900 px-4 py-3 text-white placeholder-gray-500 focus:border-indigo-500 focus:outline-none', 
          'placeholder': 'Ім\'я з forms.py'
         })
      )
    last_name = forms.CharField(
       label="Прізвище",
       required=True,
       widget=forms.TextInput(attrs={
          'class': 'w-full rounded-lg border border-gray-700 bg-gray-900 px-4 py-3 text-white placeholder-gray-500 focus:border-indigo-500 focus:outline-none', 
          'placeholder': 'Прізвище з forms.py'
         })
      )
    image = forms.ImageField(
       label="Зображення",
       widget=forms.FileInput(attrs={
          'class': 'block w-full text-sm text-gray-400 '
                     'file:mr-4 file:py-2 file:px-4 '
                     'file:rounded-lg file:border-0 '
                     'file:text-sm file:font-semibold '
                     'file:bg-indigo-600 file:text-white '
                     'hover:file:bg-indigo-500 '
                     'cursor-pointer',
          'accept': 'image/*',
         })
      )
    password1 = forms.CharField(
       label="Password",
       required=True,
       widget=forms.PasswordInput(attrs={
          'class': 'w-full rounded-lg border border-gray-700 bg-gray-900 px-4 py-3 text-white placeholder-gray-500 focus:border-indigo-500 focus:outline-none', 
          'placeholder': 'Password з forms.py'
         })
      )
    password2 = forms.CharField(
       label="Repeat Password",
       required=True,
       widget=forms.PasswordInput(attrs={
          'class': 'w-full rounded-lg border border-gray-700 bg-gray-900 px-4 py-3 text-white placeholder-gray-500 focus:border-indigo-500 focus:outline-none', 
          'placeholder': 'Password з forms.py'
         })
      )
    
    class Meta:
      model = CustomUser
      fields = ("email","first_name","last_name","image","password1","password2")  

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("Дана пошта уже зареєстрована")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Паролі не співпадають.")
        return password2

class CustomUserLoginForm(AuthenticationForm):
    email = forms.EmailField(
        label='Електронна пошта',
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'w-full rounded-lg border border-gray-700 bg-gray-900 px-4 py-3 text-white placeholder-gray-500 focus:border-indigo-500 focus:outline-none',
            'placeholder': 'example@gmail.com'
        })
    )

    password = forms.CharField(
        label='Пароль',
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'w-full rounded-lg border border-gray-700 bg-gray-900 px-4 py-3 text-white placeholder-gray-500 focus:border-indigo-500 focus:outline-none',
            'placeholder': 'Вкажіть пароль'
        })
    )

from django.contrib.auth.forms import UserCreationForm
from django import forms


from users.models import CustomUser 


class CustomUserForm(UserCreationForm):
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
      fields = ("email","first_name","password","image","password1","password2",)  


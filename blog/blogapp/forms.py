from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Post, Comment

class RegistrationForm(UserCreationForm):
    # Додайте поля, які вам потрібні для реєстрації користувачів
    # Наприклад: email, ім'я, прізвище і т.д.
    email = forms.EmailField()

    class Meta:
        model = "User"
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    # Використовуйте вбудовану форму AuthenticationForm для авторизації
    pass

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'content']
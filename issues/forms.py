from django.contrib.auth.forms import UserCreatrionForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        Fields = UsrCreationForm.Meta.filds + ('email', 'role', 'team')

class CustomUserChangeForm(UsewrChangeForm):
    class Meta(UserChangeForm):
        model = CustomUser
        fields = UserChangeForm.Meta.fields
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()

class ExetendedUserCreationForm:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].wighet.attrs['class'] = 'form-control form-control-lg'
        self.fields['firstname'].wighet.attrs['class'] = 'form-control form-control-lg'
        self.fields['lastname'].wighet.attrs['class'] = 'form-control form-control-lg'
        self.fields['password1'].wighet.attrs['class'] = 'form-control form-control-lg'
        self.fields['password2'].wighet.attrs['class'] = 'form-control form-control-lg'

    class Meta:
        model = User
        fields = ['username', 'firstname', 'lastname', 'password1', 'password2']
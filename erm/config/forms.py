from django import forms


LEVEL_CHOICES = [
    (0, "Read Only"),
    (1, "Update"),
    (2, "Admin"),
]

class AddUserForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    level = forms.TypedChoiceField(choices=LEVEL_CHOICES, label="Access Level",
                                   coerce=int, empty_value=0)

from django import forms
from users.models import Main, Firstname, Surname, Patronymic, Street


class UserForm(forms.ModelForm):
    class Meta:
        model = Main
        fields = ['surname', 'firstname', 'patronymic',
                  'street', 'house', 'corpus', 'apartments', 'phone']

    firstname = forms.ModelChoiceField(
        queryset=Firstname.objects.all(), required=False)
    surname = forms.ModelChoiceField(
        queryset=Surname.objects.all(), required=False)
    patronymic = forms.ModelChoiceField(
        queryset=Patronymic.objects.all(), required=False)
    street = forms.ModelChoiceField(
        queryset=Street.objects.all(), required=False)
    house = forms.CharField(required=False)
    corpus = forms.CharField(required=False)
    apartments = forms.IntegerField(required=False)
    phone = forms.CharField(required=False)


class EditForm(forms.ModelForm):
    class Meta:
        model = Main
        fields = '__all__'


class SurnameForm(forms.ModelForm):
    class Meta:
        model = Surname
        fields = '__all__'


class FirtsnameForm(forms.ModelForm):
    class Meta:
        model = Firstname
        fields = '__all__'


class PatronymicForm(forms.ModelForm):
    class Meta:
        model = Patronymic
        fields = '__all__'


class StreetForm(forms.ModelForm):
    class Meta:
        model = Street
        fields = '__all__'


class EditSurnameForm(forms.ModelForm):
    class Meta:
        model = Surname
        fields = '__all__'


class EditFirstnameForm(forms.ModelForm):
    class Meta:
        model = Firstname
        fields = '__all__'


class EditPatronymicForm(forms.ModelForm):
    class Meta:
        model = Patronymic
        fields = '__all__'


class EditStreetForm(forms.ModelForm):
    class Meta:
        model = Street
        fields = '__all__'

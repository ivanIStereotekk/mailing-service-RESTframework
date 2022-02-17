
from django.forms import*
from .models import*
from django.contrib.auth.forms import*




class SearchForm (forms.Form):
    '''Поиск на front'''
    keyword = forms.CharField(max_length=30,label='Кто ищет тот всегда найдет!',required=False)


class Customer_Creation_Form(UserCreationForm):
    '''Form That creates Customer (Front - User)'''
    class Meta:
        model = Customer
        fields = UserCreationForm.Meta.fields +(
            'username','gender','password','email',
            'first_name','last_name','birth_date',
            'phone_number','user_type','adress')
        help_text ={'username':'Чтобы сменить email, пройдите по ссылке ниже формы'}

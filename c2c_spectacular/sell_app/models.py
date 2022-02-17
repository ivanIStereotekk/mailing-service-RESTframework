
from django.contrib.auth.models import*

from django.contrib.auth.models import AbstractUser,User



class Customer(AbstractUser):
    GENDER = (('м','мужчина'),('ж','женщина'),)
    USER_TYPE = (('юр.лицо', 'организация'), ('физ.лицо', 'частный клиент'),)
    gender = models.CharField(max_length=1, verbose_name='Пол',choices=GENDER)
    birth_date = models.DateField(verbose_name='Дата рождения', default='1979-05-28',blank=True)
    phone_number = models.CharField(max_length=12, verbose_name='Номер телефона',blank=True)
    user_type = models.TextField(max_length=8, blank=True,choices=USER_TYPE, verbose_name='физ.лицо/орг.')
    adress = models.CharField(max_length=150, blank=True, verbose_name='Адрес')
    registred = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Зарегистрирован')
    class Meta:
        verbose_name_plural = 'Клиенты'
        verbose_name = 'Клиент'
        ordering = ['user_type','user','registred',]

class Good(models.Model):
    code = models.CharField(max_length=250, verbose_name='Код товара',blank=True,unique=True)
    quantity = models.IntegerField(max_length=10,verbose_name='Едениц товара',null=True)
    customer = models.ForeignKey(Customer,on_delete=models.PROTECT,verbose_name='Пользователь',blank=True)
    description = models.CharField(max_length=250, verbose_name='Наименование товара',blank=True)
    class Meta:
        verbose_name_plural = 'Товары'
        verbose_name = 'Товар'
        ordering = ['customer','code','description','quantity',]






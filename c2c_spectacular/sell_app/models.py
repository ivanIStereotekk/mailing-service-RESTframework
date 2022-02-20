
from django.contrib.auth.models import*

from django.contrib.auth.models import AbstractUser

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token




class Customer(AbstractUser):
    GENDER = (('м','мужчина'),('ж','женщина'),)
    gender = models.CharField(max_length=1, verbose_name='Пол',choices=GENDER)
    birth_date = models.DateField(verbose_name='Дата рождения', default='1979-05-28',blank=True)
    phone_number = models.CharField(max_length=12, verbose_name='Номер телефона',blank=True,unique=True)
    adress = models.CharField(max_length=150, blank=True, verbose_name='Адрес')
    registred = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Зарегистрирован')
    #auth_key = models.CharField(max_length=250, verbose_name='Auth_key', blank=True, unique=True)

    class Meta:
        verbose_name_plural = 'Клиенты'
        verbose_name = 'Клиент'
        ordering = ['username','registred','phone_number',]

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class Good(models.Model):
    code = models.CharField(max_length=250, verbose_name='Код товара',blank=True,unique=True)
    quantity = models.IntegerField(verbose_name='Едениц товара',null=True)
    customer = models.ForeignKey(Customer,on_delete=models.PROTECT,verbose_name='Пользователь',blank=True)
    description = models.CharField(max_length=250, verbose_name='Наименование товара',blank=True)
    class Meta:
        verbose_name_plural = 'Товары'
        verbose_name = 'Товар'
        unique_together = ['customer','code']
        ordering = ['customer','code','description','quantity',]






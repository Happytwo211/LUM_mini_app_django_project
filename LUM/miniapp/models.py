
from django.db import models
from django.contrib.auth.models import User


class Benefits(models.Model):
    promo_code = 'PC'
    bonus = 'BO'
    bonus_currnecy = 'BC'

    POSITIONS = [
        (promo_code, 'Промо-Код'),
        (bonus, 'Бонусы'),
        (bonus_currnecy, 'Баллы'),

    ]

    benefits_type = models.CharField(max_length=2, choices=POSITIONS)

    def __str__(self):
        return f'{self.benefits_type}'

class User_benefits_data(models.Model):
    user = models.ForeignKey(
        to=User, default=0, on_delete=models.CASCADE)
    # user_benefits_type = models.ForeignKey(Benefits, on_delete=models.CASCADE)
    user_benefits_type = models.ManyToManyField(Benefits)
    user_benefits_quantity = models.IntegerField(default=0)

    def user_name(self):
        return self.user.get_username()
    def __str__(self):
        return f'Пользователь:{self.user}-Количество бонусов:{self.user_benefits_quantity}'


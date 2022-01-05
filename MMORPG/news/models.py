from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    authorUser = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.authorUser}'


class Post(models.Model):
    Tank = 'Танк'
    Heal = 'Хиллы'
    DD = 'ДД'
    SELLERS = 'Торговцы'
    GILDMASTERS = 'Гилдмастеры'
    KVESTGRS = 'Квестгиверы'
    BLACKSMITHS = 'Кузнецы'
    LEATHERWRKS = 'Кожевники'
    CHEMISTS = 'Зельевары'
    SPELLMASTERS = 'Мастера Заклинаний'
    CATEGORY_CHOICES = [
        (Tank, 'Танк'),
        (Heal, 'Хиллы'),
        (DD, 'ДД'),
        (SELLERS, 'Торговцы'),
        (GILDMASTERS, 'Гилдмастеры'),
        (KVESTGRS, 'Квестгиверы'),
        (BLACKSMITHS, 'Кузнецы'),
        (LEATHERWRKS, 'Кожевники'),
        (CHEMISTS, 'Зельевары'),
        (SPELLMASTERS, 'Мастера Заклинаний')
    ]

    title = models.CharField(unique=True, max_length=128)
    text = models.TextField(verbose_name='text')
    date_creation = models.DateTimeField(auto_now_add=True)
    category = models.CharField(choices=CATEGORY_CHOICES,
                                default='Tank',
                                verbose_name='Category',
                                max_length=18
                                )
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.title}:{self.text}'

    def preview(self):
        return {self.text}[0:30]+'...'

class Comment(models.Model):
    user_comment = models.ForeignKey(User, on_delete=models.CASCADE)
    text_comment = models.TextField(verbose_name='comment text')
    post_comment = models.ForeignKey(Post, on_delete=models.CASCADE)
    time_comment = models.DateTimeField(auto_now_add=True)





# Create your models here.

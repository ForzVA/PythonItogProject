from django.db import models
from django.contrib.auth.models import User




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

    title = models.CharField(unique=True,
                             max_length=128,
                             verbose_name='Название'
                             )
    text = models.TextField(verbose_name='131')
    date_creation = models.DateTimeField(auto_now_add=True)
    category = models.CharField(choices=CATEGORY_CHOICES,
                                default='Tank',
                                verbose_name='Категория',
                                max_length=18
                                )
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               verbose_name='Автор'
                               )
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating += 1
        self.save()

    def __str__(self):
        return f'{self.title}:{self.text}'

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Comment(models.Model):
    user_comment = models.ForeignKey(User, on_delete=models.CASCADE)
    text_comment = models.TextField(verbose_name='Текст коммента')
    post_comment = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments_posts')
    time_comment = models.DateTimeField(auto_now_add=True)
    status_comment = models.BooleanField(verbose_name='Статус коммента', default=False)

    def __str__(self):
        return f'{self.user_comment}{self.time_comment}'


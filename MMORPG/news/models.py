from django.db import models
from django.contrib.auth.models import User
from pkg_resources import UnknownExtra
from .middleware import get_current_user
from django.db.models import Q




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


class StatusComments(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(Q(status_comment=False, user_comment=get_current_user()) |
                                             Q(status_comment=False, post_comment__author=get_current_user()) |
                                             Q(status_comment=True)
                                             )


class Comment(models.Model):
    user_comment = models.ForeignKey(User,
                                     on_delete=models.CASCADE,
                                     verbose_name='Автор комментария')
    text_comment = models.TextField(verbose_name='Текст коммента')
    post_comment = models.ForeignKey(Post,
                                     on_delete=models.CASCADE,
                                     related_name='comments_posts',
                                     verbose_name='Комментируемый пост')
    time_comment = models.DateTimeField(auto_now_add=True,
                                        verbose_name='Дата комментария')
    status_comment = models.BooleanField(verbose_name='Статус коммента',
                                         default=False,
                                        )
    objects = StatusComments()

    def __str__(self):
        return f'{self.user_comment}{self.time_comment}'


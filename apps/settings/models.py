from django.db import models

# Create your models here.
class Basesettings(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок сайта'
    )
    logo = models.ImageField(
        upload_to='logo/',
        verbose_name='Логотип сайта'
    )
    facebook = models.URLField(
        verbose_name='Ссылка на facebook'
    )
    twitter = models.URLField(
        verbose_name='Ссылка на twitter'
    )
    github = models.URLField(
        verbose_name='Ссылка на Github'
    )
    google = models.URLField(
        verbose_name='Ссылка на Google +'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Основная настройка сайта'
        verbose_name_plural = 'Основные настройки сайта'
        
        
class Employees(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Имя сотрудника"
    )
    image = models.ImageField(
        upload_to='image/',
        verbose_name="Фото сотрудника"       
    )
    position = models.CharField(
        max_length=255,
        verbose_name='Должность'
    )
    facebook = models.URLField(
        verbose_name='Ссылка на facebook'
    )
    twitter = models.URLField(
        verbose_name='Ссылка на twitter'
    )
    github = models.URLField(
        verbose_name='Ссылка на Github'
    )
    google = models.URLField(
        verbose_name='Ссылка на Google +'
    )
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
        
        
class Blog(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Загаловок блога"
    )
    description = models.TextField(
        verbose_name="Описание блога"
    )
    image = models.ImageField(
        upload_to='image_blog/',
        verbose_name="Фото блога"
    )
    date = models.DateField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )
    comment = models.CharField(
        max_length=255,
        verbose_name="Комментарии"
    )
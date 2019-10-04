from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Автор")
    title = models.CharField(max_length=200, verbose_name="Тема")
    text = models.TextField(verbose_name="Пост")
    created_date = models.DateTimeField(default=timezone.now, verbose_name="Дата создания")
    published_date = models.DateTimeField(blank=True, null=True, verbose_name="Дата публикации")

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ("обсуждение")
        verbose_name_plural = ("Форум")

class Video(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    link = models.CharField(max_length=200, verbose_name="Ссылка")
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ("видео")
        verbose_name_plural = ("Видео")

        
class About(models.Model):
    text = models.TextField(verbose_name="Абзац")

    def __str__(self):
        return self.text
    
    class Meta:
        verbose_name = ("описание")
        verbose_name_plural = ("Главная")

class News(models.Model):   
    title = models.CharField(max_length=200, verbose_name="Тема")
    text = models.TextField(verbose_name="Пост")
    created_date = models.DateTimeField(default=timezone.now, verbose_name="Дата создания")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ("новость")
        verbose_name_plural = ("Новости")

class Contacts(models.Model):   
    phone = models.CharField(max_length=200, verbose_name="Телефон")
    mail = models.CharField(max_length=200, verbose_name="Почта", blank=True)
    adress = models.CharField(max_length=200, verbose_name="Адрес", blank=True)    

    def __str__(self):
        return self.phone

    class Meta:
        verbose_name = ("контакт")
        verbose_name_plural = ("Контакты")

class Comments(models.Model):   
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name="Пользователь")
    post = models.ForeignKey(Post, verbose_name="Новость", on_delete=models.CASCADE)
    text = models.TextField("Комментарий")
    created = models.DateTimeField(default=timezone.now, verbose_name="Дата создания")
    
    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return "{}".format(self.user)

class Image(models.Model):
    image = models.ImageField(upload_to='images', blank=True)
    name = models.CharField(max_length=200, blank=True)
	
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ("фото")
        verbose_name_plural = ("Фотографии")

class Bible(models.Model):
    text = models.TextField("Цытата")
    link = models.CharField(max_length=200, verbose_name="Книга/глава/стих")
    
    def __str__(self):
        return self.text

    class Meta:
        verbose_name = ("цитата")
        verbose_name_plural = ("Библия")

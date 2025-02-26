from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Application(models.Model):
    class Type(models.IntegerChoices):
        REFERENCE = 0
        IMAGE = 1
        VIDEO = 2
        
    FOLDER_Name = 'uploads'
    Upload_path = models.FileField(
        null=True, blank=True,
        upload_to = "uploads/%Y/%m/%d/",
    )
    
    application_type = models.IntegerField(
        choices=Type.choices,
        null=False, blank=True,
    )
    application_file = models.FileField(
    null=True, blank=True,
    upload_to = "uploads/%Y/%m/%d/",
    )

    
    class Meta:
        verbose_name = "Приложение"
        verbose_name_plural = "Приложения"


class Topic(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Section(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название секции")
    description = models.TextField(verbose_name="Описание секции")
    image = models.ImageField(upload_to='section_images/', verbose_name="Изображение секции")
    is_active = models.BooleanField(default=True, verbose_name="Активно")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Секция"
        verbose_name_plural = "Секции"


class Test(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='tests', verbose_name="Секция")
    title = models.CharField(max_length=200, verbose_name="Название теста")
    description = models.TextField(verbose_name="Описание теста")
    is_active = models.BooleanField(default=True, verbose_name="Активно")

    def __str__(self):
        return f"{self.title} (Секция: {self.section.title})"

    class Meta:
        verbose_name = "Тест"
        verbose_name_plural = "Тесты"

class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='questions')
    text = models.CharField(max_length=500)
    image = models.ImageField(upload_to='question_images/', null=True, blank=True)
    redirect_to = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Перенаправить на вопрос')
    
    def __str__(self):
        return self.text

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)
    result_message = models.TextField(blank=True, null=True)
    result_image = models.ImageField(upload_to='result_images/', null=True, blank=True)  
    redirect_to = models.ForeignKey(Question, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Перенаправить на вопрос', related_name='redirected_answers')

    def __str__(self):
        return self.text
    


class ChatMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    message = models.TextField()  
    timestamp = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f"{self.user.username}: {self.message[:50]}"
    class Meta:
        verbose_name = "Контент для секции"
        verbose_name_plural = "Контент для секций"
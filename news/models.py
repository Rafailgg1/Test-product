from django.db import models

class Articles(models.Model):
    title = models.CharField('Название Теста', max_length=50)
    anons = models.CharField('Тема Теста', max_length=250)
    full_text = models.TextField('Описание текста')
    date = models.DateTimeField('Дата публикации')
    
    def _str_(self):
        return self.title
    
    def get_absolute_url(self):
        return f'/news/{self.id}'
    
    
    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'
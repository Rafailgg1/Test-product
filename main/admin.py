from django.contrib import admin
from .models import Test, Question, Answer, Section


class TestAdmin(admin.ModelAdmin):
    list_display = ['title', 'description'] 
    
    
class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 3
    fields = ['text', 'is_correct', 'result_message', 'result_image', 'redirect_to']
    fk_name = 'question'  
    
class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]
    list_display = ['text', 'test', 'redirect_to']
    list_filter = ['test']
    search_fields = ['text']
    autocomplete_fields = ['redirect_to']

class SectionContentAdmin(admin.ModelAdmin):
    list_display = ['title', 'test', 'created_at']
    list_filter = ['test', 'created_at']
    search_fields = ['title', 'description', 'test__title']
    
class TestInline(admin.TabularInline):
    model = Test
    extra = 1

class SectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active']
    list_filter = ['is_active']
    search_fields = ['title', 'description']
    inlines = [TestInline]

admin.site.register(Section, SectionAdmin)
admin.site.register(Test, TestAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)



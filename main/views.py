from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpRequest, Http404, JsonResponse
from django.db import models
from rest_framework import viewsets
from django.shortcuts import render, redirect
from main.models import  Test, Question, Answer, Section
from rest_framework import serializers
from .serializers import TestSerializer
from django.urls import reverse
import logging
import time  
from .models import ChatMessage
from .forms import ChatMessageForm, TestForm
from django.contrib.auth.decorators import login_required


def views_test(request, test_id):
    test = get_object_or_404(Test, id=test_id)
    return render(request, 'main/test_template.html', {'test': test})

class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    
logger = logging.getLogger(__name__)

def section(request):
    active_sections = Section.objects.filter(is_active=True).prefetch_related('tests')
    return render(request, 'main/section.html', {'active_sections': active_sections})

def section_list(request):
    active_sections = Section.objects.filter(is_active=True)
    return render(request, 'main/section_list.html', {'active_sections': active_sections})

def section_detail(request, test_id):
    test = get_object_or_404(Test, id=test_id)
    first_question = test.questions.first()
    if not first_question:
        return render(request, 'main/section_detail.html', {
            'test': test,
            'error_message': 'В этом тесте пока нет вопросов.'
        })
    
    return render(request, 'main/section_detail.html', {
        'test': test,
        'first_question': first_question
    })

def start_test(request, test_id):
    test = get_object_or_404(Test, id=test_id)
    return render(request, 'main/test.html', {'test': test})

def create_test(request):
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('section')
    else:
        form = TestForm()
    return render(request, 'main/create_test.html', {'form': form})

def delete_test(request, test_id):
    test = get_object_or_404(Test, id=test_id)
    if request.method == 'POST':
        test.delete()
        return redirect('section')
    return render(request, 'main/confirm_delete.html', {'test': test})
def edit_test(request, test_id):
    test = get_object_or_404(Test, id=test_id)
    if request.method == 'POST':
        form = TestForm(request.POST, instance=test)
        if form.is_valid():
            form.save()
            return redirect('section')
    else:
        form = TestForm(instance=test)
    return render(request, 'main/edit_test.html', {'form': form})

def question(request, test_id, question_id):
    test = get_object_or_404(Test, id=test_id)
    current_question = get_object_or_404(Question, id=question_id)

    if request.method == 'POST':
        selected_answer_id = request.POST.get('answer')
        if selected_answer_id:
            answer = get_object_or_404(Answer, id=selected_answer_id)
            if answer.is_correct:
                request.session['score'] = request.session.get('score', 0) + 1


            if 'answers' not in request.session:
                request.session['answers'] = []
            request.session['answers'].append(selected_answer_id)
            request.session.modified = True


            if answer.result_message:
                request.session['result_message'] = answer.result_message
                request.session['result_image'] = answer.result_image.url if answer.result_image else None
                result_id = f"{test_id}_{int(time.time())}"
                return redirect('results', result_id=result_id)


            if answer.redirect_to:
                next_question = answer.redirect_to
                return redirect('question', test_id=test_id, question_id=next_question.id)


        result_id = f"{test_id}_{int(time.time())}"
        return redirect('results', result_id=result_id)

    return render(request, 'main/question.html', {
        'question': current_question,
        'test_id': test_id,
    })

    
def results(request, result_id):
    test_id = int(result_id.split('_')[0])
    test = get_object_or_404(Test, id=test_id)
    score = request.session.get('score', 0)
    total = test.questions.count()
    

    result_message = "Результат не определён."


    if test_id == 4:
        if 0 <= score <= 5:
            result_message = "Понятие времени вам даётся не легко, возможно оно от вас убежало."
        elif 6 <= score <= 9:
            result_message = "Почти идеально, Вы знаете о времени многое, но ваши часы отстают на секунды, это не критично."
        elif score == 10:
            result_message = "Ого, да вы эксперт в понятии времени. Неужели вы само время?"


    elif test_id == 5:
        if 0 <= score <= 5:
            result_message = "Вы только начинаете свой путь в этом мире. Продолжайте учиться, и познайте его!"
        elif 6 <= score <= 9:
            result_message = "Вы знаете о мире многое, но ещё есть куда расти!"
        elif score == 10:
            result_message = "Вы знаете о будущем больше многих, так держать."

    elif test_id == 6:
        if 0 <= score <= 2:
            result_message = "Материальный мир далёк, попробуйте пройти тест на воображение"
        elif 3 <= score <= 4:
            result_message = "Вы близки к разгадке материального мира!"
        elif score == 5:
            result_message = "Вы знайте о материальном мире всё!"
            
            
    elif test_id == 7:
        if 0 <= score <= 5:
            result_message = "У вас есть воображение, но вы стесняйтесь о нём рассказать."
        elif 6 <= score <= 9:
            result_message = "У вас богатое воображение, и вы его хорошо демонстрируете!"
        elif score == 10:
            result_message = "Воображение ваше второе имя, и я уверен вы можете соотварить всё!"
            

    else:
        result_message = request.session.get('result_message', result_message)

    result_image = None
    last_answer_id = request.session.get('answers', [])[-1] if request.session.get('answers') else None
    if last_answer_id:
        try:
            last_answer = Answer.objects.get(id=last_answer_id)
            result_image = last_answer.result_image.url if last_answer.result_image else None
        except Answer.DoesNotExist:
            pass

    request.session.flush()

    return render(request, 'main/results.html', {
        'score': score,
        'total': total,
        'result_message': result_message,
        'result_image': result_image, 
        'test_title': test.title,
    })
    
@login_required
def chat(request):
    if request.method == 'POST':
        form = ChatMessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.user = request.user
            message.save()
            return redirect('chat')
    else:
        form = ChatMessageForm()

    messages = ChatMessage.objects.all().order_by('timestamp')
    return render(request, 'main/chat.html', {'form': form, 'messages': messages})

a = []
def start_test(request, test_id):
    test = get_object_or_404(Test, id=test_id)
    first_question = test.questions.first()
    if not first_question:
        return render(request, 'main/no_questions.html')  
    return redirect('question', test_id=test.id, question_id=first_question.id)

def test_people(request):
    return start_test(request, test_id=3) 

def test_time(request):
    return start_test(request, test_id=4) 

def test_world(request):
    return start_test(request, test_id=5)  

def test_material(request):
    return start_test(request, test_id=6)  

def test_imagination(request):
    return start_test(request, test_id=7)  

def index(request):
    return render(request, 'main/index.html')

def themes(request):
    return render(request, 'main/themes.html')

def about(request):
    return render(request, 'main/about.html')

def log_in(request):
    return render(request, 'main/log_in.html')

def theme1(request):
    return render(request, 'main/theme1.html')

def theme2(request):
    return render(request, 'main/theme2.html')

def theme3(request):
    return render(request, 'main/theme3.html')

def test1(request):
    return render(request, 'main/test1.html')

def test2(request):
    return render(request, 'main/test2.html')

def test3(request):
    return render(request, 'main/test3.html')

def section(request):
    return render(request, 'main/section.html')

def info(request):
    return render(request, 'main/info.html')



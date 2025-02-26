from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import  DetailView, UpdateView, DeleteView

def test_home(request):
    news = Articles.objects.order_by('title')[:1]
    return render(request, 'news/test_home.html', {'news':news})

class TestDetailView(DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'

class TestUpdateView(UpdateView):
    model = Articles
    template_name = 'news/create.html'
    
    form_class = ArticlesForm
    
class TestDeleteView(DeleteView):
    model = Articles
    success_url = '/test'
    template_name = 'news/test-delete.html'
    
# def create(request):
#     return render(request, 'news/create.html')

def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'
            
    form = ArticlesForm()
    
    data = {
        'form': form,
        'error': error
    }
    
    return render(request, 'news/create.html', data)
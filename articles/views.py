from django.shortcuts import render, redirect
from .models import Articles, Comments
from .forms import ArticleForm, CommentForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    articles = Articles.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = ArticleForm()
    context = {
        'form': form
    }
    return render(request, 'articles/forms.html', context)

@login_required
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user == article.user:
        if request.method == 'POST':
            form = ArticleForm(request.POST, request.FILES, instance=article)
            if form.is_valid():
                form.save()
                return redirect('articles:index')
        else:
            form = ArticleForm(instance=article)
        context = {
            'form': form
        }
        return render(request, 'articles/forms.html', context)

@login_required
def delete(request, pk):
    Article.objects.get(pk=pk).delete()
    return redirect('articles:index')

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'aritcle': article
    }
    return render(request, 'articles/detail.html', context)

@login_required
def comments(request, article_pk):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            temp = form.save(commit=False)
            temp.user = request.user
            temp.save()
            return redirect('articles:detail', article_pk)

@login_required
def comments_delete(request, article_pk, pk):
    Comments.objects.get(pk=pk).delete()
    return redirect('articles:detail', article_pk)




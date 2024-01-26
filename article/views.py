from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, Tag, Comment, Category
from django.core.paginator import Paginator
from .form import CommentForm


def article_list_view(request):
    cat = request.GET.get('cat')
    tag = request.GET.get('tag')
    articles = Article.objects.order_by('-id')
    page = request.GET.get('page')
    paginator = Paginator(articles, 3)
    page_obj = paginator.get_page(page)
    if cat:
        page_obj = articles.filter(category__title__exact=cat)

    if tag:
        page_obj = articles.filter(tags__title__exact=tag)
    q = request.GET.get('q')
    if q:
        page_obj = Article.objects.filter(title__icontains=q).order_by('-id')
    ctx = {
        'object_list': page_obj,
    }
    return render(request, 'article/blog.html', ctx)


def article_detail_view(request, slug):
    article = get_object_or_404(Article, slug=slug)
    categories = Category.objects.all()
    tags = Tag.objects.all()
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.article = article
            obj.save()
            return redirect('.#comment-list')
    ctx = {
        'object': article,
        'categories': categories,
        'tags': tags,
        'form': form,
    }
    return render(request, 'article/blog-single.html', ctx)


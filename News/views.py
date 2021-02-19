from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from .forms import NewsForm
from .models import News


def index(request):
    news = News.objects.order_by('-datetime')

    news_per_page = request.GET.get('pageSize', 10)
    page_number = request.GET.get('page', 1)

    paginator = Paginator(news, news_per_page)
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()
    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''
    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    context = {
        'page': page,
        'is_paginated': is_paginated,
        'prev_url': prev_url,
        'next_url': next_url,
        'news_per_page': news_per_page
    }
    return render(request, 'News/index.html', context)


def about(request):
    return render(request, 'News/about.html')


def create_news(request):
    error = ''
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = NewsForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'News/create_news.html', context)

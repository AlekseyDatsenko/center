from random import randint
from django.core.paginator import Paginator
from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Video, About, News, Contacts, Image, Comments, Bible
from chat.forms import CommentForm, PostForm


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    paginator = Paginator(posts, 10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    count = Bible.objects.count()
    bible = Bible.objects.all()[randint(0, count - 1)]
    return render(request, 'chat/post_list.html', {'posts':posts, 'bible':bible})


def new_post(request):
    count = Bible.objects.count()
    bible = Bible.objects.all()[randint(0, count - 1)]
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.published_date = timezone.now()
            form.save()
            return redirect(post_list)
    else:
        form = PostForm()
    return render(request, "chat/new_post.html",
                  {'form': form, 'bible':bible})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    com = Comments.objects.filter(post=pk).order_by('-created')
    paginator = Paginator(com, 10)
    page = request.GET.get('page')
    com = paginator.get_page(page)
    count = Bible.objects.count()
    bible = Bible.objects.all()[randint(0, count - 1)]
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.post = post
            form.save()
            return redirect(post_detail, pk)
    else:
        form = CommentForm()
    return render(request, "chat/post_detail.html",
                  {'post': post, 'com': com, 'form': form, 'bible':bible})

def video(request):
    videos = Video.objects.all()
    paginator = Paginator(videos, 3)
    page = request.GET.get('page')
    videos = paginator.get_page(page)
    count = Bible.objects.count()
    bible = Bible.objects.all()[randint(0, count - 1)]
    return render(request, 'chat/video.html', {'videos': videos, 'bible':bible})

def about(request):
    about = About.objects.all()
    count = Bible.objects.count()
    bible = Bible.objects.all()[randint(0, count - 1)]
    return render(request, 'chat/about.html', {'about':about, 'bible':bible})

def news_list(request):
    news = News.objects.all().order_by('-created_date')
    paginator = Paginator(news, 10)
    page = request.GET.get('page')
    news = paginator.get_page(page)
    count = Bible.objects.count()
    bible = Bible.objects.all()[randint(0, count - 1)]
    return render(request, 'chat/news_list.html', {'news':news, 'bible':bible})

def news_detail(request, pk):
    new = get_object_or_404(News, pk=pk)
    count = Bible.objects.count()
    bible = Bible.objects.all()[randint(0, count - 1)]
    return render(request, 'chat/news_detail.html', {'new': new, 'bible':bible})

def contacts(request):
    contacts = Contacts.objects.all()
    count = Bible.objects.count()
    bible = Bible.objects.all()[randint(0, count - 1)]
    return render(request, 'chat/contacts.html', {'contacts':contacts, 'bible':bible})

def fotos(request):
    fotos = Image.objects.all()
    count = Bible.objects.count()
    bible = Bible.objects.all()[randint(0, count - 1)]
    return render(request, 'chat/foto.html', {'fotos':fotos, 'bible':bible})

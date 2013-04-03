from django.shortcuts import render_to_response, redirect
from django.contrib import messages
from models import Article, ArticleForm
from django.template import RequestContext
import datetime


def home(request):
    """
    Home page
    """
    # Order articles by latest date/time
    articles = Article.all().order('-created_on')

    return render_to_response('home.html',
                              RequestContext(request, dict(articles=articles)))

def create_article(request):
    """
    Admin home page for managing articles
    """
    # Order articles by latest date/time
    articles = Article.all().order('-created_on')

    # Initiatize form
    form = ArticleForm()

    if request.method == "POST":

        # Bind the data
        form = ArticleForm(request.POST)

        if form.is_valid():
            article = Article(title=form.cleaned_data['title'],
                              body=form.cleaned_data['body'],
                              created_by=form.cleaned_data['created_by'])
            article.put()
            messages.success(request, 'Article created successfully')
            return redirect('create_article')

    return render_to_response('create_article.html',
                              RequestContext(request, dict(articles=articles,
                                                           form=form)))

def update_article(request, article_id):
    """
    Update an article
    """
    # Get the article by the article id
    article = Article.get_by_id(int(article_id))

    # Order articles by latest date/time
    articles = Article.all().order('-created_on')

    # Initiatize form
    form = ArticleForm()

    if request.method == "POST":

        # Bind the data
        form = ArticleForm(request.POST)

        if form.is_valid():
            article.title = form.cleaned_data['title']
            article.created_by = form.cleaned_data['created_by']
            article.body = form.cleaned_data['body']
            article.put()
            messages.success(request, 'Article updated successfully')
            return redirect('create_article')

    return render_to_response('create_article.html',
                              RequestContext(request, dict(articles=articles,
                                                           article=article,
                                                           form_action="edit",
                                                           form=form)))

def read_article(request, article_id):
    """
    Read an article
    """
    # Get the article by the article id
    article = Article.get_by_id(int(article_id))

    return render_to_response('read_article.html', dict(article=article))

def delete_article(request, article_id):
    """
    Delete an article
    """
    # Get the article by the article id
    article = Article.get_by_id(int(article_id))
    article.delete()
    messages.success(request, 'Article deleted successfully')

    return redirect('create_article')

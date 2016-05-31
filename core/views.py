import logging

from django.views.generic import TemplateView
from django.conf import settings
from django.shortcuts import render_to_response, redirect
from django.contrib import messages
from models import Article, ArticleForm
import datetime


class HelloWorld(TemplateView):
    template_name = "hello-world.html"
    
    def get_context_data(self, **kwargs):
        context = super(HelloWorld, self).get_context_data(**kwargs)        
        self.request.session['test'] = 'Session is working'
        context['message'] = 'Hooray! Everything seems to work... - %s' % self.request.session['test']
        context['poll_id'] = kwargs['poll_id']
        return context

def home(request):
    articles = Article.all()

    return render_to_response('home.html', dict(articles=articles))


def create_article(request):

    articles = Article.all()

    if request.method == "POST":
        form = ArticleForm(request.POST)

        if form.is_valid():
            article = Article(title=form.cleaned_data['title'],
                              body=form.cleaned_data['body'])
            article.put()
            messages.success(request, 'Article created successful')
            return redirect('create_article')

    return render_to_response('create_article.html', dict(articles=articles))

def sample(request, poll_id):
    return render_to_response('index.html')

def update_article(request, article_id):

    article = Article.get_by_id(int(article_id))
    articles = Article.all()

    if request.method == "POST":
        form = ArticleForm(request.POST)

        if form.is_valid():
            article.title = form.cleaned_data['title']
            article.body = form.cleaned_data['body']
            article.put()
            messages.success(request, 'Article updated successfully')
            return redirect('create_article')

    return render_to_response('create_article.html', dict(articles=articles, article=article, form_action="edit"))

def read_article(request, article_id):

    article = Article.get_by_id(int(article_id))

    return render_to_response('read_article.html', dict(article=article))

def delete_article(request, article_id):

    article = Article.get_by_id(int(article_id))
    article.delete()
    messages.success(request, 'Article deleted successfully')

    return redirect('create_article')


def exception_test(request):
    logging.debug('Debug log')
    logging.warn('Warn log')
    logging.error('Error log')
    raise Exception()
from google.appengine.ext import db
from django import forms

class Article(db.Model):
    id = db.IntegerProperty(indexed=True)
    title = db.StringProperty(required=True)
    body = db.StringProperty(required=True, multiline=True)
    created_by = db.StringProperty(required=True)
    created_on = db.DateTimeProperty(auto_now_add=True)

    def __unicode__(self):
        return self.title

class ArticleForm(forms.Form):
    title = forms.CharField(max_length=100)
    body = forms.CharField(max_length=500)
    created_by = forms.CharField()

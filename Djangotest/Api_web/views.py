"""
author : xjz
date : 2021-04-20
"""

from django.http import HttpResponse
from . import models

# Create your views here.


def welcome(request):
    return HttpResponse("<h1>你好，欢迎来到Django！<h1>")


def article_content(request):
    article = models.Article.objects.all()[0]
    title = article.title
    brief_content = article.brief_content
    content = article.content
    article_id = article.article_id
    publish_date = article.publish_date
    return_str = 'title: %s, brief_content: %s, content: %s, article_id: %s, publish_date: %s' % (
        title,
        brief_content,
        content,
        article_id,
        publish_date
    )
    return HttpResponse(return_str)

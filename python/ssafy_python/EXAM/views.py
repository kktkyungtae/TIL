from django.shortcuts import render
from .models import Article

def index(request, context):
    a = Article.objects.all()
    return render(request, 'index.html',{'context' : context, 'a' :a})

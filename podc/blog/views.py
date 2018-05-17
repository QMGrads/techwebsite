from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .models import Article
from .forms import PostForm

def index(request):
    latest_article_list = Article.objects.order_by('-pub_date')[:5]
    template = loader.get_template('blog/index.html')
    context = {
        'latest_article_list': latest_article_list,
    }
    return HttpResponse(template.render(context, request))
	
def about(request):
	return render(request, 'blog/about.html')
	
def post_new(request):
    form = PostForm()
    return render(request, 'blog/articles.html', {'form': form})
	
def login_user(request):
  if request.method == 'POST':
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            print(user)
            login(request, user)
            return HttpResponseRedirect('/blog')
    else:
        print("user does not exist")
        return render(request, 'blog/Login.html')
  else:
    return render(request, 'blog/Login.html')

def article(request, article_id):
    article_detail = Article.objects.get(pk=article_id)
    template = loader.get_template('blog/article.html')
    context = {
        'article_detail': article_detail,
    }
    return HttpResponse(template.render(context, request))
	
def addarticle(request):
	form = PostForm(request.POST or None)
	if form.is_valid():
		form.save()
	context = {'form': form}
	return render(request, 'blog/addarticle.html', context)

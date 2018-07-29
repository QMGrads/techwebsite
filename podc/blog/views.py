from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Article
from .forms import PostForm

def index(request):
    latest_article_list = Article.objects.order_by('-pub_date')[:5]
    template = loader.get_template('blog/index.html')
    context = {
        'latest_article_list': latest_article_list,
    }
    return HttpResponse(template.render(context, request))

def morearticles(request):
    latest_article_list = Article.objects.order_by('-pub_date')
    template = loader.get_template('blog/morearticles.html')
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
            login(request, user)
            return HttpResponseRedirect('/blog')
    else:
        print("user does not exist")
        return render(request, 'blog/Login.html')
  else:
    return render(request, 'blog/Login.html')

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/blog')

def article(request, article_id):
    article_detail = Article.objects.get(pk=article_id)
    template = loader.get_template('blog/article.html')
    context = {
        'article_detail': article_detail,
    }
    return HttpResponse(template.render(context, request))
	
@login_required(login_url='login_user')
def addarticle(request):
	form = PostForm(request.POST, request.FILES)
	if form.is_valid():
		form.save()
		return HttpResponseRedirect('/blog')
	context = {'form': form}
	return render(request, 'blog/addarticle.html', context)

class editarticle(LoginRequiredMixin, UpdateView):
    model = Article
    fields = ('title', 'author', 'article_title', 'article_image')
    template_name = 'blog/addarticle.html'
    success_url = reverse_lazy('index')

@login_required(login_url='login_user')
def deletearticle(request, pk):
	article = get_object_or_404(Article, id=pk)
	article.delete()
	return HttpResponseRedirect('/blog')
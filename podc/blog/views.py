from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

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
	
def login(request):
	""""
	context = RequestContext(request)
    if request.method == 'POST':
          username = request.POST['username']
          password = request.POST['password']
          user = authenticate(username=username, password=password)
          if user is not None:
              if user.is_active:
                  login(request, user)
                  # Redirect to index page.
                  return HttpResponseRedirect("blog/index.html")
              else:
                  # Return a 'disabled account' error message
                  return HttpResponse("You're account is disabled.")
          else:
              # Return an 'invalid login' error message.
              print  "invalid login details " + username + " " + password
              return render_to_response('login.html', {}, context)
    else:
        # the login is a  GET request, so just show the user the login form.
        return render_to_response('login.html', {}, context)
		"""
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

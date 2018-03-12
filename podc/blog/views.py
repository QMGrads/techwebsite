from django.http import HttpResponse
from django.template import loader

from .models import Article

def index(request):
    latest_article_list = Article.objects.order_by('-pub_date')[:5]
    template = loader.get_template('blog/index.html')
    context = {
        'latest_article_list': latest_article_list,
    }
    return HttpResponse(template.render(context, request))
	
def about(request):
	template = loader.get_template('blog/about.html')
	return HttpResponse(template.render(request))
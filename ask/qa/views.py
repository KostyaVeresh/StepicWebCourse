from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseBadRequest 
from django.core.paginator import Paginator
from models import Question, Answer
from django.http import Http404

def test(request, *args, **kwargs):
    return HttpResponse('OK')
	
def mainPage(request):
	questions = Question.objects.all()
	questions = questions.order_by('-id')
	try:
		page = int(request.GET.get('page', 1))
	except ValueError:
		raise Http404
	paginator = Paginator(questions, 10)
	paginator.baseurl = '/?page='
	try:
		page = paginator.page(page)
	except EmptyPage:
		page = paginator.page(paginator.num_pages)
	return render(request, 'index.html', {
		'questions': page.object_list,
		'paginator': paginator,
		'page': page,
	})	
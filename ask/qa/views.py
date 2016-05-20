from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseBadRequest 
from django.core.paginator import Paginator
from models import Question, Answer
from django.http import Http404

def test(request, *args, **kwargs):
    return HttpResponse('OK')
	
def mainPage(request, ord='-id', baseurl='/?page='):
	questions = Question.objects.all()
	questions = questions.order_by(ord)
	try:
		page = int(request.GET.get('page', 1))
	except ValueError:
		raise Http404
	paginator = Paginator(questions, 10)
	paginator.baseurl = baseurl
	try:
		page = paginator.page(page)
	except EmptyPage:
		page = paginator.page(paginator.num_pages)
	return render(request, 'index.html', {
		'questions': page.object_list,
		'paginator': paginator,
		'page': page,
	})
	
def popularPage(request):
	return mainPage(request, '-rating',  '/popular/?page=')
	
def questionPage(request, id):
	try:
		quest = Question.objects.get(id = id)
	except Question.DoesNotExist:
		raise Http404
	answers = Answer.objects.filter(question_id=id)
	return render(request, 'question.html', {
		'question': quest,
		'answers': answers
	})
	#return HttpResponse('OK')
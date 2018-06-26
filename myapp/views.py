from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from .forms import AutherForm,ResearchForm
from .models import Author,Research
from django.shortcuts import render
from django.db.models import Q

def home(request):
	return render(request,'home.html')

def listAuthor(request):
	queryset = Author.objects.all()

	query = request.GET.get('q')
	if query:
		queryset = queryset.get(id=query)

	context = {
		'object_list':queryset,
	}
	return render(request, 'author.html',context)


def listResearch(request):
	queryset = Research.objects.all()

	query = request.GET.get('q')
	if query:
		queryset = queryset.filter(
			Q(name__icontains = query) | 
			Q(abstract__icontains = query) | 
			Q(etc__icontains = query)
			).distinct()

	context = {
		'object_list':queryset,
	}
	return render(request, 'home.html',context)


# def home(request):
# 	return render(request, 'home.html', {'key': "value" })

# class CreatePersonView(CreateView):
# 	queryset = Person()
# 	template_name='person.html'
# 	form_class = PersonForm
# 	success_url = '/'

# class UpdatePersonView(UpdateView):
# 	queryset = Person.objects.all()
# 	template_name='person.html'
# 	form_class = PersonForm
# 	success_url = '/'

# class ListPersonView(ListView):
#     model = Person
#     template_name='person_list.html'


# class Home2(ListView):
#     model = Person
#     template_name='home.html'

       
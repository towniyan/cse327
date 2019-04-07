from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Page
from onwebed import core

# Create your views here.

def index(request):
	return render(request, "pages/index.html")


def list(request):
	context = {
		'pages': Page.objects.all()
	}

	return render(request, "pages/list.html", context)


def create(request):
	if request.method == "POST":
		title = request.POST['title']
		name = request.POST['name']

		Page.objects.create(title = title, name = name)

		messages.success(request, 'Page created successfully!')

		return redirect("pages:list")

	return render(request, "pages/create.html")


def delete(request, page_id):
	if request.method == "POST":
		page = get_object_or_404(Page, pk = page_id)
		page.delete()

		messages.success(request, 'Page deleted successfully!')
		return redirect("pages:list")

	context = {
		'page': get_object_or_404(Page, pk = page_id)
	}

	return render(request, "pages/delete.html", context)
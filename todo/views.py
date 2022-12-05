from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from .forms import UserRegistrationForm, TodoForm, LinkForm
from .models import TodoItem, LinkItem


@login_required
def home(request):
    """
    Create todo item and view other todo items as well.
    """
    if request.method == 'POST':
        todo_name = request.POST.get("new-todo")
        duedate = request.POST.get("new-duedate")
        todo = TodoItem.objects.create(name=todo_name, duedate=duedate, user=request.user)
        return redirect("home")

    # todo items
    todos = TodoItem.objects.filter(user=request.user, is_completed=False).order_by("duedate")

    # pagination 4 items per page
    paginator = Paginator(todos, 4)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {"todos": todos, "page_obj": page_obj}

    # NOTE: Need to change the html file to todo_app.html for displaying the todo's
    return render(request, "todo/todo_app.html", context)


def hub(request):
    """
    Create todo item and view other todo items as well.
    """
    if request.method == 'POST':
        link_name = request.POST.get("new-link")
        link_url = request.POST.get("new-url")
        link = LinkItem.objects.create(name=link_name, url=link_url, user=request.user)
        return redirect("hub")

    # todo items
    links = LinkItem.objects.filter(user=request.user).order_by("-id")

    # pagination 4 items per page
    paginator = Paginator(links, 4)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {"links": links, "page_obj": page_obj}

    # NOTE: Need to change the html file to todo_app.html for displaying the todo's
    return render(request, "todo/link_app.html", context)

def register(request):
    """
    User Registration form
    Args:
        request (POST): New user registered
    """    
    form = UserRegistrationForm()
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserRegistrationForm()

    context = {"form": form}
    return render(request, "todo/register.html", context)


def logout_user(request):
    logout(request)
    return redirect("login")
    

def update_todo(request, pk):
    """
    Update todo item
    Args:
        pk (Integer): Todo ID - primary key
    """
    # NOTE: below get_object_or_404() returns a data if exists else status 404 not found
    todo = get_object_or_404(TodoItem, id=pk, user=request.user)

    # NOTE: request.POST.get("todo_{pk}") is the input name of the todo modal
    todo.name = request.POST.get(f"todo_{pk}")
    todo.duedate = request.POST.get(f"duedate_{pk}")
    todo.save()
    # return redirect("home")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def complete_todo(request, pk):
    """
    Updating todo as completed item
    Args:
        pk (Integer): Todo ID - primary key
    """    
    todo = get_object_or_404(TodoItem, id=pk, user=request.user)
    todo.is_completed = True
    todo.save()
    # return redirect("home")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def delete_todo(request, pk):
    """
    Delete todo item
    Args:
        pk (Integer): Todo ID - Primary key
    """    
    todo = get_object_or_404(TodoItem, id=pk, user=request.user)
    todo.delete()
    # return redirect("home")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def update_link(request, pk):
    """
    Update todo item
    Args:
        pk (Integer): Todo ID - primary key
    """
    # NOTE: below get_object_or_404() returns a data if exists else status 404 not found
    link = get_object_or_404(LinkItem, id=pk, user=request.user)

    # NOTE: request.POST.get("todo_{pk}") is the input name of the todo modal
    link.name = request.POST.get(f"link_{pk}")
    link.url = request.POST.get(f"url_{pk}")
    link.save()
    # return redirect("home")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def complete_link(request, pk):
    """
    Updating todo as completed item
    Args:
        pk (Integer): Todo ID - primary key
    """    
    link = get_object_or_404(LinkItem, id=pk, user=request.user)
    link.is_completed = True
    link.save()
    # return redirect("home")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def delete_link(request, pk):
    """
    Delete todo item
    Args:
        pk (Integer): Todo ID - Primary key
    """    
    link = get_object_or_404(LinkItem, id=pk, user=request.user)
    link.delete()
    # return redirect("home")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
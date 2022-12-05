from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import (home, hub, register, logout_user, update_todo, complete_todo,
    delete_todo, update_link, complete_link, delete_link)


urlpatterns = [
    path("", home, name="home"),
    path("hub/", hub, name="hub"),
    path("login/", LoginView.as_view(template_name="todo/login.html"),
        name="login"),
    path("logout/", LogoutView.as_view(template_name="todo/logout.html"),
        name="logout"),
    path("register/", register, name="register"),
    path("update/todo/<int:pk>/", update_todo, name="update_todo"),
    path("complete/todo/<int:pk>/", complete_todo, name="complete_todo"),
    path("delete/todo/<int:pk>/", delete_todo, name="delete_todo"),
    path("update/link/<int:pk>/", update_link, name="update_link"),
    path("complete/link/<int:pk>/", complete_link, name="complete_link"),
    path("delete/link/<int:pk>/", delete_link, name="delete_link"),
]
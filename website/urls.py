from django.urls import path
from . import views

app_name = "website"
urlpatterns = [
    # ex. /
    path("", views.index, name='index'),
    # ex. /hr7397-115
    path("<str:bill_slug>", views.bill_details, name="bill_details"),
    # ex. /login
    path("login", views.login_user, name='login'),
    # ex. /logout
    path("logout", views.user_logout, name='logout'),
    # ex. /register
    path("register", views.register, name='register'),
]
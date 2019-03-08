from django.urls import path
from . import views

app_name = "website"
urlpatterns = [
    # ex. /login
    path("login", views.login_user, name='login'),
    # ex. /logout
    path("logout", views.user_logout, name='logout'),
    # ex. /register
    path("register", views.register, name='register'),
    # ex. /
    path("", views.index, name='index'),
    # ex. bill/hr7397
    path("bill/<str:bill_slug>", views.bill_details, name="bill_details"),
    # ex. bill/hr7397/save
    path("bill/<str:bill_slug>/save", views.save_bill, name="save_bill"),
    # ex. bill/hr7397/edit
    path("bill/<str:bill_slug>/edit", views.edit_saved_bill, name="edit_saved_bill"),
    # ex. bill/hr7397/delete
    path("bill/<str:bill_slug>/delete", views.delete_bill, name="delete_bill"),
    # ex. /saved
    path("saved", views.list_saved_bills, name="list_saved_bills"),

]
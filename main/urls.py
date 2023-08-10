from django.urls import path
from main.views import main_page, edit_page

urlpatterns = [
    path('', main_page, name="main"),
    path('edit/', edit_page, name="edit")
]
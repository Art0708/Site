from django.contrib import admin
from django.urls import path, include, re_path
from . import views

"""Список сылок приложения note_app"""
app_name = "note_app"
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name= "index"),
    path("topics/", views.topics, name= "topics"),
    path("programers/", views.programers, name= "programers"),
    path("spravka/", views.spravka, name= "spravka"),
    path(r'^topics/<int:topic_id>/', views.topic, name='topic'),
    path(r"^new_topic/$", views.new_topic, name="new_topic"),
    path(r'^new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    path(r'^edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry')
]

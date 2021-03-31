from django.urls import path
from . import views

app_name = 'learningLogs'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('topics/', views.topics, name = 'topics'),
    path('topics/<int:topic_id>/topic/', views.topic, name = 'topic'),
]

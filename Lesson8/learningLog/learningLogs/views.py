from django.shortcuts import render
from .models import Topic

def index(request):
        return render(request, 'learningLogs/index.html')

def topics(request):
    topics = Topic.objects.order_by('dateAdded')
    context = {'topics' : topics}
    return render (request, 'learningLogs/topics.html', context)


'''
 It will request information from the model you created before and pass it to a template
 As you can see, we created a function (def) called post_list that takes request 
 and will return the value it gets from calling another function render 
 that will render (put together) our template blog/post_list.html

'''
from django.shortcuts import render
from .models import Post
from django.utils import timezone

def post_list(request):
    posts = Post.objects.filter(publication_date__lte=timezone.now()).order_by('publication_date')
    return render(request, 'blogApp/post_list.html', {'posts': posts})

# Create your views here.

from django.shortcuts import render, redirect
from .models import PostModel, CommentsModel
from .forms import PostForm, CommentsForm
# Create your views here.

def home(request):
    posts = PostModel.objects.all()
    return render(request, 'home.html', {'posts':posts})

def create_post(request):
    form = PostForm(request.POST or None)
    if request.method == 'POST':
        print(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')
    return render(request, 'createPost.html', {'form': form})

def post(request, id):
    post = PostModel.objects.get(id=id)
    comments = CommentsModel.objects.all()
    if request.method == 'POST':
        form = CommentsForm(request.POST)
        if form.is_valid():
            form.errors.clear()
            form.save()
            # return redirect('post', id=id)
    form = CommentsForm({'post':post})      
    return render(request, 'post.html', {'post':post, 'comments':comments, 'form':form})

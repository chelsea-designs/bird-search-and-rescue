from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib import messages
from .forms import NewsPostForm
from .models import NewsPost

# Create your views here.
User = get_user_model()


def news(request):
    '''
    View to display news post page
    '''
    posts = NewsPost.objects.all().order_by('-created_on')
    context = {
        'posts': posts
    }
    return render(request, 'news/news.html', context)


def newsPostDetail(request, slug):
    '''
    View to return individual news post
    '''
    post = get_object_or_404(NewsPost, slug=slug)
    context = {
        'post': post,
    }
    return render(request, 'news/news_post_detail.html', context)


@login_required
def addNewsPost(request):
    '''
    View to handle displaying add news form
    and to handle form processing
    '''
    form = NewsPostForm()
    context = {
        'form': form,
    }
    if request.method == 'POST':
        form = NewsPostForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            messages.success(request, 'News Post successfully added!')
            return redirect('news')
        else:
            messages.error(
                request,
                'Failed to add the news post, \
                    please ensure the form is correctly filled in'
                )
    return render(request, 'news/news_post_form.html', context)


@login_required
def editNewsPost(request, slug):
    '''
    View to display prefilled form to edit a news post
    and to handle form processing
    '''
    post = get_object_or_404(NewsPost, slug=slug)
    form = NewsPostForm(instance=post)
    if request.method == 'POST':
        form = NewsPostForm(request.POST, request.FILES or None, instance=post)
        if form.is_valid():
            edited_form = form.save(commit=False)
            edited_form.author = request.user
            edited_form.save()
            messages.success(request, 'News Post successfully updated!')
            return redirect('news')
        else:
            messages.error(request, 'Failed to update news post, \
                please double check the form.')

    context = {
        'form': form,
        'post': post
    }

    return render(request, 'news/news_post_form.html', context)


@login_required
def deleteNewsPost(request, pk):
    '''
    View to handle the deletion of a news post
    '''
    post = get_object_or_404(NewsPost, pk=pk)
    if request.user.is_authenticated:
        post.delete()
        messages.success(request, 'The post has been deleted.')
        return redirect('news')
    else:
        messages.error(request, 'Only employees can delete news posts.')

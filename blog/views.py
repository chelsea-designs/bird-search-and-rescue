from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib import messages
from .forms import BlogPostForm
from .models import BlogPost

# Create your views here.
User = get_user_model()


def blog(request):
    '''
    View to display blog post page
    '''
    posts = BlogPost.objects.all().order_by('-created_on')
    context = {
        'posts': posts
    }
    return render(request, 'blog/blog.html', context)


def blogPostDetail(request, slug):
    '''
    View to return individual blog post
    '''
    post = get_object_or_404(BlogPost, slug=slug)
    context = {
        'post': post,
    }
    return render(request, 'blog/blog_post_detail.html', context)


@login_required
def addBlogPost(request):
    '''
    View to handle displaying add blog form
    and to handle form processing
    '''
    form = BlogPostForm()
    context = {
        'form': form,
    }
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            messages.success(request, 'Blog Post successfully added!')
            return redirect('blog')
        else:
            messages.error(
                request,
                'Failed to add the blog post, \
                    please ensure the form is correctly filled in'
                )
    return render(request, 'blog/blog_post_form.html', context)


@login_required
def editBlogPost(request, slug):
    '''
    View to display prefilled form to edit a blog post
    and to handle form processing
    '''
    post = get_object_or_404(BlogPost, slug=slug)
    form = BlogPostForm(instance=post)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES or None, instance=post)
        if form.is_valid():
            edited_form = form.save(commit=False)
            edited_form.author = request.user
            edited_form.save()
            messages.success(request, 'Blog Post successfully updated!')
            return redirect('blog')
        else:
            messages.error(request, 'Failed to update blog post, \
                please double check the form.')

    context = {
        'form': form,
        'post': post
    }

    return render(request, 'blog/blog_post_form.html', context)


@login_required
def deleteBlogPost(request, pk):
    '''
    View to handle the deletion of a blog post
    '''
    post = get_object_or_404(BlogPost, pk=pk)
    if request.user.is_authenticated:
        post.delete()
        messages.success(request, 'The post has been deleted.')
        return redirect('blog')
    else:
        messages.error(request, 'Only employees can delete blog posts.')
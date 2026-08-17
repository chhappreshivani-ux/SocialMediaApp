from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import PostForm
from .models import Post, Like, Comment


@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()

            return redirect("/home/")

    else:
        form = PostForm()

    return render(request, "posts/create_post.html", {"form": form})


@login_required
def all_posts(request):
    posts = Post.objects.all().order_by("-created_at")

    return render(request, "posts/all_posts.html", {
        "posts": posts
    })


@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    like, created = Like.objects.get_or_create(
        user=request.user,
        post=post
    )

    if not created:
        like.delete()

    return redirect("/posts/")


@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == "POST":
        text = request.POST.get("comment", "").strip()

        if text:
            Comment.objects.create(
                user=request.user,
                post=post,
                comment=text
            )

    return redirect("/posts/")

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if post.user == request.user:
        post.delete()

    return redirect("/posts/")

@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if comment.user == request.user:
        comment.delete()

    return redirect("/posts/")
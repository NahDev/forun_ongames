from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import PostForm, CommentForm
from .models import Post, Category, Comment



@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('forum_app:post_list')  # Redirecionar para a página post_list.html
    else:
        form = PostForm()
    return render(request, "create_post.html", {"form": form})

def post_list(request):
    posts = Post.objects.order_by('-created_at')
    categories = Category.objects.all()
    return render(request, "post_list.html", {"posts": posts, "categories": categories})

def post_list_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    posts = Post.objects.filter(category=category)
    return render(request, "post_list.html", {"posts": posts, "category": category})


@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post=post)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            if request.user.is_authenticated:
                comment.user = request.user
            else:
                comment.user = None  # Ou defina algum valor padrão para o usuário anônimo
            comment.save()
            return render(request, 'post_detail.html', {'post': post, 'comments': comments, 'form': form})
    else:
        form = CommentForm()
    
    return render(request, 'post_detail.html', {'post': post, 'comments': comments, 'form': form})
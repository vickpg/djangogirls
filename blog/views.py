from django.shortcuts import render
from .models import Post

# função de solicitação e que irá retornar valor que recebe ao chamar outra função render (renderizar) modelo blog 
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

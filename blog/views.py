from django.shortcuts import render

# função de solicitação e que irá retornar valor que recebe ao chamar outra função render (renderizar) modelo blog 
def post_list(request):
    return render(request, 'blog/post_list.html', {})

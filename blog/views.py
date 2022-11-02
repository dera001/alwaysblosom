from django.core.mail import send_mail,BadHeaderError
from django.views import generic
from .models import Post
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm

def home(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject,message,email, ['deramobilelegacy@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid Header Found!')
            return redirect('home')
    return render(request, 'index.html',{'form':form})
class PostList(generic.ListView):
    queryset = Post.objects.filter(status = 1).order_by("-created_on")
    template_name = "blog.html"

class PostDetail(generic.DetailView):
    model = Post
    template_name = "post_detail.html"

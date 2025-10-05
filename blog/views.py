from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
import logging
from . models import Post
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from . form import contactForm
# Create your views here.
#static demo data
#posts = [
#       {'id':1,'title': 'Post 1', 'content': 'Content of Post:1'},
#        {'id':2,'title': 'Post 2', 'content': 'Content of Post:2'},
#        {'id':3,'title': 'Post 3', 'content': 'Content of Post:3'},
#        {'id':4,'title': 'Post 4', 'content': 'Content of Post:4'},
#        ]'''
def index(request):
    blog_tittle="Lasted posts"
    #getting data from model
    all_posts=Post.objects.all()
    #pagination
    paginator=Paginator(all_posts,5)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    return render(request,'blog/index.html',{'blog_tittle':blog_tittle,'page_obj':page_obj})
def detail(request,slug):
    #static data
    #post = next((item for item in posts if item['id'] == int(post_id)), None)
    try:
    #getting data from model post id
        post=Post.objects.get(slug=slug)
        related_posts = Post.objects.filter(category=post.category).exclude(pk=post.id)
    except Post.DoesNotExist:
        raise Http404("Posts Does not Exists!")
    #logger = logging.getLogger("TESTING")
    #logger.debug(f'post variable is {post}')
    return render(request,'blog/detail.html',{'post':post,"related_posts":related_posts})
def old_url_redirect(request):
    return  redirect(reverse('blog:new_page_urla'))
def new_url_view(request):
    return HttpResponse("This is the new url")
def contact_view(request):
    logger = logging.getLogger(__name__)
    if request.method=="POST":
        form= contactForm(request.POST)
        name = request.POST.get('name')
        email = request.POST.get('email')       
        message = request.POST.get('message')
        logger = logging.getLogger("TESTING")
        if form.is_valid():
            logger.debug(f'post variable is {form.cleaned_data['name']} {form.cleaned_data['email']} {form.cleaned_data['message']}')
            success_message = "Thank you for your message!" 
            #send email or database save       
        else:
            logger.debug("Form is not valid")
        return render(request,'blog/contact.html',{'form':form,'name':name,'email':email,'message':message})
    return render(request, 'blog/contact.html')
def about_view(request):
    return render(request, 'blog/about.html')
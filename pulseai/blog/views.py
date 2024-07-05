from django.shortcuts import render,HttpResponse,get_object_or_404,redirect
from blog.models import Blog,BlogCategory,Comment

# Create your views here.
def index(request):
    # return HttpResponse("Hello World!!!")
    return render(request, 'blog/index.html')

def about(request):
    return render(request,'blog/about.html')

def contact(request):

    mobile = 7681049268
    email = "manoharss0407@gmail.com"
    a = 10
    b = 10
    languages = ['C','Java','Python','C++']
    blog={
        "title":"Blog Title",
        "author":"Manohar",
        "content":"Blog details"
    }
    students = [
        {"roll":1, "name":"Smith" , "cgpa":8.9},
        {"roll":2, "name":"Smith" , "cgpa":8.9},
        {"roll":3, "name":"Smith" , "cgpa":8.9},
        {"roll":4, "name":"Smith" , "cgpa":8.9},
        {"roll":5, "name":"Smith" , "cgpa":8.9},
    ]
    context = {
        "mob":mobile,
        "email":email,
        "a" : a,
        "b" : b,
        "languages":languages,
        'blog':blog,
        'students':students,
    }
    return render(request,'blog/contact.html',context)


def all_blogs(request,cid=0):
    # blogs = Blog.objects.all()
    if cid == 0:
        blogs = Blog.objects.filter(publish=True).order_by('-updated_at')
    else:
        blogs = Blog.objects.filter(publish=True,category=cid).order_by('-updated_at')
    categories = Blog.objects.all().order_by('category')
    context = {
        'blogs' : blogs,
        'categories':categories
    }

    return render(request,'blog/blog.html',context)

def blog_details(request,bid):
    # blog = Blog.objects.get(id=bid) gives individual items
    blog = get_object_or_404(Blog , pk=bid)
    comment = Comment.objects.filter(blog=blog).order_by("-created_at")
    context = {
        'blog':blog,
        'comment':comment
    }

    return render(request,'blog/details.html',context)  


def comment(request):
    if request.method == 'POST':
        user = request.user
        blog_id = request.POST.get('bid')
        comment = request.POST.get('comment')

        blog = Blog.objects.get(id=blog_id)

        comment = Comment(user=user,blog=blog, comment=comment)
        comment.save()
        return redirect('/blog/'+blog_id)
from django.shortcuts import render,HttpResponse

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
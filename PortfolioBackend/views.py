from django.shortcuts import render
from portfolioApi.models import Blogs,Skills
from django.core.paginator import Paginator

def blogs(request):
    articles = Blogs.objects.all().order_by('-createdAt')  # optional ordering
    paginator = Paginator(articles, 5)  # show 5 posts per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    skills = Skills.objects.all()

    data = {
        "articles": page_obj,
        "page_obj": page_obj,
        "tags":skills
    }

    return render(request, 'Blogs/blogs.html',data)

def blogByTag(request,tagName):
    print(tagName)
    skill = Skills.objects.filter(name=tagName).first()
    print(skill)
    blogs = skill.skillBlog.all().order_by('-createdAt')

    paginator = Paginator(blogs, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    skills = Skills.objects.all()

    data = {
        "articles": page_obj,
        "page_obj": page_obj,
        "tags":skills
    }
    return render(request, 'Blogs/blogs.html',data)

def blogDetail(request,titleSlug):
    articles = Blogs.objects.all().order_by('-createdAt')[0:5]
    blog = Blogs.objects.get(slug=titleSlug)
    return render(request,'Blogs/blogsDetails.html',{'blog':blog,"articles":articles})
    
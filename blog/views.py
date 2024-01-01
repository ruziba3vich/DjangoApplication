from django.shortcuts import render

posts = [
    {
        'author': 'PRODONiK',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'jan 1, 2024'
    },
    {
        'author': 'Alisher',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'jan 3, 2024'
    }
]

def home(request):
    
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

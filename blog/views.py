from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


posts = [
    {
    'author':'Nawed Arshad',
    'title':'My first Blog',
    'content':'jsncjd cniajdia jdiajdi oamda ncf ojdn vjnsfoas cfo iae jmdolajwmd',
    'date':'10 Aug 2024'
    },
    {
    'author':'Arshad',
    'title':'My first Blog',
    'content':'amda ncf ojdn vjnsfoas cfo iae jmdolajwmd',
    'date':'12 Aug 2024'
    }
]
def home(request):
    context = {
        'posts':posts,
    }
    return render(request, 'Blog/home.html', context)

def about(request):
    return render(request, 'Blog/about.html')


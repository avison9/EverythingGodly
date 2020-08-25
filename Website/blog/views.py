from django.shortcuts import render
from .models import post

# !-- database dummy data
# db = [
# {
# 'author':'Ayobami Abraham',
# 'date':'April 2, 2020',
# 'content':'Wecome to my first post. i will be giving you heavenly minded contents',
# 'title':'My First Post'
# },
# {
# 'author':'Tumi Adepoju',
# 'date':'April 9, 2020',
# 'content':'Wecome to my first post. my name is Tumi, a co founder of this blog',
# 'title':'My Welcome message'
# },
# {
# 'author':'Ayobami Abraham',
# 'date':'April 14, 2020',
# 'content':'Wecome to my Second post. Hope you were all blessed with my first post',
# 'title':'My Second Post'
# }

# ]


def home(request):
	content = {'database': post.objects.all(), 'tag':'Welcome!'}
	return render(request,'blog/home.html',content)

def about(request):
	content = {'tag':'About-Us'}
	return render(request,'blog/about.html',content)

from django.shortcuts import render

from datetime import date

all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "Beep Beep - Mountains.png",
        "author": "D me",
        "date": date(2021, 7, 21),
        "title": "Mountain Hiking",
        "excerpt": ".. only text .. only text .. only text .. only text .. only text...", 
        "content": """
        Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
        Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
        when an unknown printer took a galley of type and scrambled it to make a type specimen book.

        Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
        Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
        when an unknown printer took a galley of type and scrambled it to make a type specimen book.

        Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
        Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
        when an unknown printer took a galley of type and scrambled it to make a type specimen book.
        """
    },
    {
        "slug": "hike-in-the-mountains",
        "image": "Fitz - Morning Routine.png",
        "author": "Dd me",
        "date": date(2020, 5, 19),
        "title": "Sea Swimming",
        "excerpt": ".............some text some text some text ", 
        "content": """
        Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
        Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
        when an unknown printer took a galley of type and scrambled it to make a type specimen book.

        Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
        Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
        when an unknown printer took a galley of type and scrambled it to make a type specimen book.

        Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
        Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
        when an unknown printer took a galley of type and scrambled it to make a type specimen book.
        """
    },
    {
        "slug": "hike-in-the-mountains",
        "image": "People of Brooklyn - Nature.png",
        "author": "Ddd me",
        "date": date(2012, 2, 22),
        "title": "Forest walking",
        "excerpt": ",,,,,,some text some,,,,,,,,,,  ", 
        "content": """
        Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
        Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
        when an unknown printer took a galley of type and scrambled it to make a type specimen book.

        Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
        Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
        when an unknown printer took a galley of type and scrambled it to make a type specimen book.

        Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
        Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
        when an unknown printer took a galley of type and scrambled it to make a type specimen book.
        """
    },
]

#temparally function for dummmy data
def get_date(post):
    return post["date"]
    

# Create your views here.

def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", { "posts": latest_posts })


def posts(request):
    return render(request, "blog/all-posts.html")


def post_detail(request, slug):
    return render(request, "blog/post-detail.html")
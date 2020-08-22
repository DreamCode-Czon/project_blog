from django.shortcuts import render

posts = [
    {
        "author": "dreamCode",
        "title": "dream Big",
        "content": "dream True",
        "date_posted": "Sep 16,2020",
    },
    {
        "author": "dreamCode",
        "title": "dream Big",
        "content": "dream True",
        "date_posted": "Sep 16,2020",
    },
]


def home(request):
    context = {"posts": posts}

    return render(request, "blog/index.html", context)


def about(request):

    context = {"variable": posts}

    return render(request, "blog/about.html", context)

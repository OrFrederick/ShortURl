from django.shortcuts import render, redirect
from .forms import UrlForm
from .models import Url
import random
import string
# Create your views here.
def urls_view(request):
    
    context = {}

    if request.method == 'POST':
        form = UrlForm(request.POST)
        if form.is_valid():
            user = request.user
            url_link = request.POST.get('url')
            if ":" not in url_link:
                url_link = "http://"+url_link
            url_code = get_url_code()
            url = Url(url=url_link,url_code=url_code)
            url.save()
            context['code'] = url_code
            context['old_url'] = url_link
            
    return render(request,"home.html", context = context)

def get_url_code():
    unique = False
    while not unique:
        code = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=6))
        try:
            urls = Url.objects.get(url_code=code)
            unique = False
        except:
            unique = True
    return code

def redirect_view(request,url_code):
    url = Url.objects.get(url_code=url_code)
    url = url.url 
    return redirect(url)
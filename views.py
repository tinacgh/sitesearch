# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Site

@login_required
def showform(request):
    sites = Site.objects.all().order_by('tag')
    return render(request, 'sitesearch/main.html', {'sites': sites})

@login_required
def add(request):
    if request.method == 'POST':
        req_tag = request.POST.get('tag', '')
        req_url = request.POST.get('url', '')

        newsite = Site(tag=req_tag, url=req_url)
        newsite.save()

    return HttpResponseRedirect('/sitesearch/')

def delete(request, site_id):
    site = get_object_or_404(Site, pk=site_id)
    site.delete()
    return HttpResponseRedirect('/sitesearch/')

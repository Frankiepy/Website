from django.shortcuts import render, redirect
from .models import Match
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms

def match(request):
    matches = Match.objects.all().order_by('date')
    return render(request, 'match/match.html', { 'matches': matches })

def match_detail(request, slug):
    match = Match.objects.get(slug=slug)
    return render(request, 'match/match_detail.html', { 'match': match })

@login_required(login_url="/accounts/login/")
def profile_create(request):
    if request.method == 'POST':
        form = forms.CreatePost(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect("match:list")
    else:
        form = forms.CreatePost()
    return render(request, 'match/profile_create.html', { 'form':form })
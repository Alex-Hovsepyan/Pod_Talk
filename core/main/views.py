from django.shortcuts import render, redirect
from .models import Header
from .models import Title
from .models import ContactGet
from .models import ContactPost
from .forms import ContactModelForm
from .models import Footer
from .models import About
from .models import About_Content
from .models import LastestEpisode
from .models import TrendingEpisode
from .models import Topic
from .models import Specialist
from .models import DetailContent
from .models import Subscribe
from .forms import SubscribeModelForm


# Create your views here.

def index(request):
    contact_info_get = ContactGet.objects.all()[0]
    header_info = Header.objects.all()[0]
    title_info = Title.objects.all()[0]
    footer_info = Footer.objects.all()[0]
    latest_episodes = LastestEpisode.objects.all()
    trending_episodes = TrendingEpisode.objects.all()
    topic_content = Topic.objects.all()
    specialist_content = Specialist.objects.all()
    if request.method == 'POST':
        form = SubscribeModelForm(request.POST)
        if form.is_valid():
            Subscribe.objects.create(**form.cleaned_data)
            return redirect('index')
    else:
        form = SubscribeModelForm()
    return render(request, 'main/index.html', context={
        'header_info':header_info,
        'title_info':title_info,
        'contact_info_get':contact_info_get,
        'footer_info':footer_info,
        'latest_episodes':latest_episodes,
        'trending_episodes':trending_episodes,
        'topic_content':topic_content,
        'specialist_content':specialist_content,
    })

def about(request):
    contact_info_get = ContactGet.objects.all()[0]
    header_info = Header.objects.all()[0]
    title_info = Title.objects.all()[0]
    footer_info = Footer.objects.all()[0]
    about_page = About.objects.all()[0]
    about_content = About_Content.objects.all()
    if request.method == 'POST':
        form = SubscribeModelForm(request.POST)
        if form.is_valid():
            Subscribe.objects.create(**form.cleaned_data)
            return redirect('about')
    else:
        form = SubscribeModelForm()
    return render(request, 'main/about.html', context={
        'header_info':header_info,
        'title_info':title_info,
        'contact_info_get':contact_info_get,
        'footer_info':footer_info,
        'about_page':about_page,
        'about_content':about_content,
    })

def contact(request):
    if request.method == 'POST':
        form = ContactModelForm(request.POST)
        if form.is_valid():
            ContactPost.objects.create(**form.cleaned_data)
            return redirect('contact')
    else:
        form = ContactModelForm()
    footer_info = Footer.objects.all()[0]
    header_info = Header.objects.all()[0]
    title_info = Title.objects.all()[0]
    contact_info_get = ContactGet.objects.all()[0]
    if request.method == 'POST':
        form = SubscribeModelForm(request.POST)
        if form.is_valid():
            Subscribe.objects.create(**form.cleaned_data)
            return redirect('contact')
    else:
        form = SubscribeModelForm()
    return render(request, 'main/contact.html', context={
        'header_info':header_info,
        'title_info':title_info,
        'contact_info_get':contact_info_get,
        'footer_info':footer_info,
    })

def detail_page(request):
    contact_info_get = ContactGet.objects.all()[0]
    footer_info = Footer.objects.all()[0]
    header_info = Header.objects.all()[0]
    title_info = Title.objects.all()[0]
    trending_episodes = TrendingEpisode.objects.all()
    details_content = DetailContent.objects.all()[0]
    if request.method == 'POST':
        form = SubscribeModelForm(request.POST)
        if form.is_valid():
            Subscribe.objects.create(**form.cleaned_data)
            return redirect('detail-page')
    else:
        form = SubscribeModelForm()
    return render(request, 'main/detail-page.html', context={
        'header_info':header_info,
        'title_info':title_info,
        'contact_info_get':contact_info_get,
        'footer_info':footer_info,
        'trending_episodes':trending_episodes,
        'details_content':details_content,
    })

def listing_page(request):
    contact_info_get = ContactGet.objects.all()[0]
    footer_info = Footer.objects.all()[0]
    header_info = Header.objects.all()[0]
    title_info = Title.objects.all()[0]
    latest_episodes = LastestEpisode.objects.all()
    trending_episodes = TrendingEpisode.objects.all()
    if request.method == 'POST':
        form = SubscribeModelForm(request.POST)
        if form.is_valid():
            Subscribe.objects.create(**form.cleaned_data)
            return redirect('listing-page')
    else:
        form = SubscribeModelForm()
    return render(request, 'main/listing-page.html', context={
        'header_info':header_info,
        'title_info':title_info,
        'contact_info_get':contact_info_get,
        'footer_info':footer_info,
        'latest_episodes':latest_episodes,
        'trending_episodes':trending_episodes,
    })


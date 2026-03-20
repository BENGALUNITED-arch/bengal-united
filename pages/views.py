from django.shortcuts import render, get_object_or_404
from core.models import HeroSlide, SiteSettings
from players.models import Player
from news.models import News
from trophies.models import Trophy
from shop.models import Product
from gallery.models import Album
from .models import Facility, About, Program, JoinSection

def home(request):
    """Main homepage view with optimized database queries."""
    slides = HeroSlide.objects.filter(is_active=True).order_by('order')
    players = Player.objects.filter(is_active=True).order_by('jersey_number')[:4]
    latest_news = News.objects.filter(is_published=True).order_by('-publish_date')[:3]
    trophies = Trophy.objects.all()
    facilities = Facility.objects.all()
    programs = Program.objects.filter(is_active=True)
    products = Product.objects.all()[:4] 
    
    settings = SiteSettings.objects.first()
    about = About.objects.first()
    
    # SPEED BOOST: Prefetch photos for the Join Section slider
    join_section = JoinSection.objects.prefetch_related('photos').first()

    context = {
        'slides': slides, 
        'players': players, 
        'news': latest_news, 
        'settings': settings,
        'facilities': facilities, 
        'trophies': trophies, 
        'about': about, 
        'programs': programs,
        'products': products, 
        'join_section': join_section,
    }
    return render(request, 'pages/home.html', context)

def news_detail(request, article_id):
    """Detailed view for individual news articles."""
    article = get_object_or_404(News, id=article_id)
    settings = SiteSettings.objects.first()
    recent_news = News.objects.filter(is_published=True).exclude(id=article_id).order_by('-publish_date')[:3]
    
    context = {
        'article': article, 
        'settings': settings, 
        'recent_news': recent_news
    }
    return render(request, 'pages/news_detail.html', context)

def programs_page(request):
    """Dedicated page for all academy programs."""
    programs = Program.objects.filter(is_active=True)
    settings = SiteSettings.objects.first()
    
    context = {
        'programs': programs, 
        'settings': settings
    }
    return render(request, 'pages/programs.html', context)

def shop_page(request):
    """Main official store page."""
    products = Product.objects.all()
    settings = SiteSettings.objects.first()
    
    context = {
        'products': products, 
        'settings': settings
    }
    return render(request, 'pages/shop.html', context)

def product_detail(request, product_id):
    """Product order page."""
    product = get_object_or_404(Product, id=product_id)
    settings = SiteSettings.objects.first()
    
    context = {
        'product': product, 
        'settings': settings
    }
    return render(request, 'pages/product_detail.html', context)

def gallery_page(request):
    """
    Categorized gallery view.
    SPEED BOOST: Added .prefetch_related('photos') to fetch all images 
    in one go rather than one by one.
    """
    match_albums = Album.objects.filter(is_active=True, category='Match Day').prefetch_related('photos').order_by('-date_created')
    practice_albums = Album.objects.filter(is_active=True, category='Practice').prefetch_related('photos').order_by('-date_created')
    bts_albums = Album.objects.filter(is_active=True, category='Behind The Scenes').prefetch_related('photos').order_by('-date_created')
    
    settings = SiteSettings.objects.first()
    
    context = {
        'match_albums': match_albums, 
        'practice_albums': practice_albums, 
        'bts_albums': bts_albums, 
        'settings': settings
    }
    return render(request, 'pages/gallery.html', context)

def about_detail(request):
    """Dedicated About Us page."""
    about = About.objects.first()
    settings = SiteSettings.objects.first()
    context = {
        'about': about,
        'settings': settings,
    }
    return render(request, 'pages/about_detail.html', context)
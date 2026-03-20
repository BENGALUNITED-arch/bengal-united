from django import template
from players.models import Player
from news.models import News
from trophies.models import Trophy

register = template.Library()

@register.simple_tag
def get_total_players():
    return Player.objects.count()

@register.simple_tag
def get_total_news():
    return News.objects.count()

@register.simple_tag
def get_total_trophies():
    return Trophy.objects.count()
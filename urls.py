from django.urls import path
from .views import RandomQuoteView,FavoriteQuoteView

urlpatterns=[
    path('random/',RandomQuoteView.as_view(),name='random-quote'),
path('favorites/', FavoriteQuoteView.as_view(), name='favorite-quotes'),
]
from django.urls import path, include
from . import views
urlpatterns = [
    path('partner-list/', views.PartnerListView.as_view()),
    path('faq-list/', views.FAQListView.as_view()),
    path('review-list/', views.ReviewListView.as_view()),
    path('news-list/', views.NewsListView.as_view()),
]
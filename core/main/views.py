from django.shortcuts import render
from rest_framework import generics
from . import serializers, models

class PartnerListView(generics.ListAPIView):
    """Получить список партнера"""
    queryset = models.Partners.objects.all()
    serializer_class = serializers.PartnerSerializer

class FAQListView(generics.ListAPIView):
    """Получить список ответы-вопросы"""
    queryset = models.FAQ.objects.all()
    serializer_class = serializers.FAQSerializer

class ReviewListView(generics.ListAPIView):
    """Получить список отзывов"""
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer

class NewsListView(generics.ListAPIView):
    """Получить список новостей"""
    queryset = models.News.objects.all()
    serializer_class = serializers.NewsSerializer
from rest_framework import serializers
from . import models

class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Partners
        fields = '__all__'
class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FAQ
        fields = '__all__'
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = '__all__'
class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.News
        fields = '__all__'
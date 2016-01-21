from rest_framework import serializers
from display.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'author', 'pub_date', 'text')

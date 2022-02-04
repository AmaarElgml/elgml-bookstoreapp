from rest_framework import serializers
from storeapp.models import Book, Author, News, AppAdmin


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class AppAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppAdmin
        fields = '__all__'

from rest_framework import serializers
from .models import Category, Post


class CategorySerializer(serializers.ModelSerializer):
    """
    カテゴリのシリアライザー
    記事のカテゴリ名や色も一緒に取得したいので、
    記事シリアライザ2つで使われているほか、
    カテゴリ一覧のためのビューでも使う予定
    fieldsは__all__と書いてもOK
    """
    class Meta:
        model = Category
        fields = ('id', 'name', 'color',)


class SimplePostSerializer(serializers.ModelSerializer):
    """
    記事一覧ビューで使う記事モデルのシリアライザー
    記事一覧の取得では詳細なデータはいらないので、
    本文や作成日といったフィールドをexcludeで除外してる。
    """
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Post
        exclude = ('main_text', 'created_at')


class PostSerializer(serializers.ModelSerializer):
    """
    記事の詳細データ取得ビューで使うため、
    全てのフィールドを含めたシリアライザー
    """
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Post
        fields = '__all__'
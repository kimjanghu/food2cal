from rest_framework import serializers
from users.serializers import UserSerializer
from .models import Post, Comment, Vote

from diets.serializers import DietSerializer, DietListSerializer

# post 리스트
class PostListSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    class Meta:
        model = Post
        # 게시글 제목이랑 작성자만 보여주기
        fields = '__all__'
        read_only_fields = ('id', 'user', 'created_at', 'updated_at')


class PostUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('id', 'user', 'created_at')


class CommentListSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    class Meta:
        model = Comment
        fields='__all__'
        read_only_fields = ('id', 'user', 'created_at')

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('id', 'user','created_at', 'updated_at', 'post')

# 게시글 상세정보
class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    # commments = CommentSerializer(many=True, read_only=True)
    # diets = DietSerializer(many=True, read_only=True)
    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('id', 'user', 'created_at', 'updated_at')

class CommentUpdateSeriailzer(serializers.ModelSerializer):
    # user = UserSerializer(required=False)
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('id', 'user','created_at', 'post')

class VoteSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    class Meta:
        model = Vote
        fields = '__all__'
        read_only_fields = ('user',)


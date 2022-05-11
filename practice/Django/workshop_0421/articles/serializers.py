from rest_framework import serializers
from .models import Artist, Music


class MusicListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = '__all__'

class MusicListSerializer(serializers.ModelSerializer):
    artist = Music.objects.artist(many=True, read_only=True)
    class Meta:
        model = Music
        fields = '__all__'

# class ArticleDetailSerializer(serializers.ModelSerializer):
#     # comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
#     comment_set = MusicListSerializer(many=True, read_only=True)
#     class Meta:
#         model = Article
#         fields = '__all__'


class ArtistListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artist
        fields = ('id', 'name',)

class ArtistSerializer(serializers.ModelSerializer):
    music_set = MusicListSerializer(many=True, read_only=True)
    music_count = music_set.count()

    class Meta:
        model = Artist
        fields = '__all__'
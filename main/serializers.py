from rest_framework import serializers
from main.models import Main
from django.contrib.auth.models import User

class MainSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='main-highlight', format='html')

    class Meta:
        model = Main
        fields = ['url', 'id', 'highlight', 'owner', 'title', 'body']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    main = serializers.HyperlinkedRelatedField(many=True, view_name='main-detail', read_only=True)
    
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'password', 'main']
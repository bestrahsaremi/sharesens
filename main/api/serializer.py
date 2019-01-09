from rest_framework.serializers import ModelSerializer

from main.models import Sentences

class SensSerializer(ModelSerializer):

    class Meta:
        model = Sentences
        fields = ['id', 'title']
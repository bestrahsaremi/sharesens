from rest_framework.generics import ListAPIView
from main.models import Sentences
from .serializer import (SensSerializer)

class SentencesListAPIView(ListAPIView):
    queryset = Sentences.objects.all()
    serializer_class = SensSerializer

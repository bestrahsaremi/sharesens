from django.urls import path
from .views import (
    SentencesListAPIView
)


urlpatterns = [
    path('', SentencesListAPIView.as_view(), name="sens_list"),
]


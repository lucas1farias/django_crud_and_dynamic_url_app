

from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),

    # Url p/ todos os cartões (todos os objetos do modelo PoEDivinationCard)
    path('poe-div-cards/', PoeCardsView.as_view(), name='poe-div-cards'),

    # Url p/ formulário que edita todos os campos
    path('poe-div-cards/all/id=<int:pk>/<str:slug>', EditPoeCardAnyField.as_view(), name='all'),

    # Url p/ formulário que edita campos de forma separada
    path('poe-div-cards/edit/name/id=<int:pk>/<str:slug>', EditPoeCardNameView.as_view(), name='name'),
    path('poe-div-cards/edit/description/id=<int:pk>/<str:slug>', EditPoeCardDescriptionView.as_view(), name='description'),
    path('poe-div-cards/edit/stack-size/id=<int:pk>/<str:slug>', EditPoeCardStackSizeView.as_view(), name='stack-size'),
    path('poe-div-cards/edit/image/id=<int:pk>/<str:slug>', EditPoeCardImageView.as_view(), name='img')
]

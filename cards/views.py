

from django.shortcuts import render

from django.views.generic import ListView
from django.views.generic import TemplateView
from django.views.generic import UpdateView

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy

from .models import *

from os import remove


class IndexView(TemplateView):
    template_name = 'index.html'


class PoeCardsView(ListView):
    template_name = 'poe_div_cards.html'
    context_object_name = 'poe_cards_db'
    model = PoEDivinationCard


# View p/ alterar o campo do modelo "PoeDivinationCard": qualquer um
class EditPoeCardAnyField(UpdateView):
    fields = ('name', 'description', 'stack_size', 'image')
    model = PoEDivinationCard
    template_name = 'edit_card_any_field.html'
    success_message = 'Carta alterada com sucesso!'  # Não é mandatório

    def post(self, request, pk, *args, **kwargs):
        if str(self.request.method) == 'POST':
            input_values = {
                'name': self.request.POST.get('name'),
                'description': self.request.POST.get('description'),
                'stack_size': self.request.POST.get('stack_size'),
                'image': self.request.FILES.get('image')
            }

            card = PoEDivinationCard.objects.get(pk=pk)

            if input_values['name'] != '':
                card.name = input_values['name']
            if input_values['description'] != '':
                card.description = input_values['description']
            if input_values['stack_size'] != '':
                card.stack_size = input_values['stack_size']
            if input_values['image'] is not None:
                card.image = input_values['image']

            card.save()
            return redirect('poe-div-cards')


# View p/ alterar o campo do modelo "PoeDivinationCard": name
class EditPoeCardNameView(SuccessMessageMixin, UpdateView):
    fields = ('name', )
    model = PoEDivinationCard
    template_name = 'edit_card_field_name.html'
    # success_message = 'Nome da carta alterado com sucesso!'  # Não é mandatório
    # success_url = reverse_lazy('poe-div-cards')

    # FUNÇÃO ADD POSTERIORMENTE APENAS COM O INTUITO DE EXIBIR UMA MENSAGEM MENOS GENÉRICA QUE EM 'success_messages'
    # POR CAUSA DO RETORNO DESSA FUNÇÃO, 'success_url' também perde a utilidade acima
    def post(self, request, pk, *args, **kwargs):
        if str(self.request.method) == 'POST':
            card = PoEDivinationCard.objects.get(pk=pk)
            card_name_then = card.name
            card_name_now = self.request.POST.get('name')
            card.name = card_name_now
            card.save()
            msg = f'A carta "{card_name_then}" teve seu nome modificado para "{card_name_now}"'
            messages.success(request, msg)
            return redirect('poe-div-cards')


# View p/ alterar o campo do modelo "PoeDivinationCard": description
class EditPoeCardDescriptionView(SuccessMessageMixin, UpdateView):
    fields = ('description', )
    model = PoEDivinationCard
    success_url = reverse_lazy('poe-div-cards')
    template_name = 'edit_card_field_description.html'
    success_message = 'Descrição da carta alterada com sucesso!'  # Não é mandatório


# View p/ alterar o campo do modelo "PoeDivinationCard": stack_size
class EditPoeCardStackSizeView(SuccessMessageMixin, UpdateView):
    fields = ('stack_size', )
    model = PoEDivinationCard
    template_name = 'edit_card_field_stack_size.html'
    # success_message = 'Quantidade da carta alterada com sucesso!'  # Não é mandatório
    # success_url = reverse_lazy('poe-div-cards')

    # FUNÇÃO ADD POSTERIORMENTE APENAS COM O INTUITO DE EXIBIR UMA MENSAGEM MENOS GENÉRICA QUE EM 'success_messages'
    # POR CAUSA DO RETORNO DESSA FUNÇÃO, 'success_url' também perde a utilidade acima
    def post(self, request, pk, *args, **kwargs):
        if str(self.request.method) == 'POST':
            card = PoEDivinationCard.objects.get(pk=pk)
            card_stack_size_then = card.stack_size
            card_stack_size_now = self.request.POST.get('stack_size')
            card.stack_size = card_stack_size_now
            card.save()
            msg = f'A carta {card.name} teve sua qtd. alterada de {card_stack_size_then} para {card_stack_size_now}'
            messages.success(request, msg)
            return redirect('poe-div-cards')


# View p/ alterar o campo do modelo "PoeDivinationCard": image
class EditPoeCardImageView(UpdateView):
    fields = ('image', )
    model = PoEDivinationCard
    success_url = reverse_lazy('poe-div-cards')
    template_name = 'edit_card_field_image.html'

    def post(self, request, pk, *args, **kwargs):
        if str(self.request.method) == 'POST':
            card = PoEDivinationCard.objects.get(pk=pk)
            new_image = self.request.FILES.get('image')
            if new_image is not None:
                remove(card.image.path)
                card.image = new_image
                card.save()
                msg = f'A carta {card.name} teve sua imagem alterada!'
                messages.success(request, msg)
                return redirect('poe-div-cards')

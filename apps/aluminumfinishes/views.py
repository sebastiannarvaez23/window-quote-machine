from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from apps.aluminumfinishes.models import AluminumFinishes

# Create your views here.
@method_decorator(login_required, name='dispatch') 
class AluminumFinishesTemplateView(TemplateView):
    template_name = "aluminum-finishes.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['aluminum_finishes'] = AluminumFinishes.objects.all()
        return context

@method_decorator(login_required, name='dispatch')
class AluminumFinishesCreateView(CreateView):
    model = AluminumFinishes
    template_name = "aluminum-finishes.html"
    fields = ['name', 'price']
    
    def get_success_url(self):
        return reverse_lazy('aluminumfinishes')
    
    def form_valid(self, form):
        name = self.request.POST.get('name')
        price = self.request.POST.get('price')
        # Pendiente terminar esta validación
        if name == None or price == None: return HttpResponse(status=400)
        aluminum_finishes = AluminumFinishes(name=name, price=price)
        aluminum_finishes.save()

        return HttpResponseRedirect(redirect_to=self.get_success_url())

@method_decorator(login_required, name='dispatch')
class AluminumFinishesUpdateView(UpdateView):
    model = AluminumFinishes
    template_name = "aluminum-finishes-update.html"
    fields = ['name', 'price']
    
    def get_success_url(self):
        return reverse_lazy('aluminumfinishes')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        return response

@method_decorator(login_required, name='dispatch')
class AluminumFinishesDeleteView(DeleteView):
    model = AluminumFinishes
    template_name = 'aluminum-finishes-conf-delete.html'
    success_url = reverse_lazy('aluminumfinishes')
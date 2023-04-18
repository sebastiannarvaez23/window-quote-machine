from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView
from glasstype.models import GlassType

# Create your views here.
@method_decorator(login_required, name='dispatch')
class GlassTypeTemplateView(TemplateView):
    template_name = "glass_type.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['glasses_types'] = GlassType.objects.all()
        return context
    
@method_decorator(login_required, name='dispatch')
class GlassTypeCreateView(CreateView):
    model = GlassType
    template_name = "window_styles.html"
    fields = ['name', 'price']
    
    def get_success_url(self):
        return reverse_lazy('glasstype')
    
    def form_valid(self, form):
        name = self.request.POST.get('name')
        price = self.request.POST.get('price')
        # Pendiente terminar esta validación
        if name == None or price == None: return HttpResponse(status=400)
        style_window = GlassType(name=name, price=price)
        style_window.save()

        return HttpResponseRedirect(redirect_to=self.get_success_url())

@method_decorator(login_required, name='dispatch')
class GlassTypeDeleteView(DeleteView):
    model = GlassType
    template_name = 'glass_type_conf_delete.html'
    success_url = reverse_lazy('glasstype')
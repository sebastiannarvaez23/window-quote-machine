from django.urls import path
from window import views

urlpatterns = [
    # Templates
    path('', views.QuoteWindowTemplateView.as_view(), name='quote'),
    path('styles/', views.StylesWindowTemplateView.as_view(), name="windowstyles"),
    path('aluminum/', views.AluminumFinishesTemplateView.as_view(), name="aluminumfinishes"),
    # API
    path('quote/', views.getQuoteWindow, name="windowquote"),
]
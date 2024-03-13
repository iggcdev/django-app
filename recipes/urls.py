from django.urls import path
from recipes.views import home, contact, about


urlpatterns = [
    path('', home),  # HOME
    path('about/', about),  # Sobre
    path('contact/', contact),  # Contato

]

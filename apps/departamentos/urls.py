from django.urls import path
from .views import DepartamentosList #, DepartamentoCreate, DepartamentoEdit

urlpatterns = [
    path('', DepartamentosList.as_view(), name='list_departamentos'),
    #path('editar/<int:pk>/', EmpresaEdit.as_view(), name='edit_empresa'),
]
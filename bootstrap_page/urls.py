from django.urls import path

from . import views

app_name = 'bootstrap_page'

urlpatterns = [
  path('', views.bootstrap_page.as_view(), name=''),
 # path('new', views.BookCreate.as_view(), name='book_new'),
 # path('edit/<int:pk>', views.BookUpdate.as_view(), name='book_edit'),
 # path('delete/<int:pk>', views.BookDelete.as_view(), name='book_delete'),
]
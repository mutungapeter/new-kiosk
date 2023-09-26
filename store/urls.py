from django.urls import path
from . import views
urlpatterns = [
    path("", views.store, name="store"),
    path("category/<slug:category_slug>/",
         views.store, name="products_by_category"),
    path("category/<slug:category_slug>/<slug:product_slug>/",
         views.product_detail, name="product_detail"),
    path("search/", views.search, name="search"),

    path('submit_review/<int:product_id>/',
         views.submit_review, name='submit_review'),


    path("add_product/", views.add_product, name="add_product"),
    path("products/", views.products, name="products"),






    path('edit_product/<int:pk>/', views.Edit_product, name='edit_product'),
    path('delete_product/<int:pk>/', views.delete_product, name='delete_product'),


]

from django.urls import path
from .views import *

urlpatterns = [
    path('get-Info/', get_Info),
    path('post-order/', post_order),
    path('get-product/', get_product),
    path('get-order/', get_order),
    path('get-productinfo/', get_productinfo),
    path('get-fakt/', get_fakt),
    path('get-aboutus/', get_aboutus),
    path('get-productfaq/', get_productfaq),
    path('get-header/', get_header),
    path('get-faq/', get_faq),
    path('get-advice/', get_advice),
    path('get-abouttea/', get_abouttea),
]
from django.urls import path
from .views import ProductView, ApplicationsViews, SpecialistUpdateDeleteView

urlpatterns = [
    path('product/', ProductView.as_view(), name='product-list-create'),
    path('applications/', ApplicationsViews.as_view(), name='applications'),
    path('specialist/', SpecialistUpdateDeleteView.as_view(), name='specialist')
]
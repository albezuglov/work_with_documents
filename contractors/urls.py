from django.conf.urls import url
from .views import ContractorList

urlpatterns = [
    url(r'^$', ContractorList.as_view(), name='contractor_list'),
]
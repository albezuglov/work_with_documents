from django.views.generic.list import ListView
from .models import Contractor, AccountingDetails, BankDetails
# Create your views here.

class ContractorList(ListView):
    model = Contractor


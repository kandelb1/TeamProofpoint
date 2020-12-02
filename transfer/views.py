from django.shortcuts import render
from django.http import HttpResponse
import sys
import os.path

from transferData import transfer

sys.path.append(os.path.abspath(os.path.join(os.path.dirname('transferData'), os.path.pardir)))

from transferData import transfer
# Create your views here.
def transferDatabase(request):
    # run transfer data calls to refresh database when called

    transfer("leads_lead", "stats", "proofpointDB.db")
    transfer("stocks_stocks", "statsStocks", "proofpointDBnewnew.db")
    # update user that transfer was done successfully
    return HttpResponse("Transfer Complete!")

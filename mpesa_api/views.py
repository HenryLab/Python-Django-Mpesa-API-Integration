from django.http import HttpResponse
import requests
from requests.auth import HTTPBasicAuth
from datetime import datetime
import base64
import json


def getAccessToken(request):
    consumer_key = 'cHnkwYIgBbrxlgBoneczmIJFXVm0oHky'
    consumer_secret = '2nHEyWSD4VjpNh2g'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token['access_token']

    return HttpResponse(validated_mpesa_access_token)


def lipa_na_mpesa_online(request):
    access_token = getAccessToken()
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = {"Authorization": "Bearer %s" % access_token}
    request = {
        "BusinessShortCode": "174379",
        "Password": "",
        "Timestamp": "",
        "TransactionType": "CustomerPayBillOnline",
        "Amount": " ",
        "PartyA": " ",
        "PartyB": " ",
        "PhoneNumber": " ",
        "CallBackURL": "https://ip_address:port/callback",
        "AccountReference": " ",
        "TransactionDesc": " "
    }

    response = requests.post(api_url, json=request, headers=headers)
    return HttpResponse('success')




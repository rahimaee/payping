import requests
import json


# ساخت کد پرداخت
def make_payment_code(header='', amount=2000, payerIdentity='', payerName='', description='', returnUrl='',
                      clientRefId=''):
    url = 'https://api.payping.ir/v1/pay'
    body = {
        "amount": amount,
        "payerIdentity": payerIdentity,
        "payerName": payerName,
        "description": description,
        "returnUrl": returnUrl,
        "clientRefId": clientRefId
    }
    res = requests.post(url, data=json.dumps(body), headers=header)
    if res.status_code == 200:
        code = res.json().get('code')
        return code
    return res.status_code


# دریافت ادرس صفحه پرداخت
def get_url_payment(code=''):
    return f'https://api.payping.ir/v2/pay/gotoipg/{code}'


# تایید پرداخت
def verify_payment(header='', refid='', amount=0):
    url = 'https://api.payping.ir/v2/pay/verify'
    body = {
        "refId": refid,
        "amount": amount
    }
    res = requests.post(url, data=json.dumps(body), headers=header)
    if res.status_code == 200:
        return res.json()
    return res.status_code

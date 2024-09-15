import requests
import kavenegar
def SMS():

    Api_key = '4F7846335857707467322B4D472F44367A4B4F31326A78565851384A4F4E4F6554764A4879616C715337413D'
    response1 = requests.get('https://api.coinlore.net/api/ticker/?id=90')
    response2 = requests.get('https://api.coinlore.net/api/ticker/?id=80')
    price = float(response1.json()[0]['price_usd'])
    price2 = float(response2.json()[0]['price_usd'])

    api =kavenegar.KavenegarAPI(Api_key)
    params = {
        'sender': '',
        'receptor': '09013559494',
        'message': 'قیمت لحظه ای بیت کوین %i دلار است'%price,
    }
    response = api.sms_send(params)
    print (response)

SMS()
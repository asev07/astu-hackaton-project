import json
import time
import jwt
import requests


def generate_payment_url(self, merchant_id, reason, amount, private_key, token, success_redirect_url, failure_redirect_url, notify_url):
        current_time = int(time.time())
        data = {
            "amount": amount,
            "paymentReason": reason,
            "merchantId": merchant_id,
            "generated": current_time
        }
        signed_token  = jwt.encode(data, private_key, algorithm="ES256")
    
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

        data = {
            "id": "1r4ftfrftgvtg",
            "amount": amount,
            "reason": reason,
            "merchantId": merchant_id,
            "signedToken": signed_token,
            "successRedirectUrl": success_redirect_url,
            "failureRedirectUrl": failure_redirect_url,
            "notifyUrl": notify_url
        }
        URL = "https://services.santimpay.com/api/v1/gateway/initiate-payment"
        try:
            response = requests.post(URL, headers=headers, data=json.dumps(data))
            print(response.content)

        except requests.exceptions.RequestException as e:
            print(e)

SANTIMPAY_GATEWAY_TOKEN = "'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwaG9uZU51bWJlciI6IisyNTE5MTAxMDEwMTAiLCJ3YWxsZXRJZCI6IjJkY2I0MzE0LTg0MTAtNDQ1YS05YjVlLTczNWE5YjE0OTZkZCIsInVzZXJJZCI6IjZkMjhhZmFiLTkzOWUtNGZjMC04Mzg1LTA4M2I2Zjc1ZTQwYSIsImRldmljZUlkIjoic2FtcG1tazIiLCJleHAiOjE2ODUwNzg2Mjd9.tJkcBi5FiSv9HDS1QLj0SsRxvvVbRFDaYHiVyx6no7w'"

PRIVATE_KEY_IN_PEM='-----BEGIN EC PRIVATE KEY-----\nMHcCAQEEII0qPPByHBzW3znAladzC0uQDi6vhgctF/r6NYlN4ftmoAoGCCqGSM49\nAwEHoUQDQgAE4zghgXLQRJWd56Fe282IVNChD+oa8cNdSAZ6DaELdExs2lKmjXeS\nxU/A8YCNg1GqgfrrLcx3eHnI+Qm6+ppgng==\n-----END EC PRIVATE KEY-----\n'

GATEWAY_MERCHANT_ID = "9e2dab64-e2bb-4837-9b85-d855dd878d2b"
id='25tgtgygygy6gy6g'
success_redirect_url = 'https://santimpay.com'
failure_redirect_url = 'https://santimpay.com'

# backend url to receive a status update (webhook)
notify_url = 'https://santimpay.com'
client = generate_payment_url(id, GATEWAY_MERCHANT_ID,'payment for coffee',1,PRIVATE_KEY_IN_PEM,SANTIMPAY_GATEWAY_TOKEN, success_redirect_url, failure_redirect_url, notify_url)
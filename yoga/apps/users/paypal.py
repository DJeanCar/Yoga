#encoding=utf-8
import paypalrestsdk

from django.conf import settings
from django.shortcuts import redirect

paypalrestsdk.configure({
        "mode": settings.PAYPAL_MODE,
        "client_id": settings.PAYPAL_CLIENT_ID,
        "client_secret": settings.PAYPAL_CLIENT_SECRET 
    })


def paypal_create(request):
	
	payment = paypalrestsdk.Payment({
        "intent": "sale",
        "payer": {
            "payment_method": "paypal"
		    },


        "redirect_urls": {
            "return_url": 'http://localhost:8000/paypal/execute/',
            "cancel_url": 'http://localhost:8000/' },
            

        "transactions": [{

            "item_list": {
                "items": [{
                    "name": 'Usuario Premium',
                    "price": 1,
                    "currency": "USD",
                    "quantity": 1 }]
                },

            "amount":  {
                "total": 1,
                "currency": "USD" },
            "description": 'Usuario Premium' }]

        })

	redirect_url = "/"

	if payment.create():
        # Store payment id in user session
		request.session['payment_id'] = payment.id
        # Redirect the user to given approval url
		for link in payment.links:
			if link.method == "REDIRECT":
				redirect_url = link.href
		return redirect(redirect_url)

	else:
		return redirect('/error/')


def paypal_execute(request):
	payment_id = request.session['payment_id']
	payer_id = request.GET['PayerID']

	payment = paypalrestsdk.Payment.find(payment_id)
	payment_name = payment.transactions[0].item_list.items[0].name

	if payment.execute({"payer_id": payer_id}):
        # the payment has been accepted
		user = request.user
        user.premium = True
        user.save()
	return redirect('/felicitaciones/')
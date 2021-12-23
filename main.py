from flask import Flask, redirect, url_for, render_template, request
from flask_uploads import UploadSet, configure_uploads, IMAGES

import glob
import os

import numpy as np
import pandas as pd

# Configure Flask app
app = Flask(__name__)
app.config['Dataframes'] = 'static/Dataframes'

#Variables

#Login Page
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

#Home Page
@app.route('/home', methods=['GET'])
def home():
	return render_template('home.html')

#New Order Page
@app.route('/new-cad-order', methods=['GET', 'POST'])
def CAD_order():
	error = None
	if request.method == 'POST':
		Order_ID = request.form['Order_ID']
		Order_Date = request.form['Order_Date']
		Customer_Name = request.form['Customer_Name']
		Order_Balance_Without_Tax = request.form['Order_Balance_Without_Tax']
		Delivery_Date = request.form['Delivery_Date']
		Final_Order_Balance_With_Tax = request.form['Final_Order_Balance_With_Tax']
		Payment_Date = request.form['Payment_Date']
		Check_Number = request.form['Check_Number']
		Deposit_Date = request.form['Deposit_Date']
		Verification_Date = request.form['Verification_Date']

		key = 'Allow'

		if Order_ID == '':
			error = 'Invalid Order id. Please try again.'
			return render_template('CAD_order.html', error=error)

		if Order_Date == '':
			error = 'Invalid Order Date. Please try again.'
			return render_template('CAD_order.html', error=error)

		if Customer_Name == '':
			error = 'Invalid Customer Name. Please try again.'
			return render_template('CAD_order.html', error=error)

		if Order_Balance_Without_Tax == '':
			error = 'Invalid Order Balance. Please try again.'
			return render_template('CAD_order.html', error=error)

		Downpayment_Balance = float(Order_Balance_Without_Tax) * 0.3

		Revenue_Check = ''

		if Final_Order_Balance_With_Tax != '':
			Revenue_Check = float(Final_Order_Balance_With_Tax) - float(Downpayment_Balance)
			Revenue_Check = str(Revenue_Check) + ' $CAD'
				
		if Delivery_Date == '':
			Order_Delivered = 'No'
		else: Order_Delivered = 'Yes'	

		if Payment_Date == '':
			Payment_Received = 'No'
		else: Payment_Received = 'Yes'	

		if Deposit_Date == '':
			Bank_Deposit = 'No'
		else: Bank_Deposit = 'Yes'	

		if Verification_Date == '':
			Verification = 'No'
		else: Verification = 'Yes'	

		Downpayment_Balance = str(Downpayment_Balance) + ' $CAD'
		Order_Balance_Without_Tax = Order_Balance_Without_Tax + ' $CAD'
		Final_Order_Balance_With_Tax = Final_Order_Balance_With_Tax + '$CAD'

		return render_template('tracking.html', ID=Order_ID, OrderDate=Order_Date, CustomerName=Customer_Name,
	OrderBalance=Order_Balance_Without_Tax, Downpayment=Downpayment_Balance, Delivery=Order_Delivered, DeliveryDate=Delivery_Date,
	FinalOrderBalance=Final_Order_Balance_With_Tax, RCheck=Revenue_Check, PReceival=Payment_Received, PaymentDate=Payment_Date,
	CheckNum=Check_Number, Deposit=Bank_Deposit, DepositDate=Deposit_Date, Ver=Verification, VerDate=Verification_Date, key=key)
	
	return render_template('CAD_order.html')


@app.route('/new-usd-order', methods=['GET', 'POST'])
def USD_order():
	error = None
	if request.method == 'POST':
		Order_ID = request.form['Order_ID']
		Order_Date = request.form['Order_Date']
		Customer_Name = request.form['Customer_Name']
		Order_Balance_Without_Tax = request.form['Order_Balance_Without_Tax']
		Delivery_Date = request.form['Delivery_Date']
		Final_Order_Balance_With_Tax = request.form['Final_Order_Balance_With_Tax']
		Payment_Date = request.form['Payment_Date']
		Check_Number = request.form['Check_Number']
		Deposit_Date = request.form['Deposit_Date']
		Verification_Date = request.form['Verification_Date']

		key = 'Allow'

		if Order_ID == '':
			error = 'Invalid Order id. Please try again.'
			return render_template('USD_order.html', error=error)

		if Order_Date == '':
			error = 'Invalid Order Date. Please try again.'
			return render_template('USD_order.html', error=error)

		if Customer_Name == '':
			error = 'Invalid Customer Name. Please try again.'
			return render_template('USD_order.html', error=error)

		if Order_Balance_Without_Tax == '':
			error = 'Invalid Order Balance. Please try again.'
			return render_template('USD_order.html', error=error)

		Downpayment_Balance = float(Order_Balance_Without_Tax) * 0.3
		
		Revenue_Check = ''

		if Final_Order_Balance_With_Tax != '':
			Revenue_Check = float(Final_Order_Balance_With_Tax) - float(Downpayment_Balance)
			Revenue_Check = str(Revenue_Check) + ' $USD'
		
		if Delivery_Date == '':
			Order_Delivered = 'No'
		else: Order_Delivered = 'Yes'	

		if Payment_Date == '':
			Payment_Received = 'No'
		else: Payment_Received = 'Yes'	

		if Deposit_Date == '':
			Bank_Deposit = 'No'
		else: Bank_Deposit = 'Yes'	

		if Verification_Date == '':
			Verification = 'No'
		else: Verification = 'Yes'	

		Downpayment_Balance = str(Downpayment_Balance) + ' $USD'
		Order_Balance_Without_Tax = Order_Balance_Without_Tax + ' $USD'
		Final_Order_Balance_With_Tax = Final_Order_Balance_With_Tax + '$USD'

		return render_template('tracking.html', ID=Order_ID, OrderDate=Order_Date, CustomerName=Customer_Name,
	OrderBalance=Order_Balance_Without_Tax, Downpayment=Downpayment_Balance, Delivery=Order_Delivered, DeliveryDate=Delivery_Date,
	FinalOrderBalance=Final_Order_Balance_With_Tax, RCheck=Revenue_Check, PReceival=Payment_Received, PaymentDate=Payment_Date,
	CheckNum=Check_Number, Deposit=Bank_Deposit, DepositDate=Deposit_Date, Ver=Verification, VerDate=Verification_Date, key=key)

	return render_template('USD_order.html')


#Tracking Page for All Orders
@app.route('/tracking', methods=['GET', 'POST'])	
def tracking():
	return render_template('tracking.html')	


if __name__ == '__main__':
    app.run(debug=True)
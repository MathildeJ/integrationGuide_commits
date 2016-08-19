from flask import Flask, request, make_response, render_template
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/landing_page')
def landing_page():
   return render_template('landing_page.html')

@app.route('/order_form')
def order_form():
   return render_template('order_form.html')

@app.route('/survey')
def survey():
   return render_template('survey.html')

@app.route('/receipt')
def receipt():
   return render_template('receipt.html')

@app.route('/thank_you')
def thank_you():
   return render_template('thank_you.html')

@app.route('/customer_login')
def customer_login():
   return render_template('customer_login.html')

@app.route('/thanks_survey')
def thanks_survey():
   return render_template('thanks_survey.html')

@app.route('/restricted')
def restricted():
   return render_template('restricted.html')


    from flask import Flask, render_template, request, redirect
    import alpaca_trade_api as tradeapi

    app = Flask(__name__)

    @app.route('/', methods=['GET', 'POST'])
    def index():
        if request.method == 'POST':
            api_key = request.form['api_key']
            secret_key = request.form['secret_key']
            # Store keys securely (e.g., environment variables, database)
            return redirect('/dashboard')
        return render_template('index.html')

    @app.route('/dashboard')
    def dashboard():
         api_key = request.form.get('api_key')
         secret_key = request.form.get('secret_key')
         api = tradeapi.REST(api_key, secret_key, base_url="https://paper-api.alpaca.markets")
         account = api.get_account()
         return render_template('dashboard.html', account=account)

    if __name__ == '__main__':
        app.run(debug=True)

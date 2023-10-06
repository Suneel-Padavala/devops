from flask import Flask, render_template
from flask_talisman import Talisman

app = Flask(__name__)
talisman = Talisman(app)
cert_dir = './ssl_certificates/'

cert = cert_dir + 'server.cert'
key = cert_dir + 'server.key'
print(cert, key)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', ssl_context=(cert,key))

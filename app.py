from flask import Flask, request, render_template, redirect, url_for, session, logging, jsonify


app = Flask(__name__)

@app.route('/health')
def health():
    return jsonify(status='UP')

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('/404.html')


@app.route('/validate', methods=['GET', 'POST'])
def validate():
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        return f'Hello {fname} {lname}'
    elif request.method == 'GET':
        pass

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
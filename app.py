from flask import Flask, render_template


app = Flask(__name__)
state = 'on'

@app.route('/')
def home():
    return render_template('page.html', status='process started')

@app.route('/status_on')
def turn_on():
    global state
    state = 'on'
    return render_template('page.html', status='current status: on')

@app.route('/status_off')
def turn_off():
    global state
    state = 'off'
    return render_template('page.html', status='current status: off')

@app.route('/status')
def current_state():
    global state
    return render_template('page.html', status=f'current status: {state}')

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
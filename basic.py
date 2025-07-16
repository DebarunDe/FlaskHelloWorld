from flask import Flask
app = Flask('Simple App')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.data:
            return 'GOT a POST request with a body: %s' % str(request.data)
        else:
            return 'Got a POST request without a body!'
    else:
        return 'index function from a GET request'
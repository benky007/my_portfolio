from flask import Flask, request, render_template

app = Flask(__name__, template_folder="templates")


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def get_coords():
    data = request.get_json()
    x = data['X']
    y = data['Y']
    print(f"Received coordinates: X - {x}, Y - {y}")
    return {'X': x, 'Y': y}


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True, ssl_context='adhoc')

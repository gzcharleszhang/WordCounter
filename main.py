from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


# @app.route('/index')
# def form():
#     return render_template('index.html')

# @app.route('/index', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         asd = request.json
#         print(asd)
#         session['formdata'] = asd
#         if 'formdata' in session:
#             return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}
#     return render_template("index.html")

lib = dict()

def count(arr):
    for i in range(len(arr)):
        if arr[i] in lib:
            num = lib.get(arr[i])
            num = int(num)
            num = num + 1
            lib[arr[i]] = num
        else:
            lib[arr[i]] = 1

    st2 = ""

    for k, v in lib.items():
        k = str(k)
        v = str(v)
        st2 += k + " " + v + "\n"

    return st2


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/_start_count', methods=["GET", "POST"])
def start_count():
    """Add two numbers server side, ridiculous but well..."""
    a = request.args.get('userInput', 0, type=str)
    arr = a.split()
    lib.clear()
    st = count(arr)
    return jsonify(result=st)
    # return jsonify(result=a)

@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500


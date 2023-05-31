from flask import Flask, render_template, request, jsonify
app = Flask(__name__)


@app.route('/hello/<string:name>', strict_slashes=False)
def greetings(name):
    """Returns strings"""
    return f"Hello, {name}"


@app.route('/python/')
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    """Defines the python text"""
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def number(n):
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def render(n):
    return render_template('index.html', num=n+1)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    if n % 2 == 0:
        return render_template('index.html', num=f"{n} is even")
    else:
        return render_template('index.html', num=f"{n} is odd")


@app.route('/test_loop/<int:n>', strict_flashes=False)
def test_loop(n):
    return render_template('loop.html', start=range(n))

@app.route('/requests', strict_flashes=False)
def req():
    print(dict(request.headers))
    return jsonify(dict(request.headers))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

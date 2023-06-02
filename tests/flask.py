from flask import Flask, request, jsonify, render_template
app = Flask(__name__)

@app.route('/home')
def test():
	return "Hello, World!"
@app.route('/requests')
def req():
	return jsonify(dict(request.headers))
@app.route('/dict')
def dictionary():
	return jsonify(dict)
@app.route('/var/<num>')
def var(num):
	return num

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000, debug=True)


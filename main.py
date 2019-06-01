from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/calc")
def hello_world():
	operation = request.args.get('operation').replace(" ", "")
	if len(operation.replace(" ", "")) == 2:
		a = float(operation[0])
		b = float(operation[1])
		return jsonify(
			result=str(a+b)
		);
	else: 
		return jsonify(
			result=str(float(eval(operation)))
		)
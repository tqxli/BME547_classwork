# server.py
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def server_status():
    return "Server is on."

@app.route("/info", methods=["GET"])
def information():
    x = "The website will calculate blood cholesterol level. "
    x += "It is written by tl299"
    return x

@app.route("/hdl_check", methods=["POST"])
def hdl_check_from_internet():
    from interface import check_HDL
    in_data = request.get_json()
    hdl_value = in_data["hdl_value"]
    answer = check_HDL(hdl_value)
    return answer

@app.route("/add_numbers", methods=["POST"])
def add_numbers_from_internet():
    from my_math import add
    in_data = request.get_json()
    a, b = in_data["a"], in_data["b"]
    answer = add(a, b)
    return jsonify(answer)

if __name__ == "__main__":
    app.run()
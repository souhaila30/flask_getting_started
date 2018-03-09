from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/name", methods=["GET"])
def get_name():
    """
    Returns name when called as JSON
    """
    name = {
        "name": "Souhaila"
    }
    return jsonify(name), 200

@app.route("/hello/<name>", methods=["GET"])
def get_hello_name(name):
    """returns message with name """
    name = {
        "message": "Hello there, {0}".format(name)
    }

    return jsonify(name),200


@app.route("/distance", methods=["POST"])
def get_distance():
    """Returns the distance between two points"""
    r = request.get_json()
    a = r['a']
    b = r['b']
    s = (b[1] - a[1])^2 - (b[0] - a[0])^2

    data = {
        "distance": s,
        "a": r["a"],
        "b": r["b"]
    }
    return jsonify(data), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0")


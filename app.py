from flask import Flask, render_template, request, jsonify
from blind_solver import Blind_Solver

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/solve", methods=["POST"])
def solve():
    data = request.json
    if not data or "mode" not in data:
        return jsonify({"error": "mode missing"}), 400

    mode = data["mode"]

    solver = Blind_Solver(mode)
    output = solver.solve()

    return jsonify({"result": output})

if __name__ == "__main__":
    app.run(debug=True)
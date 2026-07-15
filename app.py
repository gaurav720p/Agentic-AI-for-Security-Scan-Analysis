from flask import Flask, render_template, request

from nmap_tool import run_nmap
from security_agent import analyze_scan

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/scan", methods=["POST"])
def scan():

    target = request.form["target"]

    # Run Nmap
    scan_result = run_nmap(target)

    # Send scan to Gemini
    ai_analysis = analyze_scan(scan_result)

    return render_template(
        "index.html",
        target=target,
        scan_result=scan_result,
        ai_analysis=ai_analysis
    )


if __name__ == "__main__":
    app.run(debug=True)
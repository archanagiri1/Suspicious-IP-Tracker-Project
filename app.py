from flask import Flask, render_template, request
from ip_logic import check_ip_malicious

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    results = []

    if request.method == "POST":
        ip_input = request.form.get("ips")

        if ip_input:
            ip_list = [ip.strip() for ip in ip_input.split(",")]

            for ip in ip_list:
                results.append(check_ip_malicious(ip))

    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)


from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Cloud-Native Student Portal</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: #eef2ff;
                text-align: center;
                padding: 60px 20px;
                margin: 0;
            }
            .card {
                background: white;
                max-width: 650px;
                margin: auto;
                padding: 35px;
                border-radius: 16px;
                box-shadow: 0 5px 20px #cbd5e1;
            }
            h1 { color: #1d4ed8; }
            .status { color: #15803d; font-weight: bold; }
            .pill {
                display: inline-block;
                background: #dbeafe;
                color: #1e40af;
                padding: 8px 12px;
                margin: 4px;
                border-radius: 20px;
            }
        </style>
    </head>
    <body>
        <main class="card">
            <h1>Cloud-Native Student Portal</h1>
            <p>Containerization and Deployment of a Cloud-Native Application</p>
            <p class="status">Application Status: Running</p>
            <h3>Technology Stack</h3>
            <span class="pill">Python Flask</span>
            <span class="pill">Docker</span>
            <span class="pill">Kubernetes</span>
            <p>This application is packaged in a Docker container and configured for Kubernetes deployment.</p>
            <p>Health endpoint: <code>/health</code></p>
        </main>
    </body>
    </html>
    """


@app.route("/health")
def health():
    return jsonify(status="healthy", application="cloud-native-student-portal")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

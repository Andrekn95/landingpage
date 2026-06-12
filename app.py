from flask import Flask, render_template_string
from datetime import datetime

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Reloj en Vivo</title>
    <style>
        body {
            margin: 0;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            background: radial-gradient(circle, #0f2027, #203a43, #2c5364);
            font-family: 'Arial', sans-serif;
            color: white;
            text-align: center;
        }

        .container {
            padding: 40px;
            border-radius: 20px;
            background: rgba(0,0,0,0.4);
            box-shadow: 0 0 30px rgba(0,255,255,0.2);
        }

        h1 {
            font-size: 2.5rem;
            margin-bottom: 20px;
            color: #00ffe5;
            text-shadow: 0 0 10px #00ffe5;
        }

        #clock {
            font-size: 3rem;
            letter-spacing: 2px;
            font-weight: bold;
            color: #ffffff;
            text-shadow: 0 0 15px #00ff99;
        }

        .date {
            margin-top: 15px;
            font-size: 1.3rem;
            color: #cceeff;
        }

        .pulse {
            animation: pulse 2s infinite;
        }

        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.05); }
            100% { transform: scale(1); }
        }
    </style>
</head>
<body>
    <div class="container pulse">
        <h1>⏰ Reloj en Tiempo Real</h1>
        <div id="clock">--:--:--</div>
        <div class="date" id="date"></div>
    </div>

<script>
function updateClock() {
    const now = new Date();

    const time = now.toLocaleTimeString('es-EC', {
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit'
    });

    const date = now.toLocaleDateString('es-EC', {
        weekday: 'long',
        year: 'numeric',
        month: 'long',
        day: 'numeric'
    });

    document.getElementById("clock").textContent = time;
    document.getElementById("date").textContent = date;
}

setInterval(updateClock, 1000);
updateClock();
</script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

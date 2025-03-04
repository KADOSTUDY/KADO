from flask import Flask, render_template

app = Flask(__name__)

# Ruta principal
@app.route('/')
def home():
    return render_template('index.html')  # Renderiza tu archivo HTML desde templates

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

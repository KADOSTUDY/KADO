from flask import Flask, send_from_directory

app = Flask(__name__)

# Ruta para servir el archivo HTML principal
@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

# Ruta para servir archivos estáticos (CSS, JS, imágenes, etc.)
@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('.', filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    



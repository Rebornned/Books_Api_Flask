from flask import Flask
from models import db
from config import Config
from routes import livros_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

# Configurando banco de dados ====================================================
with app.app_context():
    db.create_all()
# ===============================================================================

# Registrar rotas ***************************************************************
app.register_blueprint(livros_bp)

@app.route('/')
# ***************************************************************
def index():
    return "📚 Bem-vindo à API de Livros!"

if __name__ == '__main__':
    app.run(debug=True)

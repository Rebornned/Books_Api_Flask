from flask import Blueprint, request, jsonify
from models import db, Livro

livros_bp = Blueprint('livros', __name__)


# Rota para cadastrar um livro (POST /doar)
@livros_bp.route('/doar', methods=['POST'])
def doar_livro():
    data = request.get_json()
    if not all(key in data for key in ["titulo", "categoria", "autor", "imagem_url"]):
        return jsonify({"erro": "Todos os campos são obrigatórios"}), 400

    novo_livro = Livro(
        titulo=data['titulo'],
        categoria=data['categoria'],
        autor=data['autor'],
        imagem_url=data['imagem_url']
    )
    db.session.add(novo_livro)
    db.session.commit()

    return jsonify({"mensagem": "Livro cadastrado com sucesso!"}), 201
# ====================================================

# Rota para listar todos os livros (GET /livros)
@livros_bp.route('/livros', methods=['GET'])
def listar_livros():
    livros = Livro.query.all()
    return jsonify([{
        "id": livro.id,
        "titulo": livro.titulo,
        "categoria": livro.categoria,
        "autor": livro.autor,
        "imagem_url": livro.imagem_url
    } for livro in livros])
# ======================================================================
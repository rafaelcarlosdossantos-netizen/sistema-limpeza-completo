from flask import Blueprint, request, jsonify
from src.main import db
from src.models.cliente import Cliente

cliente_bp = Blueprint("cliente_bp", __name__)

@cliente_bp.route("/clientes", methods=["POST"])
def create_cliente():
    data = request.get_json()
    new_cliente = Cliente(nome=data["nome"], email=data["email"], telefone=data["telefone"], endereco=data["endereco"])
    db.session.add(new_cliente)
    db.session.commit()
    return jsonify({"message": "Cliente criado com sucesso!"}), 201

@cliente_bp.route("/clientes", methods=["GET"])
def get_clientes():
    clientes = Cliente.query.all()
    result = []
    for cliente in clientes:
        result.append({"id": cliente.id, "nome": cliente.nome, "email": cliente.email, "telefone": cliente.telefone, "endereco": cliente.endereco, "ativo": cliente.ativo})
    return jsonify(result), 200

@cliente_bp.route("/clientes/<int:id>", methods=["GET"])
def get_cliente(id):
    cliente = Cliente.query.get_or_404(id)
    return jsonify({"id": cliente.id, "nome": cliente.nome, "email": cliente.email, "telefone": cliente.telefone, "endereco": cliente.endereco, "ativo": cliente.ativo}), 200

@cliente_bp.route("/clientes/<int:id>", methods=["PUT"])
def update_cliente(id):
    cliente = Cliente.query.get_or_404(id)
    data = request.get_json()
    cliente.nome = data["nome"]
    cliente.email = data["email"]
    cliente.telefone = data["telefone"]
    cliente.endereco = data["endereco"]
    cliente.ativo = data["ativo"]
    db.session.commit()
    return jsonify({"message": "Cliente atualizado com sucesso!"}), 200

@cliente_bp.route("/clientes/<int:id>", methods=["DELETE"])
def delete_cliente(id):
    cliente = Cliente.query.get_or_404(id)
    db.session.delete(cliente)
    db.session.commit()
    return jsonify({"message": "Cliente deletado com sucesso!"}), 200



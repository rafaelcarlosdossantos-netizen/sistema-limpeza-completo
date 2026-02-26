from flask import Blueprint, request, jsonify
from src.main import db
from src.models.orcamento import Orcamento

orcamento_bp = Blueprint("orcamento_bp", __name__)

@orcamento_bp.route("/orcamentos", methods=["POST"])
def create_orcamento():
    data = request.get_json()
    new_orcamento = Orcamento(
        cliente_id=data["cliente_id"],
        servico_id=data["servico_id"],
        data_validade=data["data_validade"],
        valor_total=data["valor_total"],
        status=data.get("status", "pendente"),
        descricao=data.get("descricao")
    )
    db.session.add(new_orcamento)
    db.session.commit()
    return jsonify({"message": "Orçamento criado com sucesso!"}), 201

@orcamento_bp.route("/orcamentos", methods=["GET"])
def get_orcamentos():
    orcamentos = Orcamento.query.all()
    result = []
    for orc in orcamentos:
        result.append({
            "id": orc.id,
            "cliente_id": orc.cliente_id,
            "servico_id": orc.servico_id,
            "data_criacao": str(orc.data_criacao),
            "data_validade": str(orc.data_validade),
            "valor_total": orc.valor_total,
            "status": orc.status,
            "descricao": orc.descricao
        })
    return jsonify(result), 200

@orcamento_bp.route("/orcamentos/<int:id>", methods=["GET"])
def get_orcamento(id):
    orc = Orcamento.query.get_or_404(id)
    return jsonify({
        "id": orc.id,
        "cliente_id": orc.cliente_id,
        "servico_id": orc.servico_id,
        "data_criacao": str(orc.data_criacao),
        "data_validade": str(orc.data_validade),
        "valor_total": orc.valor_total,
        "status": orc.status,
        "descricao": orc.descricao
    }), 200

@orcamento_bp.route("/orcamentos/<int:id>", methods=["PUT"])
def update_orcamento(id):
    orc = Orcamento.query.get_or_404(id)
    data = request.get_json()
    orc.cliente_id = data["cliente_id"]
    orc.servico_id = data["servico_id"]
    orc.data_validade = data["data_validade"]
    orc.valor_total = data["valor_total"]
    orc.status = data.get("status", orc.status)
    orc.descricao = data.get("descricao")
    db.session.commit()
    return jsonify({"message": "Orçamento atualizado com sucesso!"}), 200

@orcamento_bp.route("/orcamentos/<int:id>", methods=["DELETE"])
def delete_orcamento(id):
    orc = Orcamento.query.get_or_404(id)
    db.session.delete(orc)
    db.session.commit()
    return jsonify({"message": "Orçamento deletado com sucesso!"}), 200



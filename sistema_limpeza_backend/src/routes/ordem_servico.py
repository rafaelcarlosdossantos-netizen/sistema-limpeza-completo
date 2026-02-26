from flask import Blueprint, request, jsonify
from src.main import db
from src.models.ordem_servico import OrdemServico

ordem_servico_bp = Blueprint("ordem_servico_bp", __name__)

@ordem_servico_bp.route("/ordens_servico", methods=["POST"])
def create_ordem_servico():
    data = request.get_json()
    new_ordem_servico = OrdemServico(
        cliente_id=data["cliente_id"],
        operador_id=data.get("operador_id"),
        servico_id=data["servico_id"],
        data_agendada=data["data_agendada"],
        hora_inicio=data["hora_inicio"],
        status=data.get("status", "pendente"),
        endereco_servico=data["endereco_servico"],
        observacoes=data.get("observacoes")
    )
    db.session.add(new_ordem_servico)
    db.session.commit()
    return jsonify({"message": "Ordem de Serviço criada com sucesso!"}), 201

@ordem_servico_bp.route("/ordens_servico", methods=["GET"])
def get_ordens_servico():
    ordens_servico = OrdemServico.query.all()
    result = []
    for os in ordens_servico:
        result.append({
            "id": os.id,
            "cliente_id": os.cliente_id,
            "operador_id": os.operador_id,
            "servico_id": os.servico_id,
            "data_agendada": str(os.data_agendada),
            "hora_inicio": str(os.hora_inicio),
            "status": os.status,
            "endereco_servico": os.endereco_servico,
            "observacoes": os.observacoes,
            "data_criacao": str(os.data_criacao),
            "data_atualizacao": str(os.data_atualizacao)
        })
    return jsonify(result), 200

@ordem_servico_bp.route("/ordens_servico/<int:id>", methods=["GET"])
def get_ordem_servico(id):
    os = OrdemServico.query.get_or_404(id)
    return jsonify({
        "id": os.id,
        "cliente_id": os.cliente_id,
        "operador_id": os.operador_id,
        "servico_id": os.servico_id,
        "data_agendada": str(os.data_agendada),
        "hora_inicio": str(os.hora_inicio),
        "status": os.status,
        "endereco_servico": os.endereco_servico,
        "observacoes": os.observacoes,
        "data_criacao": str(os.data_criacao),
        "data_atualizacao": str(os.data_atualizacao)
    }), 200

@ordem_servico_bp.route("/ordens_servico/<int:id>", methods=["PUT"])
def update_ordem_servico(id):
    os = OrdemServico.query.get_or_404(id)
    data = request.get_json()
    os.cliente_id = data["cliente_id"]
    os.operador_id = data.get("operador_id")
    os.servico_id = data["servico_id"]
    os.data_agendada = data["data_agendada"]
    os.hora_inicio = data["hora_inicio"]
    os.status = data.get("status", os.status)
    os.endereco_servico = data["endereco_servico"]
    os.observacoes = data.get("observacoes")
    db.session.commit()
    return jsonify({"message": "Ordem de Serviço atualizada com sucesso!"}), 200

@ordem_servico_bp.route("/ordens_servico/<int:id>", methods=["DELETE"])
def delete_ordem_servico(id):
    os = OrdemServico.query.get_or_404(id)
    db.session.delete(os)
    db.session.commit()
    return jsonify({"message": "Ordem de Serviço deletada com sucesso!"}), 200



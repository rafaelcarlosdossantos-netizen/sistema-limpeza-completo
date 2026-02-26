#!/usr/bin/env python3
"""
Script de configuração inicial do banco de dados para o Sistema de Gestão de Limpeza.

Este script cria as tabelas necessárias e insere dados iniciais no banco de dados.
"""

import os
import sys
from datetime import datetime
from werkzeug.security import generate_password_hash

# Adiciona o diretório src ao path para importar os módulos
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from main import create_app, db
from models.user import User
from models.cliente import Cliente
from models.operador import Operador
from models.servico import Servico


def create_initial_data():
    """Cria dados iniciais para o sistema."""
    
    # Criar usuário administrador padrão
    admin_user = User.query.filter_by(email='admin@sistema.com').first()
    if not admin_user:
        admin_user = User(
            nome='Administrador',
            email='admin@sistema.com',
            senha=generate_password_hash('admin123'),
            tipo='admin',
            ativo=True
        )
        db.session.add(admin_user)
        print("✓ Usuário administrador criado (email: admin@sistema.com, senha: admin123)")
    
    # Criar serviços padrão
    servicos_padrao = [
        {
            'nome': 'Limpeza Residencial Básica',
            'descricao': 'Limpeza geral de apartamentos e casas',
            'preco_base': 80.00,
            'tempo_estimado': 120,
            'categoria': 'residencial'
        },
        {
            'nome': 'Limpeza Residencial Completa',
            'descricao': 'Limpeza completa incluindo vidros e enceramento',
            'preco_base': 150.00,
            'tempo_estimado': 240,
            'categoria': 'residencial'
        },
        {
            'nome': 'Limpeza de Condomínio',
            'descricao': 'Limpeza de áreas comuns de condomínios',
            'preco_base': 300.00,
            'tempo_estimado': 360,
            'categoria': 'condominio'
        },
        {
            'nome': 'Limpeza de Garagem',
            'descricao': 'Limpeza e organização de garagens',
            'preco_base': 100.00,
            'tempo_estimado': 180,
            'categoria': 'garagem'
        },
        {
            'nome': 'Coleta de Lixo',
            'descricao': 'Serviço de coleta e descarte de lixo',
            'preco_base': 50.00,
            'tempo_estimado': 60,
            'categoria': 'coleta'
        },
        {
            'nome': 'Remoção de Móveis',
            'descricao': 'Remoção e descarte de móveis usados',
            'preco_base': 200.00,
            'tempo_estimado': 240,
            'categoria': 'remocao'
        }
    ]
    
    for servico_data in servicos_padrao:
        servico_existente = Servico.query.filter_by(nome=servico_data['nome']).first()
        if not servico_existente:
            servico = Servico(**servico_data)
            db.session.add(servico)
            print(f"✓ Serviço criado: {servico_data['nome']}")
    
    # Criar operador exemplo
    operador_exemplo = Operador.query.filter_by(email='operador@exemplo.com').first()
    if not operador_exemplo:
        operador_exemplo = Operador(
            nome='João Silva',
            email='operador@exemplo.com',
            telefone='(11) 99999-9999',
            especialidades='Limpeza residencial, Limpeza de condomínio',
            ativo=True
        )
        db.session.add(operador_exemplo)
        print("✓ Operador exemplo criado")
    
    # Criar cliente exemplo
    cliente_exemplo = Cliente.query.filter_by(email='cliente@exemplo.com').first()
    if not cliente_exemplo:
        cliente_exemplo = Cliente(
            nome='Maria Santos',
            email='cliente@exemplo.com',
            telefone='(11) 88888-8888',
            endereco='Rua das Flores, 123',
            cidade='São Paulo',
            estado='SP',
            cep='01234-567',
            ativo=True
        )
        db.session.add(cliente_exemplo)
        print("✓ Cliente exemplo criado")
    
    # Salvar todas as alterações
    try:
        db.session.commit()
        print("\n✅ Dados iniciais criados com sucesso!")
        print("\nInformações de acesso:")
        print("- Email do administrador: admin@sistema.com")
        print("- Senha do administrador: admin123")
        print("\n⚠️  IMPORTANTE: Altere a senha do administrador após o primeiro login!")
        
    except Exception as e:
        db.session.rollback()
        print(f"\n❌ Erro ao criar dados iniciais: {str(e)}")
        return False
    
    return True


def main():
    """Função principal do script."""
    print("🚀 Iniciando configuração do banco de dados...")
    
    # Criar aplicação Flask
    app = create_app()
    
    with app.app_context():
        try:
            # Criar todas as tabelas
            print("📋 Criando tabelas do banco de dados...")
            db.create_all()
            print("✓ Tabelas criadas com sucesso!")
            
            # Criar dados iniciais
            print("\n📝 Inserindo dados iniciais...")
            if create_initial_data():
                print("\n🎉 Configuração do banco de dados concluída com sucesso!")
                return True
            else:
                print("\n❌ Falha na configuração do banco de dados.")
                return False
                
        except Exception as e:
            print(f"\n❌ Erro durante a configuração: {str(e)}")
            return False


if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)

"""Extensão do Flask:

Este tipo de arquivo aqui chama-se extensão do flask,
Que vem a ser um módulo com classe, função ou qualquer coisa 
dentro desde que seja callable (invocável)
"""
from flask import render_template


def init_app(app):
    """Inicialização de extensões"""
    @app.route("/")
    def index():
        return "Hello pai!"

    @app.route("/sobre")
    def super():
        return render_template('ola.html')

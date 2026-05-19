from flask import Blueprint, render_template, request, redirect
from app import db
from app.models.paciente import Paciente

paciente_bp = Blueprint('paciente', __name__)

@paciente_bp.route('/pacientes')

def pacientes():

    lista_pacientes = Paciente.query.all()

    return render_template(
        'pacientes.html',
        pacientes=lista_pacientes
    )

@paciente_bp.route('/agregar_paciente', methods=['POST'])

def agregar_paciente():

    nuevo = Paciente(
        nombre=request.form['nombre'],
        edad=request.form['edad'],
        direccion=request.form['direccion'],
        telefono=request.form['telefono']
    )

    db.session.add(nuevo)
    db.session.commit()

    return redirect('/pacientes')

@paciente_bp.route('/eliminar_paciente/<int:id>')

def eliminar_paciente(id):

    paciente = Paciente.query.get(id)

    db.session.delete(paciente)
    db.session.commit()

    return redirect('/pacientes')
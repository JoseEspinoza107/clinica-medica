from flask import Blueprint, render_template, request, redirect
from app import db

from app.models.consulta import Consulta
from app.models.medico import Medico
from app.models.paciente import Paciente

consulta_bp = Blueprint('consulta', __name__)

@consulta_bp.route('/consultas')

def consultas():

    lista_consultas = Consulta.query.all()

    medicos = Medico.query.all()

    pacientes = Paciente.query.all()

    return render_template(
        'consultas.html',
        consultas=lista_consultas,
        medicos=medicos,
        pacientes=pacientes
    )

@consulta_bp.route('/agregar_consulta', methods=['POST'])

def agregar_consulta():

    nueva = Consulta(
        fecha=request.form['fecha'],
        diagnostico=request.form['diagnostico'],
        tratamiento=request.form['tratamiento'],
        id_medico=request.form['id_medico'],
        id_paciente=request.form['id_paciente']
    )

    db.session.add(nueva)
    db.session.commit()

    return redirect('/consultas')

@consulta_bp.route('/eliminar_consulta/<int:id>')

def eliminar_consulta(id):

    consulta = Consulta.query.get(id)

    db.session.delete(consulta)
    db.session.commit()

    return redirect('/consultas')
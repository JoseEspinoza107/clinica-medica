from flask import Blueprint, render_template, request, redirect
from app import db
from app.models.medico import Medico

medico_bp = Blueprint('medico', __name__)

@medico_bp.route('/')

def inicio():
    return render_template('index.html')

@medico_bp.route('/medicos')

def medicos():

    lista_medicos = Medico.query.all()

    return render_template(
        'medicos.html',
        medicos=lista_medicos
    )

@medico_bp.route('/agregar_medico', methods=['POST'])

def agregar_medico():

    nuevo = Medico(
        nombre=request.form['nombre'],
        especialidad=request.form['especialidad'],
        telefono=request.form['telefono'],
        correo=request.form['correo']
    )

    db.session.add(nuevo)
    db.session.commit()

    return redirect('/medicos')

@medico_bp.route('/eliminar_medico/<int:id>')

def eliminar_medico(id):

    medico = Medico.query.get(id)

    db.session.delete(medico)
    db.session.commit()

    return redirect('/medicos')
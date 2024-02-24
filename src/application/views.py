from flask import render_template, request, redirect, flash
from pylastic.elater.renderer.functions import ElasticFunction
from pylastic.handler.exceptions import TensorNotFound

from services.analyze import AnalyzeService
from .app import app

service = AnalyzeService()


@app.get('/')
def index():
    return render_template("index.html", functions=[func for func in ElasticFunction])


@app.post('/')
def process():
    if 'file' not in request.files or not request.files['file'].filename:
        flash('Please upload file')
        return redirect(request.url)
    file = request.files['file']
    match request.form['action']:
        case '1':
            try:
                return service.process_analyze(file.stream.read(), title=file.filename)
            except TensorNotFound as exception:
                flash('Tensor not found')
        case '2':
            try:
                return service.process_surface(file.stream.read(), ElasticFunction.by_name(request.form['function']))
            except TensorNotFound as exception:
                flash('Tensor not found')
            except ValueError as exception:
                flash(str(exception))
        case '3':
            try:
                return service.process_projections(file.stream.read(), ElasticFunction.by_name(request.form['function']))
            except TensorNotFound as exception:
                flash('Tensor not found')
            except ValueError as exception:
                flash(str(exception))
        case _:
            flash('Wrong action')
            return redirect(request.url)
    return render_template("index.html", functions=[func for func in ElasticFunction])

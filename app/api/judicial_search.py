from flask import Blueprint, request, jsonify
from app.services.judicial_api_service import JudicialAPIService

# Crear el Blueprint
judicial_bp = Blueprint('judicial', __name__)
service = JudicialAPIService()  # Instancia del servicio JudicialAPIService

@judicial_bp.route('/consulta_nombre', methods=['GET'])
def consulta_por_nombre():
    """
    Endpoint para consultar procesos por nombre.
    """
    nombre = request.args.get('nombre')  # Obligatorio
    tipo_persona = request.args.get('tipoPersona', 'jur')  # Opcional, valor por defecto 'jur'
    codificacion_despacho = request.args.get('codificacionDespacho')  # Opcional
    pagina = int(request.args.get('pagina', 1))  # Opcional, valor por defecto 1
    solo_activos = request.args.get('soloActivos', 'true').lower() == 'true'  # Opcional, valor por defecto True

    # Validar que el parámetro obligatorio 'nombre' esté presente
    if not nombre:
        return jsonify({'error': 'El parámetro "nombre" es obligatorio'}), 400

    try:
        # Llamar al servicio para realizar la consulta
        response = service.consulta_por_nombre(
            nombre=nombre,
            tipo_persona=tipo_persona,
            codificacion_despacho=codificacion_despacho,
            pagina=pagina,
            solo_activos=solo_activos
        )
        return jsonify(response)  # Devolver la respuesta de la API
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@judicial_bp.route('/consulta_radicado', methods=['GET'])
def consulta_por_radicado():
    """
    Endpoint para consultar procesos por número de radicado.
    """
    numero = request.args.get('numero')  # Obligatorio
    pagina = int(request.args.get('pagina', 1))  # Opcional, valor por defecto 1
    solo_activos = request.args.get('soloActivos', 'false').lower() == 'true'  # Opcional, valor por defecto False

    # Validar que el número de radicado esté presente
    if not numero:
        return jsonify({'error': 'El parámetro "numero" es obligatorio'}), 400

    try:
        # Llamar al servicio para realizar la consulta
        response = service.consulta_por_radicado(
            numero=numero,
            pagina=pagina,
            solo_activos=solo_activos
        )
        return jsonify(response)  # Devolver la respuesta de la API
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@judicial_bp.route('/detalle_proceso', methods=['GET'])
def consulta_detalle_proceso():
    """
    Endpoint para consultar el detalle de un proceso.
    """
    id_proceso = request.args.get('idProceso')  # Obligatorio

    # Validar que el ID del proceso esté presente
    if not id_proceso:
        return jsonify({'error': 'El parámetro "idProceso" es obligatorio'}), 400

    try:
        # Llamar al servicio para obtener el detalle del proceso
        response = service.consulta_detalle_proceso(id_proceso)
        return jsonify(response)  # Devolver la respuesta de la API
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@judicial_bp.route('/actuaciones', methods=['GET'])
def consulta_actuaciones_proceso():
    """
    Endpoint para consultar las actuaciones de un proceso.
    """
    id_proceso = request.args.get('idProceso')  # Obligatorio

    # Validar que el ID del proceso esté presente
    if not id_proceso:
        return jsonify({'error': 'El parámetro "idProceso" es obligatorio'}), 400

    try:
        # Llamar al servicio para obtener las actuaciones del proceso
        response = service.consulta_actuaciones_proceso(id_proceso)
        return jsonify(response)  # Devolver la respuesta de la API
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@judicial_bp.route('/documentos_actuacion', methods=['GET'])
def consulta_documentos_actuacion():
    """
    Endpoint para consultar los documentos de una actuación.
    """
    id_reg_actuacion = request.args.get('idRegActuacion')  # Obligatorio

    # Validar que el ID de la actuación esté presente
    if not id_reg_actuacion:
        return jsonify({'error': 'El parámetro "idRegActuacion" es obligatorio'}), 400

    try:
        # Llamar al servicio para obtener los documentos de la actuación
        response = service.consulta_documentos_actuacion(id_reg_actuacion)
        return jsonify(response)  # Devolver la respuesta de la API
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@judicial_bp.route('/descarga_documento', methods=['GET'])
def descarga_documento():
    """
    Endpoint para descargar un documento.
    """
    id_reg_documento = request.args.get('idRegDocumento')  # Obligatorio

    # Validar que el ID del documento esté presente
    if not id_reg_documento:
        return jsonify({'error': 'El parámetro "idRegDocumento" es obligatorio'}), 400

    try:
        # Llamar al servicio para descargar el documento
        response = service.descarga_documento(id_reg_documento)
        return response, 200, {
            'Content-Disposition': f'attachment; filename=documento_{id_reg_documento}.pdf',
            'Content-Type': 'application/pdf'
        }
    except Exception as e:
        return jsonify({'error': str(e)}), 500
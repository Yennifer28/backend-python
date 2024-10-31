from flask import  jsonify, request
from services.empleado_service import EmpleadoService

class EmpleadoController:
    @staticmethod
    def get_all():
        empleados = EmpleadoService.get_all()
        return jsonify(empleados)
    
    @staticmethod
    def get_by_id(empleado_id):
        empleado = EmpleadoService.get_by_id(empleado.id)
        return jsonify(empleado)
    
    @staticmethod
    def create_empleado():
        data = request.get_json()
        response = EmpleadoService.create_empleado(data)
        return jsonify(response)
    
#borrar y actualizar
    @staticmethod
    def delete_empleado(empleado_id):
            response = EmpleadoService.delete_empleado(empleado_id)
            return jsonify(response)
            
    @staticmethod
    def update_empleado(empleado_id):
        data = request.get_json()
        response = EmpleadoService.update_empleado(empleado_id, data)
        return jsonify(response)

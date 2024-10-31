from repositories.empleado_repository import EmpleadoRepository
from utils.encryption_util import encrypt_password
from utils.token_util import generate_token 

class EmpleadoService:
    @staticmethod
    def get_all():
        return EmpleadoRepository.get_all()
    
    @staticmethod
    def create_empleado(data):
        if EmpleadoRepository.get_by_user(data['usuario']):
            return { "error": "usuario ya existe" }
                    
        data['password'] = encrypt_password(data['password'])
        EmpleadoRepository.create_empleado(data)
        token = generate_token(data['usuario'])
        return {
            "menssage": "empleado registrado",
            "token": token
        }
        
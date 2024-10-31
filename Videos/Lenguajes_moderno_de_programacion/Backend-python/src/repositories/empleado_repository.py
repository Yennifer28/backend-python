import firebase_admin 
from firebase_admin import credentials, firestore
from models.empleado_model import Empleado

cred = credentials.Certificate("RUTA")
firebase_admin.initialize_app(cred)
db = firestore.client()
coll = 'empleados_python'

class EmpleadoRepository:
    @staticmethod
    def get_all():
        empleados = db.collection(coll)
        return [doc.to_dict() for doc in empleados.stream()]
    
    @staticmethod
    def create_empleado(data):
        db.collection(coll).add(data)
    
    @staticmethod
    def get_by_user(username):
        docs = db.collection(coll).where("usuario", "==", username).stream()
        for doc in docs :
            return Empleado.from_dict(doc.to_dict())
        return None #null y no existe 
    
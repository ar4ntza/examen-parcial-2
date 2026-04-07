# Examen Parcial 2

**Nombre:** Arantza García Vázquez
**Materia:** Administración de Bases de Datos  
**Tecnologías:** FastAPI · MySQL · MongoDB 

---

## Estructura del proyecto


parcial2/
├── routes/
│   ├── __init__.py
│   ├── usuario.py       # POST /usuarios  · GET /usuarios
│   ├── pedido.py        # POST /pedidos   (transacción explícita)
│   ├── evento.py        # POST /eventos   · GET /eventos/analisis
│   └── dashboard.py     # GET  /dashboard/resumen
├── database.py          # Conexiones MySQL y MongoDB Atlas
├── models.py            # Esquemas Pydantic
├── main.py              # App FastAPI + startup automático
└── requirements.txt


---
## Instalación

```bash
# Crear entorno virtual
python -m venv parcial2
parcial2\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar servidor
uvicorn main:app --reload

Swagger disponible en: http://localhost:8000/docs 

Tecnologías
FastAPI → API REST
MySQL → Datos transaccionales
MongoDB Atlas → Eventos y análisis
Pydantic → Validación de datos
Base de datos
MySQL (ecommerce_db)
usuarios
pedidos
pagos
MongoDB (ecommerce_logs)

Colección: eventos_usuario

{
  "usuario_id": 1,
  "evento": "string",
  "fecha": "ISODate",
  "dispositivo": "web | mobile",
  "producto_id": 1
}
Endpoints
POST /usuarios

Crear usuario

{
  "nombre": "sam",
  "email": "sam@cortes.com"
}
POST /pedidos

Crear pedido con transacción

{
  "usuario_id": 1,
  "total": 1500
}
Aplica 10% de descuento si total > 1000
Inserta pedido y pago en una sola transacción
Si ocurre un error → rollback completo
POST /eventos

Registrar evento en MongoDB

{
  "usuario_id": 1,
  "evento": "click_producto",
  "fecha": "2025-06-01T10:30:00",
  "dispositivo": "web",
  "producto_id": 42
}
GET /eventos/analisis

Obtiene el evento más frecuente y total de eventos

GET /dashboard/resumen

Resumen general del sistema

{
  "ventas": {
    "total_ventas": 1500,
    "promedio_descuento": 150
  },
  "eventos": {
    "evento_mas_frecuente": "click_producto",
    "total_eventos": 3
  }
}
Notas
MySQL maneja transacciones y consistencia
MongoDB permite análisis flexible
Se utiliza una arquitectura híbrida (SQL + NoSQL)
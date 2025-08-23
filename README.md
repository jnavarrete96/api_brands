# Brands API

API RESTful para gestionar marcas y titulares, construida con Django 5.2.5 y Django REST Framework.

**Versión de Python utilizada:** 3.13.7

---

## 🚀 Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/tu-usuario/tu-repo.git
cd tu-repo
```
2. Crea y activa un entorno virtual:

```bash
python -m venv venv
source venv/bin/activate        # Linux/macOS
venv\Scripts\activate           # Windows
```
3. Instala las dependencias:

```bash
pip install -r requirements.txt
```
4. Configura la base de datos en settings.py o usando variables de entorno.

5. Ejecuta migraciones:

```bash
python manage.py migrate
```
6. Inicia el servidor:
```bash
python manage.py runserver
```

---

## 📘 Documentación

Accede a la documentación Swagger en:

[http://localhost:8000/api/docs/](http://localhost:8000/api/docs/)

También disponible en formato Redoc:

[http://localhost:8000/api/redoc/](http://localhost:8000/api/redoc/)

---

## 🧪 Pruebas

Ejecuta las pruebas unitarias con:

```bash
python manage.py test brands
```

---

## 📦 Requisitos clave

- **Python**: 3.13.7  
- **Django**: 5.2.5  
- **Django REST Framework**: 3.16.1  
- **drf-spectacular**: 0.28.0  
- **mysqlclient**: 2.2.7

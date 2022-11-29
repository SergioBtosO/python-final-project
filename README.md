# Python Final Project: Orders App
Proyecto final del curso de python de CoderHouse

## Equipo
- Juan David Echeverry Fernández
- Sergio Barrientos Ossa

# Instrucciones para ejecutar este proyecto

- Crear Directorio del proyecto orders_manager

### 1. Abrir Git Bash para `Windows` o una terminal para `Linux/Unix`.

### 2. Crear directorio de trabajo para el proyecto 
```bash
cd
mkdir -p Documents/orders_manager
cd Documents/orders_manager
ls 
```

- Clonar el proyecto 
```bash
git clone 


### 3. Crear y activar entorno virtual
(Windows)
```bash
python -m venv venv
.\venv\Scripts\activate
```

(Linux)
```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Instalar las dependencias del proyecto
```bash
pip install -r requirements.txt
```

### 5. Navegamos hacia la carpeta del proyecto `orders_manager`
```bash
cd orders_manager
```

### 6. Se crean las migraciones que son una "plantilla" para crear la base de datos con la que trabajará nuestro proyecto de Django
```bash
python manage.py makemigrations
```

### 7. Se ejecuta la migración para crear la base de datos con la que trabajará nuestro proyecto de Django
```bash
python manage.py migrate
```

### 8. Se crea el super usuario para nuestro proyecto de Django, **Solo si no se ha creado**
```bash
python manage.py createsuperuser
```
Ingrese `Username`, `Email address` y `Password` 

### 9. Se levanta el servidor de Django que expone el servicio por el localhost en el puerto 8000 por defecto `http://127.0.0.1:8000/`
```bash
python manage.py runserver
```

 
### 10. una vez creado el super usuario se puede ingresar como administrador para tener acceso a las configuraciones de los maestros: 
categorias, puntuaciones y estados.



1. Creamos un venv 

2. Seleccinar el venv creado

3. Instalamos dependencias. pip install python-dotenv
  python-dotenv:   Se utiliza para cargar variables de entorno desde archivos .env en aplicaciones Python. 
                    Esto es útil para separar la configuración de la aplicación del código fuente, lo que proporciona flexibilidad y seguridad al manejar datos sensibles o variables de configuración que pueden variar según el entorno (desarrollo, pruebas, producción, etc.).

creamos un archivo .env donde establecemos el usuario y contraseña de nuestra aplicacion

4. configuramos nuestra cuenta de gmail para que nos permita hacer envios de correos desde esta.

a. entramos a la cuenta.
b. seleccionamos: gestionar nuestra cuenta de google
c. habilitamos la autenticaion de do spasos--> seguridad--> autentificacion dos pasos
generamos una contraseña de aplicacion

5. completamos el archivo .env (no se sube a github)

6. Creamos el sctript python envio_correo.py, realizamos importaciones
smtplib --> representa un conexion con el servidor de correo smtp (gmail)
os --> para simular la extaccion de datos de varaibles de entorno
from dotenv import load_dotenv

from email.mime.multipart import MIMEMultipart --> permite que el correo este compuesto de varias partes (img, html,adjuntos,etc) para unirse posteriomente (estructura)

from email.mime.text import MIMEText --> para html

cargamos las variables de entorno --> load_dotenv()

accedemos a la variable con remiente = os.getenv('USER')
establecemos el destinatario



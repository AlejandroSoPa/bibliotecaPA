from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseForbidden, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .forms import *
from .models import *
from .utils import generarLog, subir_logs_a_bd
from django.conf import settings
import random
import string
import csv
from datetime import datetime
from django.utils import timezone


# Create your views here.

def login_view(request):
    data = {}
    if request.method == "POST":
        username = request.POST.get("username").lower()
        password = request.POST.get("password")

        try:
            user = Usuari.objects.get(email=username)
            if check_password(password, user.password):
                generarLog(request, 'INFO', f"Inicio de sesión exitoso", ruta='/index', usuario=user)
                subir_logs_a_bd(request)

                login(request, user)
                return redirect("dashboard")
		# data['info'] = True
                # data['errorMsg'] = "Inicio de sesion correcto, redireccionando..."
            else:
                generarLog(request, 'WARNING', f"Contraseñas incorrectas: Intento de inicio de sesión fallido - Contraseña incorrecta", ruta='/index', usuario=None)
                subir_logs_a_bd(request)
                data['warning'] = True
                data['errorMsg'] = "El correo electrónico o la contraseña son incorrectos."

        except Usuari.DoesNotExist:
            generarLog(request, 'WARNING', f"Usuari.DoesNotExist: Intento de inicio de sesión fallido - Usuario no encontrado", ruta='/index', usuario=None)
            subir_logs_a_bd(request)
            data['warning'] = True
            data['errorMsg'] = "El correo electrónico o la contraseña son incorrectos."

    return render(request, "index.html", data)

def index(request):
    return render(request, 'index.html')

def search(request):
    return render(request, 'search.html')

def manage_users(request):
    return render(request, 'manage_users.html')

def create_user(request):
    return render(request, 'create_user.html')

def import_users(request):
    return render(request, 'import_users.html')

def dashboard(request):
    print(request.user)
    if not request.user.is_authenticated:
        generarLog(request, 'ERROR', f"Ha fallado la redirección a la página de dashboard", ruta='/dashboard', usuario=None)
        subir_logs_a_bd(request)
        return redirect('index')
    generarLog(request, 'INFO', f"Inicio de sesión exitoso", ruta='/dashboard', usuario=request.user)
    subir_logs_a_bd(request)
    return render(request, 'dashboard.html', {'user':request.user})

@login_required
def logout_view(request):
    generarLog(request, 'INFO', f"Cierre de sesión exitoso", ruta='/dashboard', usuario=request.user)
    logout(request)
    return redirect("index")

def password_reset_request(request):
    if request.method == "POST":
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user = Usuari.objects.filter(email=email).first()
            if user:
                uid = urlsafe_base64_encode(str(user.pk).encode())
                token = default_token_generator.make_token(user)
                reset_link = ('/reset-password/{}/{}'.format(uid, token))
                subject = 'Password Reset Request'
                message = render_to_string('reset_password_email.html', {
                    'reset_link': reset_link,
                })
                send_mail(subject, message, settings.EMAIL_HOST_USER, [email])
                generarLog(request, 'ERROR', f"Ha fallado la redirección a la página de dashboard", ruta='/dashboard', usuario=None)
                subir_logs_a_bd(request)
                return redirect('password_reset_done')
            else:
                messages.error(request, 'No user with that email address.')
    else:
        form = PasswordResetForm()
    return render(request, 'password_reset_request.html', {'form': form})

def password_reset_confirm(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Usuari.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, Usuari.DoesNotExist):
        user = None

    if user and default_token_generator.check_token(user, token):
        if request.method == "POST":
            password = request.POST.get('password')
            user.set_password(password)
            user.save()
            messages.success(request, 'Password has been reset successfully.')
            return redirect('dashboard')
        return render(request, 'password_reset_confirm.html')
    else:
        messages.error(request, 'Invalid password reset link.')
        return redirect('dashboard')    

@login_required
def change_password(request):
    data = {}
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            data['info'] = True
            data['infoMsg'] = "La contrasenya s'ha canviat correctament."
            return redirect('change_password')
        else:
            data['warning'] = True
            data['infoMsg'] = "No s'ha pogut canviar la contrasenya."
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form})


@login_required
def edit_profile(request, user_id):
    data = {}
    user_to_edit = get_object_or_404(Usuari, id=user_id)
    
    if not (request.user.id == user_id or request.user.centre.id == user_to_edit.centre.id):
        return HttpResponseForbidden("You are not allowed to edit this profile.")
    
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, request.FILES, instance=user_to_edit)
        if form.is_valid():
            form.save()
            data['info'] = True
            data['infoMsg'] = "Usuari editat correctament."
            if user_to_edit:
                return redirect('manage_users')
            else:
                return redirect('dashboard')
    else:
        form = CustomUserChangeForm(instance=user_to_edit)
    
    return render(request, 'edit_profile.html', {'form': form})

def generate_random_password():
    # Define los requisitos para la contraseña
    length = random.randint(8, 16)  # Longitud aleatoria entre 8 y 16 caracteres
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special_chars = '@#$%&*!'  # Puedes ajustar esto según tus necesidades
    
    # Genera una contraseña aleatoria
    password = ''.join(random.choices(uppercase + lowercase + digits + special_chars, k=length))
    
    # Asegúrate de que la contraseña cumpla con los criterios
    while not (any(char in uppercase for char in password) and
               any(char in lowercase for char in password) and
               any(char in digits for char in password)):
        password = ''.join(random.choices(uppercase + lowercase + digits + special_chars, k=length))
    
    return password


def create_user(request):
    data = {}
    if request.method == 'POST':
        form = CustomCreateUserForm(request.POST)
        if form.is_valid():
            # Generar una contraseña aleatoria
            password = generate_random_password()
            # Establecer la contraseña en el formulario
            form.instance.set_password(password)
            user = form.save(commit=False)
            # Guardar el usuario
            user.save()
            # Enviar la contraseña por correo electrónico
            send_mail(
                'Compte a biblio7 creat correctament',
                f"Hola,\n\nEl teu compte ha sigut creat correctament. La teva contrasenya és: {password}\nUs recomanem canviar la contrasenya\n\nPots iniciar sessió pulsant el següent enllaç: <a href='http://127.0.0.1:8000/'>Iniciar sessió</a>.\nL'equip de la biblioteca.\n\n",
                settings.EMAIL_HOST_USER,
                [form.cleaned_data['email']],
                fail_silently=False,
            )
            data['info'] = True
            data['infoMsg'] = "Usuari creat correctament."
            return redirect('manage_users')
    else:
        # Verificar si el usuario está autenticado
        if request.user.is_authenticated:
            # Obtener el centro asociado al usuario logeado
            centro = request.user.centre
            # Crear una instancia del formulario pasando el centro como argumento
            form = CustomCreateUserForm(centre=centro)
        else:
            # Si el usuario no está autenticado, redirigirlo a la página de inicio de sesión
            return redirect('login')
    
    return render(request, 'create_user.html', {'form': form})



def import_users(request):
    data = {}
    feedback_messages = []  # Lista para almacenar los mensajes de retroalimentación

    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            archivo_csv = request.FILES['archivo_csv']

            decoded_file = archivo_csv.read().decode('utf-8').splitlines()
            lector_csv = csv.DictReader(decoded_file)

            line_number = 0  # Inicia con la primera línea del archivo
            for fila in lector_csv:
                line_number += 1  # Incrementar el número de línea
                try:
                    # Verificar si el correo ya existe
                    email = fila['email']
                    if Usuari.objects.filter(email=email).exists():  # Usar el manager de Usuari
                        data["warning"] = True 
                        data["warningMsg"] = f"El correo {email} ya existe en la base de datos."
                        feedback_messages.append(f"Línea {line_number}: El correo {email} ya existe en la base de datos.".rstrip())
                        continue  # Saltar a la siguiente fila del CSV

                    # Si el correo no existe, crear el nuevo usuario
                    usuario = Usuari(
                        username=fila['username'],
                        first_name=fila['first_name'],
                        last_name=fila['last_name'],
                        email=fila['email'],
                        data_naixement=datetime.strptime(fila['data_naixement'], '%Y-%m-%d').date(),
                        cicle=fila.get('cicle'),  # Si 'cicle' no está presente, devuelve None
                        telefon=fila.get('telefon'),  # Si 'telefon' no está presente, devuelve None
                        centre=form.cleaned_data['centre'],
                        password=fila['password'],
                        # Puedes manejar la subida de imágenes de manera similar
                    )
                    
                    usuario.save()
                    # Añade lógica adicional para manejar los campos relacionales si es necesario
                    data["info"] = True
                    data["infoMsg"] = "Usuarios importados correctamente."
                    feedback_messages.append(f"Línea {line_number}: Usuario importado correctamente.".rstrip())
                except Exception as e:
                    data["error"] = True
                    data["errorMsg"] = f"Error en la línea {line_number}: {str(e)}"
                    feedback_messages.append(f"Línea {line_number}: Error - {str(e)}".rstrip())

    else:
        # Verificar si el usuario está autenticado
        if request.user.is_authenticated:
            # Obtener el centro asociado al usuario logeado
            centro = request.user.centre
            # Crear una instancia del formulario pasando el centro como argumento
            form = CSVUploadForm(centre=centro)
    
    return render(request, 'import_users.html', {'form': form, 'feedback_messages': feedback_messages, **data})

def list_loan(request):
    prestecs = Prestec.objects.filter(usuari=request.user)
    now = timezone.now()

    for prestec in prestecs:
        prestec.retrasado = now > prestec.data_retorn

    return render(request, 'list_loan.html', {'prestecs': prestecs})
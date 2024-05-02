import logging
from django.utils import timezone
from .models import Log, Usuari 
from django.db import transaction

import logging
from django.utils import timezone
from .models import Log

def generarLog(request, tipo, mensaje, ruta, usuario):
    session_key = request.session.session_key
    if not session_key:
        request.session.save()
        session_key = request.session.session_key
    
    logs = request.session.get('logs', [])
    
    nuevo_log = {
        'timestamp': timezone.now().isoformat(),
        'tipo': tipo,
        'mensaje': mensaje,
        'ruta': ruta
    }
    logs.append(nuevo_log)
    
    request.session['logs'] = logs

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    for log in logs:
        log_message = f"{log['timestamp']} - {log['tipo'].upper()}: {log['mensaje']}"
        getattr(logger, log['tipo'].lower())(log_message)
    
    log_obj = Log(esdeveniment=mensaje, nivell=tipo, data=timezone.now(), usuari=usuario, ruta=ruta)
    log_obj.save()

    return f"{tipo.upper()}: {mensaje}"

def subir_logs_a_bd(request):
    logs = request.session.get('logs', [])
    
    usuario = None
    if request.user.is_authenticated:
        usuario = request.user

    with transaction.atomic():
        for log in logs:
            tipo = log['tipo']
            mensaje = log['mensaje']
            ruta = log['ruta']
            log_obj = Log(esdeveniment=mensaje, nivell=tipo, data=timezone.now(), usuari=usuario, ruta=ruta)
            log_obj.save()

        request.session['logs'] = []

    return "Todos los logs han sido guardados en la base de datos."

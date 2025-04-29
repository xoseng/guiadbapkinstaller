# coding=utf8
#Author: Xosé Brais Noya García

#Comentarios, información adicional relevante
#capturar eventos: adb shell "getevent -l"
#ver servicios: adb shell "service list"
#ver paquetes: adb shell "pm list packages"

#Imports
import time
from subprocess import check_output

#Funciones
def adb_start():
    val= str(check_output("adb kill-server && adb start-server", shell=False))
    return val

def adb_start_headless():
    from subprocess import DEVNULL, call
    # Ejecuta el comando sin mostrar nada en consola
    call("adb kill-server && adb start-server", shell=True, stdout=DEVNULL, stderr=DEVNULL)

def adb_devices():
    val= str(check_output("adb devices", shell=False))
    return val

def device_status():
    try:
        val=adb_devices()
        val=val.replace('\\r','')
        val=val.replace('\\t','')
        val=val.replace('\\n','\n')
        val=val.replace("b'","")
        val=val.replace("'","")
        val=val.split('\n')[1]

        status = 'CONNECTED'
        if val == '':
            status='DISCONNECTED'
        else:
            #comprobar el estado
            if 'device' in val:
                status = 'CONNECTED'
            if 'unauthorized' in val:
                status = 'UNAUTHORIZED'
        return status
    except:
        status = 'DISCONNECTED'
        return status

def obtener_dispositivos_completo():
    from subprocess import check_output
    try:
        output = check_output("adb devices", shell=False).decode("utf-8")
        lineas = output.strip().split("\n")[1:]  # Ignorar cabecera
        dispositivos = []

        for linea in lineas:
            if linea.strip() == '':
                continue
            partes = linea.split('\t')
            if len(partes) == 2:
                dispositivos.append((partes[0], partes[1]))  # (id, estado)

        return dispositivos

    except Exception as e:
        return []

import subprocess

def instalar_apks_en_dispositivo(id_dispositivo, lista_apks):
    import colorama
    from colorama import Back, Fore, Style
    colorama.init(
        autoreset=True)  # NOTICE: to reset color, if not set the terminal color should be change to last print...

    try:
        for apk in lista_apks:
            comando = f'adb -s {id_dispositivo} install "{apk}"'
            resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)

            if resultado.returncode != 0:
                print(Fore.RED + f"Error al instalar {apk}: {resultado.stderr}")
                return False  # Fallo, salimos

        return True  # Todo correcto

    except Exception as e:
        print(Fore.RED + f"Excepción durante la instalación: {str(e)}")
        return False


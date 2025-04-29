# coding=utf8
# Author: Xosé Brais Noya García

#imports
import cmd_command

def limpiar_consola():
    import os
    os.system('cls')

def abrir_explorer_apks():
    import os
    os.startfile(os.path.abspath('./apks/'))

def instalar_adb():
    import os
    os.startfile(os.path.abspath('./adb/adb.exe'))

def obtener_apks():
    import os
    ruta_apks = os.path.abspath('./apks/')
    ruta_base='./apks/'
    apks_encontradas = []

    if not os.path.isdir(ruta_apks):
        return []  # Si la carpeta no existe, devolvemos vacío

    for archivo in os.listdir(ruta_apks):
        if archivo.lower().endswith('.apk'):
            #apks_encontradas.append(os.path.join(ruta_apks, archivo))
            apks_encontradas.append(os.path.join(ruta_base, archivo))

    return apks_encontradas


def adb_instalado():
    #shutil.which("adb") busca si el comando adb está en el PATH del sistema. Si lo encuentra, devuelve su ruta; si no, devuelve None.
    import shutil
    return shutil.which("adb") is not None
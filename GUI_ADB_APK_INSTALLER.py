# coding=utf8
# Author: Xosé Brais Noya García

#IMPORTS PRIV
import functions_library
import adb_library
import cmd_command
import tkinter_library_functions

#IMPORTS
import time
import subprocess
from os import path
import os
from PIL import Image
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import webbrowser
import threading
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

def main_start():

    #MAIN FUNCTIONS
    # Muestra el mensaje y elimina lo anterior
    def update_log_clean(mensaje):
        log_box.config(state="normal")
        log_box.delete("1.0", END)
        log_box.insert(END, mensaje + "\n")
        log_box.see(END)
        log_box.config(state="disabled")

    # Añade un nuevo mensaje sin borrar lo anterior
    def update_log(mensaje):
        log_box.config(state="normal")
        log_box.insert(END, mensaje + "\n")
        log_box.see(END)
        log_box.config(state="disabled")

    def iniciar_instalacion():

        if instalacion_activa.get():
            update_log("⚠️ Ya hay una instalación en proceso. Finalízala antes de iniciar otra.")
            return

        update_log_clean("Iniciando...")

        update_log("🔍 Verificando APKs...")

        apks_found = functions_library.obtener_apks()
        if not apks_found:
            update_log("❌ No se encontraron APKs en ./apks/. Abriendo carpeta para que las añadas...")
            functions_library.abrir_explorer_apks()
            return
        else:
            update_log(f"✅ Se encontraron {len(apks_found)} APK(s).")

        update_log("🔍 Verificando instalación de ADB...")
        if not functions_library.adb_instalado():
            update_log("❌ ADB no está instalado. Iniciando instalador de ADB...")
            functions_library.instalar_adb()
            return
        else:
            update_log("✅ ADB está instalado y listo.")

        # Si pasamos todas las verificaciones, lanzamos el hilo de escaneo
        hilo = threading.Thread(target=buscar_dispositivos, args=(apks_found,))
        hilo.start()

    def buscar_dispositivos(apks_found):
        update_log_clean("🔍 Buscando dispositivos conectados...")
        instalacion_activa.set(True)

        while instalacion_activa.get():
            dispositivos = adb_library.obtener_dispositivos_completo()
            dispositivos_validos = []

            for id_disp, estado in dispositivos:
                if estado == "device":
                    if id_disp not in dispositivos_instalados:
                        update_log(f"✅ {id_disp} está autorizado y listo.")
                        dispositivos_validos.append(id_disp)
                    else:
                        update_log(f"⚠️ {id_disp} ya fue procesado anteriormente.")
                elif estado == "unauthorized":
                    update_log(f"❌ {id_disp} está conectado pero no autorizado. Acepta el permiso en el dispositivo.")
                else:
                    update_log(f"❌ {id_disp} tiene un estado desconocido o no válido: {estado}")

            if not dispositivos:
                update_log("❌ No se encontraron dispositivos conectados. Verifica la Depuración USB.")

            if dispositivos_validos:
                for dispositivo in dispositivos_validos:
                    update_log(f"🚀️ Instalando APKs en {dispositivo}...")
                    exito = adb_library.instalar_apks_en_dispositivo(dispositivo, apks_found)
                    if exito:
                        dispositivos_instalados.append(dispositivo)
                        update_log(f"✅ APKs instaladas correctamente en {dispositivo}")
                    else:
                        update_log(f"❌ Error al instalar APKs en {dispositivo}.")

            time.sleep(tasa_refresco)

        update_log_clean("🔚 Instalación finalizada.\nPuedes desconectar dispositivos.")

    def finalizar_instalacion():
        instalacion_activa.set(False)

    # MAIN SCREEN
    version_software = 'GUI ADB APK INSTALLER v0.2 BETA'
    logo_path = './img/apk.ico'
    root = Tk()
    root.config(bd=30)
    root.title(version_software)  # Titulo de la ventana
    root.iconbitmap(logo_path)  # Icono de la ventana, en ico o xbm en Linux
    root.resizable(0, 0)  # Desactivar redimension de ventana

    menubar = Menu(root)
    root.config(menu=menubar)

    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Términos de licencia", command=tkinter_library_functions.license_agreement_gnu)
    helpmenu.add_command(label="Página del proyecto", command=tkinter_library_functions.project_website)
    helpmenu.add_command(label="Sobre el programa", command=tkinter_library_functions.about_program)
    helpmenu.add_command(label="Salir", command=tkinter_library_functions.exit_program)
    menubar.add_cascade(label="Información", menu=helpmenu)

    imgpath = './img/logo.png'
    img_tk = ImageTk.PhotoImage(Image.open(imgpath))
    imglabel = Label(root, image=img_tk).grid(row=1, column=1, padx=5, pady=5)

    # GLOBAL VARS
    # Lista global para dispositivos ya tratados, se resetea cada vez que se reinicia el programa.
    dispositivos_instalados = []
    # Tasa refresco en segundos
    tasa_refresco = 10
    # CONTROL PARA LA INSTALACIÓN
    instalacion_activa = BooleanVar()
    instalacion_activa.set(False)
    # StringVar para log de salida
    info_output = StringVar()
    info_output.set("Es necesario tener ADB instalado en el equipo.\nRecuerda conectar el dispositivo al equipo con la depuración USB activada (Opciones de desarrollador).\n")

    # --- BUTTON ZONE ---
    install_adb_button = Button(
        root,
        text="🚀️ Instalar ADB",
        command=functions_library.instalar_adb,
        width=25,
        bg="#dff0d8",
        fg="#3c763d",
        font=("Segoe UI", 10, "bold")
    )
    install_adb_button.grid(row=2, column=1, pady=5)

    open_apks_button = Button(
        root,
        text="📂 Abrir carpeta de APKs",
        command=functions_library.abrir_explorer_apks,
        width=25,
        bg="#fff8dc",
        fg="#8a6d3b",
        font=("Segoe UI", 10, "bold")
    )

    open_apks_button.grid(row=3, column=1, pady=5)

    # Área de texto para mostrar logs (solo lectura)
    log_box = ScrolledText(root, width=70, height=10, wrap=WORD, state="normal", font=("Consolas", 9))
    log_box.grid(row=4, column=1, padx=5, pady=10)
    log_box.insert(END, info_output.get())
    log_box.config(state="disabled")  # lo volvemos solo lectura

    start_button = Button(
        root,
        text="▶️ Iniciar instalación",
        command=iniciar_instalacion,
        width=25,
        bg="#d9edf7",
        fg="#31708f",
        font=("Segoe UI", 10, "bold")
    )
    start_button.grid(row=5, column=1, pady=5)

    finalizar_button = Button(
        root,
        text="⛔ Finalizar instalación",
        command=finalizar_instalacion,
        width=25,
        bg="#f2dede",
        fg="#a94442",
        font=("Segoe UI", 10, "bold")
    )
    finalizar_button.grid(row=6, column=1, pady=5)

    # CENTER WINDOW TO SCREEN
    tkinter_library_functions.center(root)
    # LOOP TK
    root.mainloop()

main_start()



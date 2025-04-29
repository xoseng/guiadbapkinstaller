# 📱 GUI ADB APK INSTALLER APP

## Descripción
Este programa permite instalar automáticamente archivos APK en dispositivos Android conectados al ordenador mediante ADB, usando una **interfaz gráfica (GUI)** sencilla y clara basada en **Tkinter**.

Es compatible con Windows, y necesita tener instalado ADB en el equipo para funcionar.

## Captura de pantalla

A continuación, una vista previa de la interfaz del programa:

![Captura de la interfaz](https://github.com/xoseng/guiadbapkinstaller/blob/main/img/tk_interfaz.png?raw=true)

---

## Características principales

- Detecta dispositivos Android conectados con depuración USB activada.
- Instala automáticamente todos los APKs que haya en la carpeta `apks/`.
- Permite abrir directamente el directorio donde debes colocar los APKs.
- Incluye botón para instalar ADB si no está instalado.
- Interfaz amigable, sin necesidad de usar consola.
- Seguimiento del estado de instalación en tiempo real.
- Posibilidad de cancelar la instalación en cualquier momento.
- Código 100% en **Python 3** y liberado bajo licencia **GNU GPL v3**.

---

## Requisitos

- Python 3.8 o superior
- Librerías:

```
Pillow>=9.5.0
cx-Freeze>=6.7
```

Instalación de dependencias:

```bash
pip install -r requirements.txt
```

---

## Estructura del proyecto

```
gui_adb_apk_installer/
├── adb/                   # Herramientas ADB necesarias
├── apks/                  # Carpeta donde se deben colocar los APKs a instalar
├── docs/                  # Documentación y licencias
├── img/                   # Imágenes y logotipos usados en la GUI
├── functions_library.py   # Funciones de apoyo
├── adb_library.py         # Funciones relacionadas con ADB
├── cmd_command.py         # Funciones para ejecutar comandos de sistema
├── tkinter_library_functions.py # Funciones específicas para la GUI
├── main_gui_installer.py   # Código principal de la interfaz
├── requirements.txt       # Dependencias del proyecto
├── setup.py               # Script para compilar a ejecutable (.exe)
└── README.md              # Este archivo
```

---

## Cómo ejecutar

```bash
python main_gui_installer.py
```

o, si quieres generar un `.exe`, usa:

```bash
python setup.py build
```

---

## Autor

**Xosé Brais Noya García**  
© 2025

---

## Licencia

Este proyecto está licenciado bajo los términos de la **Licencia Pública General GNU v3.0** (GPL-3.0).

Puedes consultar los términos completos aquí:  
🔗 [https://www.gnu.org/licenses/gpl-3.0.html](https://www.gnu.org/licenses/gpl-3.0.html)

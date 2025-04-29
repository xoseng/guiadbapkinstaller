# coding=utf8
# author: Xose Brais Noya Garcia

#IMPORTS
from PIL import Image
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import webbrowser
import threading
from tkinter import ttk

#GLOBAL VARS
version_software='GUI ADB APK INSTALLER v0.1 BETA'
author='Xosé Brais Noya García'
url='https://github.com/xoseng/guiadbapkinstaller'
email='xose.noya.garcia@gmail.com'
github='https://github.com/xoseng'
logo_img='./img/apk.ico'

# GUI FUNCTIONS
def about_program():
    #import Tkinter as tk
    import tkinter as tk
    root = tk.Tk()
    root.title("Sobre el programa")  # Titulo de la ventana
    logo_about='./img/about.ico'
    root.iconbitmap(logo_about)  # Icono de la ventana, en ico o xbm en Linux
    root.resizable(0, 0)
    texto = tk.Text(root)
    texto.pack()
    texto.config(width=38, height=4, padx=5, pady=5)
    texto.insert(tk.END,version_software+"\nAutor: "+author+"\nEmail: "+email+"\nGitHub: "+github+"\n")
    texto.config(state="disabled")
    center(root)
    root.mainloop()

def license_agreement_gnu():
    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.title("Términos de licencia")
    root.iconbitmap('./img/license.ico')
    root.resizable(0, 0)

    frame = ttk.Frame(root)
    frame.pack(fill="both", expand=True)

    # Scrollbar
    scrollbar = tk.Scrollbar(frame)
    scrollbar.pack(side="right", fill="y")

    # Text widget con scroll
    texto = tk.Text(frame, wrap="word", yscrollcommand=scrollbar.set)
    texto.pack(side="left", fill="both", expand=True)
    scrollbar.config(command=texto.yview)

    texto.config(width=80, height=20, padx=10, pady=10)

    licencia_gnu = """Licencia Pública General GNU v3.0

    Los permisos de esta licencia copyleft fuerte están condicionados
    a la disponibilidad del código fuente completo de las obras licenciadas y sus modificaciones,
    incluyendo trabajos más grandes que utilicen una obra licenciada, bajo la misma licencia.
    Deben conservarse los avisos de copyright y de licencia.
    Los contribuyentes otorgan una concesión expresa de derechos de patente.

    Puedes copiar, distribuir y modificar el software siempre que registres los cambios y fechas
    en los archivos fuente. Cualquier modificación o software que incluya (vía compilador) código licenciado bajo la GPL
    también debe estar disponible bajo la misma licencia GPL, junto con las instrucciones de compilación e instalación.

    Para consultar el texto completo de la licencia, visita: https://www.gnu.org/licenses/gpl-3.0.html
    """

    texto.insert(tk.END, licencia_gnu)
    texto.config(state="disabled")

    center(root)
    root.mainloop()

def exit_program():
    sys.exit()
    root.destroy()

def center(win):
    """
    centers a tkinter window
    :param win: the root or Toplevel window to center
    """
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()

def project_website():
    import webbrowser
    webbrowser.open(url)
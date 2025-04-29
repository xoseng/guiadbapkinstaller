# coding=utf8
#launch from cmd: python setup.py build
     
from cx_Freeze import setup, Executable

target = Executable(
    script="GUI_ADB_APK_INSTALLER.py",
    base="Win32GUI", #esta línea oculta la consola
    icon="apk.ico"
    )

options = {
    'build_exe': {
        'include_files': ['adb/', 'apks/', 'docs/', 'img/', 'apk.ico']
    }
}

setup(
    name="GUI ADB APK INSTALLER",
    version="0.1",
    description="GUI ADB APK INSTALLER 0.1 BETA",
    author="Xosé Brais Noya García",
    options=options,
    executables=[target]
    )
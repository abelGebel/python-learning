"""
Consular programas instalados en Windows.
El registro de windows es una bd gerarquica que almacean configuaraciones y opciones para el SO , HARDWARE, APPS y usuarios.

"""
import os
import winreg # Para acceder al registro de aplicaciones

key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                     r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall")

programs = []

num_subkeys = winreg.QueryInfoKey(key)[0]

for i in range(num_subkeys):
    try:
        subkey_name = winreg.EnumKey(key, i)
        subkey = winreg.OpenKey(key, subkey_name)

        display_name = winreg.QueryValueEx(subkey, "DisplayName")[0]
        programs.append(display_name)
    except FileNotFoundError as e:
        print(f"{subkey_name}: {e}")

for program in programs:
    print(program)
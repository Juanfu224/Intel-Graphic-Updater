import os
import time
from sys import stdout


"""LOGOTIPO DE LA APLICACIÓN"""
BANNER = """
██╗███╗   ██╗████████╗███████╗██╗                                                                           
██║████╗  ██║╚══██╔══╝██╔════╝██║                                                                           
██║██╔██╗ ██║   ██║   █████╗  ██║                                                                           
██║██║╚██╗██║   ██║   ██╔══╝  ██║                                                                           
██║██║ ╚████║   ██║   ███████╗███████╗                                                                      
╚═╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚══════╝                                                      (by Juanfu224)
██████╗ ██████╗ ██╗██╗   ██╗███████╗██████╗       ██╗   ██╗██████╗ ██████╗  █████╗ ████████╗███████╗██████╗ 
██╔══██╗██╔══██╗██║██║   ██║██╔════╝██╔══██╗      ██║   ██║██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██╔══██╗
██║  ██║██████╔╝██║██║   ██║█████╗  ██████╔╝█████╗██║   ██║██████╔╝██║  ██║███████║   ██║   █████╗  ██████╔╝
██║  ██║██╔══██╗██║╚██╗ ██╔╝██╔══╝  ██╔══██╗╚════╝██║   ██║██╔═══╝ ██║  ██║██╔══██║   ██║   ██╔══╝  ██╔══██╗
██████╔╝██║  ██║██║ ╚████╔╝ ███████╗██║  ██║      ╚██████╔╝██║     ██████╔╝██║  ██║   ██║   ███████╗██║  ██║
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝       ╚═════╝ ╚═╝     ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝     
"""


"""COLORES"""
def red():  # Rojo
    RED = "\033[1;31m"
    stdout.write(RED)


def green():  # Verde
    GREEN = "\033[0;32m"
    stdout.write(GREEN)


def blue():  # Azul
    BLUE = "\033[1;34m"
    stdout.write(BLUE)


def yellow():  # Amarillo
    YELLOW = "\033[1;33m"
    stdout.write(YELLOW)


def orange():  # Naranja
    ORANGE = "\033[1;38;5;208m"
    stdout.write(ORANGE)


def white():  # Blanco
    WHITE = "\033[1;37m"
    stdout.write(WHITE)


def purple():  # Morado
    PURPLE = "\033[1;35m"
    stdout.write(PURPLE)


def cyan():  # Cian
    CYAN = "\033[1;36m"
    stdout.write(CYAN)


def light_gray():  # Gris claro
    LIGHT_GRAY = "\033[0;37m"
    stdout.write(LIGHT_GRAY)


def dark_gray():  # Gris oscuro
    DARK_GRAY = "\033[1;30m"
    stdout.write(DARK_GRAY)


def light_blue():  # Azul claro
    LIGHT_BLUE = "\033[1;94m"
    stdout.write(LIGHT_BLUE)


"""FUNCIONES PRINCIPALES"""
#  Añade y firma el repositorio de Intel
def preparar_cliente():
    os.system("wget -qO - https://repositories.intel.com/gpu/intel-graphics.key | \
              sudo gpg --yes --dearmor --output /usr/share/keyrings/intel-graphics.gpg")
    soportar_i386()


# Pregunta al usuario si desea soportar actualizaciones de paquetes i386.
# Configura el repositorio de Intel en función de la respuesta.
def soportar_i386():
    no_soportar_i386 = "echo 'deb [arch=amd64 signed-by=/usr/share/keyrings/intel-graphics.gpg] https://repositories.intel.com/gpu/ubuntu jammy client' | \
        sudo tee /etc/apt/sources.list.d/intel-gpu-jammy.list"
    si_soportar_i386 = "echo 'deb [arch=amd64,i386 signed-by=/usr/share/keyrings/intel-graphics.gpg] https://repositories.intel.com/gpu/ubuntu jammy client' | \
        sudo tee /etc/apt/sources.list.d/intel-gpu-jammy.list"

    while True:
        soportar = input(
            "\n¿Deseas poder soportar actualizaciones de paquetes i386 de Intel? (s/n): ").lower()
        if soportar not in ["s", "n"]:
            print("\nSolo puedes responder 's' o 'n'\n")
            continue
        if soportar == "s":
            os.system(si_soportar_i386)
        else:
            os.system(no_soportar_i386)
        break


# Actualizar los repositorios y realizar una actualización completa
def updatear_sistema():
    os.system("sudo apt update")
    os.system("sudo apt full-upgrade -y")


# Instalar los paquetes Compute Runtime, Media y Mesa
def instalar_drivers():
    updatear_sistema()
    os.system("sudo apt install -y \
              intel-opencl-icd intel-level-zero-gpu level-zero intel-level-zero-gpu-raytracing \
              intel-media-va-driver-non-free libmfx1 libmfxgen1 libvpl2 \
              libegl-mesa0 libegl1-mesa libegl1-mesa-dev libgbm1 libgl1-mesa-dev libgl1-mesa-dri \
              libglapi-mesa libgles2-mesa-dev libglx-mesa0 libigdgmm12 libxatracker2 mesa-va-drivers \
              mesa-vdpau-drivers mesa-vulkan-drivers va-driver-all vainfo hwinfo clinfo \
              libigc-dev intel-igc-cm libigdfcl-dev libigfxcmrt-dev level-zero-dev")


# Recomienda actualizar el sistema y pregunta si se desea reiniciar.
def recomendar_reinicio():
    while True:
        reiniciar = input(
            "\nSe recomienda reiniciar el sistema después de instalar los drivers. ¿Quieres reiniciar ahora? (s/n): ").lower()
        if reiniciar not in ["s", "n"]:
            print("\nSolo puedes responder 's' o 'n'\n")
            continue
        if reiniciar == "s":
            os.system("sudo reboot")
        break


# Función principal que configura el sistema e instala los drivers.
def instalar():
    # Añadir y firmar repositorios de intel repositorio
    print("\n[+] Configurando su sistema para instalar paquetes de cliente....\n")
    time.sleep(3)
    preparar_cliente()

    # Instalar los paquetes Compute Runtime, Media y Mesa
    print("\n[+] Instalando Compute Runtime, Media y Mesa en el cliente....\n")
    time.sleep(3)
    instalar_drivers()


"""PROGRAMA PRINCIPAL"""
if __name__ == "__main__":
    # Imprimir banner del programa
    blue()
    print(BANNER)

    # Funcion principal
    white()
    instalar()

    # Recomenda reiniciar sistema
    orange()
    recomendar_reinicio()

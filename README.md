# Intel-Graphic-Updater
Automatiza la instalación y la configuración de los drivers gráficos de Intel en equipos cón GPUs dedicadas o integradas en las CPU a partir de la 11º generación. Este script ha sido creado con la finalidad de ofrecer una forma de actualizar drivers a los usuarios con una forma mucho mas fácil, rápida e interactiva, pudiendo elegir tener soporte a la arquitectura i386 en caso de ser requerido.

Es compatible con cualquier distribución basada en Ubuntu. Probado en Linux Mint 22 (Wilma) y Ubuntu 24.04 LTS.

# Instalación
```
sudo apt install git
git clone https://github.com/Juanfu224/Intel-Graphic-Updater.git ~/Intel-Graphic-Updater
cd ~/Intel-Graphic-Updater
python3 main.py
```

# Funciones del Script
El script consta de varias funciones distintas:

- **La opción más sencilla** es utilizar la habilitación de hardware (HWE) suministrada por Ubuntu Desktop a partir de Ubuntu 23.04 para gráficos integrados y discretos. Esta es la opción más sencilla y no requiere ninguna configuración personalizada. Sin embargo, esta opción no está validada y algunas funciones no están disponibles en el controlador del kernel suministrado con Ubuntu 23.04 (Lunar), por ejemplo, la depuración de GPU.

- **La pila de visualización personalizada** permite utilizar los módulos de kernel fuera del árbol de Intel para gráficos integrados y discretos. Puede utilizar Ubuntu Desktop 24.04 LTS e instalar los paquetes de cliente para actualizar el módulo de kernel y los paquetes de espacio de usuario, incluido Mesa. Esta configuración permite el uso de la depuración de GPU.

- **El escritorio aislado del desarrollo** permite utilizar el HWE provisto por Ubuntu Desktop para gráficos integrados y alojar la GPU discreta en una máquina virtual. Puede utilizar Ubuntu 24.04 LTS o una versión más reciente para su escritorio principal. La configuración adicional permite pasar la GPU discreta a una máquina virtual que ejecute el HWE de Ubuntu 24.04 LTS y el controlador fuera del árbol de Intel. **(La versión de Mesa de Intel incluye compatibilidad con el controlador fuera del árbol. Puede utilizar el Mesa estándar si utiliza el controlador predeterminado de Ubuntu 23.04.)**

# Importante
Es recomendable reiniciar el equipo después de hacer una instalación completa o reiniciar el administrador de ventanas.

# Extras
Toda la información y paquetes necesarios para la instalación han sido extraidos directamente desde la página oficial de Intel.

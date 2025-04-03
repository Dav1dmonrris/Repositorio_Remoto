#  - - - Manipular un repositorio remotamente- - -
## 1- Configurar git:
    git config --global user.name "Usuario"
    git config --global user.email "tu@email.com"
#### puedes verificar la configuracion con:
    git config --global --list
## 2- Para clonar un repositorio:
    git clone https://github.com/tu-usuario/tu-repositorio.git
  puedes copiar la direccion ssh directamente del repositorio y sustituirlo por la direccion de arriba.

## 3- Generar claves SSH:
    ssh-keygen -t ed25519 -C "tu_email@github.com"
## 4- Activa el SSH Agent:
    eval "$(ssh-agent -s)"
#### sino funcionó, pueba con:
    exec ssh-agent bash
#### Agregar claves al SSH agent:
    ssh-add ~/.ssh/id_ed25519
#### Mostrar clave publica:
    cat ~/.ssh/id_ed25519.pub
## 4- Agregar clave a tu perfil Github y listo.

# - - - Comandos para el Agente SSH- - -
## Para SHELL:
- **-c** : Genera comandos para C-Shell
- **-s** : Genera comandos para Bourne Shell
- **-k** : Elimina el Agente SSH actual
- **-D** : Ejecuta ssh-agent en modo foreground
- **-t 3600** : Establece el tiempo máximo de vida para las claves cargadas
- **-s** : Genera comandos para Bourne Shell

## Mostrar claves en el agente:
    ssh-add -L

   

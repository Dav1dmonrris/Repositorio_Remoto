##  Manipular un repositorio remotamente
## Configurar git:
    git config --global user.name "Usuario"
    git config --global user.email "tu@email.com"
### puedes verificar la configuracion con:
    git config --global --list
## Para clonar un repositorio:
    git clone https://github.com/tu-usuario/tu-repositorio.git
  puedes copiar la direccion ssh directamente del repositorio y sustituirlo por la direccion de arriba.

### Generar claves SSH:
    ssh-keygen -t ed25519 -C "tu_email@github.com"
### Agregar claves a tu ordenador:
    ssh-add ~/.ssh/id_ed25519
### Mostrar clave publica:
    cat ~/.ssh/id_ed25519.pub
### Agregar clave a tu perfil Github
   

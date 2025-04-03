##  Manipular un repositorio remotamente
### Generar claves SSH:
    ssh-keygen -t ed25519 -C "tu_email@github.com"
### Agregar claves a tu ordenador:
    ssh-add ~/.ssh/id_ed25519
### Mostrar clave publica:
    cat ~/.ssh/id_ed25519.pub
### Agregar clave a tu perfil Github
   

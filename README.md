# Gitid: Administrar varias identidades git/github

Esta herramienta es para los que tienen varias cuentas de github, o los que quieren separar su identidad del internet de la personal, etc.

Es un pequeño script que guarda los nombres de usuario y mail, para poder cambiar de cuentas facilmente. No soporta cambiar de cuentas de github automaticamente,
por lo que en cada cambio de cuenta el script te mandara a autorizar la cuenta manualmente. 

Para que funcione el sistema debe tener instalado Python 3, y el script debera estar en un directorio apuntado por el PATH del sistema si estas en Windows.

### Comandos:

`gitid`: Imprime el usuario logeado ahora mismo.

`gitid list`: Lista los usuarios guardados.

`gitid auth`: Logearse como un usuario guardado.

`gitid add`: Agrega un usuario a los usuarios guardados.

`gitid remove`: Borra un usuario de los usuarios guardados.
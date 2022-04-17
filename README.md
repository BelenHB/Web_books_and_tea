# Proyecto:  Books & Tea

## Entrega Proyecto Final - Coderhouse
## Realizado por: Analía Belén Hereñú Baldo
Este proyecto fue realizado individualmente.


## Página: BOOKS & TEA
Este proyecto está dirigido a personas que les guste la lectura mientras 
disfruta de algún té con algo rico para comer.
La idea es que los usuarios puedan registrar sus libros favoritos, junto con
recetas inspiradas por esa lectura y un blog donde poder compartir su 
experiencia de cocina o lectura.

## VIDEO DEMO
El video donde se muestra de modo resumido, un recorrido por el funcionamiento integral de la app.


https://drive.google.com/file/d/1iR-q4effSlFv7lFpxGzOc9V4QYPwMNDX/view?usp=sharing

## INICIO
En esta página se da la bienvenida de forma genérica y se invita a registrarse.
Si el usuario ya se hubiera logueado, se personaliza la bienvenida y no es visible el botón de REGÍSTRATE.

## REGISTRARSE
Esta sección permite registrarse en la página, solicitando:
- nombre de usuario
- correo electrónico
- contraseña
- confirmación de contraseña

Una vez ingresado estos datos, presionando el botón REGISTRARSE, se procede a guardar los datos del usuario y se redirecciona al formulario de INGRESO, para que efectivamente puede utilizar la página como usuario registrado.
Si el usuario optara por abortar el registro, mediante el botón INICIO, puede regresar el inicio sin registrarse.
Registrarse en la página otorga acceso a ciertas funcionalidades descriptas posteriormente.

## INGRESAR
Una vez que el usuario, previamente registrado, ingresa, es redireccionado al inicio con un mensaje de bienvendia personalizado (Bienvenido, nombre_de_usario). También se modifica el navbar, mostrando la opción CERRAR SESIÓN para salir y una imagen de avatar sin definir. Presionando sobre esta imagen, nos lleva a mostrar el perfil de usuario, que por el momento solo contendrá el nombre de usuario.

Aquí aparece la opción EDITAR USUARIO y VOLVER. Éste último, nos lleva de regreso a inicio sin modificar nada.

El botón de EDITAR USUARIO abre un formulario para registrar más información de este usuario:
- email: permite modificar el ingresado al registrarnos o dejarlo (es un campo obligatorio)
- Contraseña: si no se completa, permite seguir utilizando la contraseña registrada previamente.
- Confirma contraseña: ídem el anterior
- Nombre: ingresar nombre del usuario (es obligatorio)
- Apellido: ingresar apellido del usuario (no obligatorio)
- Avatar: elegir una imagen de avatar (no obligatorio)
- Link: dirección web del usuario (no obligatorio)
- Descripción: información adicional que el usuario quiera mostrar o compartir.

Con el botón EDITAR PERFIL se confirman los datos ingresados.
Si se elige una imagen de avatar, en el navbar aparecerá la elegida, en reemplazo del avatar sin definir, la cual tendrá la misma funcionalidad que la anterior (redirigir al formulario de edición del perfil).

## LIBROS
En esta sección se puede ver un listado de los libros y autores que recomiendan los usuarios.

Si no está registrado, solamente puede acceder a ver el listado y utilizar la función BUSCAR LIBRO. Los botones EDITAR, BORRAR y AGREGAR LIBRO lo redireccionará al formulario de INGRESAR.
Esta función de BUSCAR LIBRO nos pide ingresar una palabra o fragmento de ella, que será buscada tanto en los títulos de los libros como en el nombre del autor. Haciendo scroll se pueden observar los resultados de la búsqueda o un cartel que informa que no hay resultados.

El botón VOLVER nos lleva de nuevo al listado de libros.

Si el usuario está registrado, tiene acceso a las funciones:
- AGREGAR LIBRO: se accede al formulario de carga de libro, debiendo ingresar Título, Autor e ISBN (International Standard Book Number, solo números en un máximo de 13 dígitos).
- EDITAR: permite ingresar al libro seleccionado para modificar alguno de sus datos. El botón ACTUALIZAR guarda los cambios efectuados.
- BORRAR: permite borrar el libro seleccionado. Esta función no tiene confirmación de borrado, así que se debe ser cuidadoso con su uso.

En todos los casos en que aparece el botón VOLVER, nos lleva de regreso al listado de libros sin efectuar ningún cambio.

## RECETAS

Esta sección permite ver un listado de las recetas subidas por los usuarios.

Si el visitante no está registrado puede ver el listado de recetas y haciendo click en LEER MÁS, puede acceder a la vista completa (el listado visualiza los primeros 100 caracteres de ingredientes y 150 de preparación).

Al final del listado, nos encontramos el botón INGRESAR NUEVA RECETA. Si el usuario no está registrado, este botón nos redirecciona a INGRESAR. Si ya estamos logueados, nos despliega un formulario para cargar una nueva receta. En este debemos ingresar:
- Título: con una máximo de 150 caracteres (obligatorio)
- Ingredientes: sin máximo de caracteres, permite utilizar los comandos de edición de texto brindados por CKEditor.
- Preparación: sin máximo de caracteres, permite utilizar los comandos de edición de texto brindados por CKEditor.
- Autor: se visualiza un despleglable que permite elegir entre los usuarios registrados en la página.
- Foto: cargar un archivo de imagen (no obligatorio).

Con el botón ENVIAR se genera la publicación, sumándose al listado de recetas en primer lugar, ya que se ordenan desde la más reciente a la más antigua.

El botón LEER MÁS, como se describe anteriormente, nos permite visualizar la receta con el texto completo. El botón VOLVER nos lleva de nuevo al listado de recetas.

El botón EDITAR nos permite editar la información, siempre que ya hayamos ingresado con nuestro nombre de usuario, sino nos redirigirá al INGRESO. En esta sección poseemos un formulario similar el de creación de una nueva receta, con la salvedad de que podemos eliminar la imagen previamente seleccionada y elegir otra (aunque esto debe hacerse en dos pasos, es decir primero eliminar, actualizar la publicación y despúes volver a editar para agregar una imagen nueva).

El de BORRAR nos redirecciona a una página que nos pide confirmar el borrado del elemento elegido, para lo cual nos pone el título de la receta. Si confirmamos borrar, lo elimina y nos lleva de nuevo al listado. Sino con el botón VOLVER regresamos al listado sin realizar la operación

## BLOG
Esta sección permite ver un listado de las publicaciones del Blog.

Si el visitante no está registrado puede ver el listado de publicaciones y haciendo click en LEER MÁS, puede acceder a la publicación completa (el listado visualiza los primeros 150 caracteres).

Al final del listado, nos encontramos el botón CREAR NUEVO POST. Si el usuario no está registrado, este botón nos redirecciona a INGRESAR. Si ya estamos logueados, nos despliega un formulario para cargar una nueva publicación al blog. En este debemos ingresar:
- Título: con una máximo de 100 caracteres (obligatorio)
- Subtítulo: con una máximo de 100 caracteres (obligatorio)
- Contenido: sin máximo de caracteres, permite utilizar los comandos de edición de texto brindados por CKEditor.
- Autor: se visualiza un despleglable que permite elegir entre los usuarios registrados en la página.
- Imagen: cargar un archivo de imagen (no obligatorio).

Con el botón ENVIAR se genera la publicación, sumándose al listado de publicaciones en primer lugar, ya que se ordenan por fecha de publicación.

La fecha de publicación se genera automáticamente al crear el post y no se puede editar manualmente.

El botón LEER MÁS, como se describe anteriormente, nos permite visualizar la publicación con el texto completo. El botón VOLVER nos lleva de nuevo al listado de publicaciones.

El botón EDITAR nos permite editar la información, siempre que ya hayamos ingresado con nuestro nombre de usuario, sino nos redirigirá al INGRESO. En esta sección poseemos un formulario similar el de creación de una nueva publicación, con la salvedad de que podemos eliminar la imagen previamente seleccionada y elegir otra (aunque esto debe hacerse en dos pasos, es decir primero eliminar, actualizar la publicación y despúes volver a editar para agregar una imagen nueva).

El de BORRAR nos redirecciona a una página que nos pide confirmar el borrado del elemento elegido, para lo cual nos pone el título de la publicación. Si confirmamos borrar, lo elimina y nos lleva de nuevo al listado. Sino con el botón VOLVER regresamos al listado sin realizar la operación

## ACERCA DE
En esta sección podemos ver una imagen relacionada a la temática y un breve descripción del autor del proyecto.

## USUARIOS
Nos permite ver el listado de usuarios registrados para, en un futuro, hacer una aplicación de mensajería.

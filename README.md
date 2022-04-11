# Proyecto:  Books & Tea

## Entrega Proyecto Final - Coderhouse

## Página: BOOKS & TEA
Este proyecto está dirigido a personas que les guste la lectura mientras 
disfruta de algún té con algo rico para comer.
La idea es que los usuarios puedan registrar sus libros favoritos, junto con
recetas inspiradas por esa lectura y un blog donde poder compartir su 
experiencia de cocina o lectura.

## INICIO
En esta página se da la bienvenida de forma genérica y se invita a registrarse.
Si el usuario ya se hubiera logueado, se personaliza la bienvenida y no es visible el botón de REGÍSTRATE.

## REGISTRARSE
Esta sección permite registrarse en la página, solicitando:
- nombre de usuario
- correo electrónico
- contraseña
- confirmación de contraseña
Una vez ingresado estos datos, presionando el botón REGISTRARSE, se procede a guardar los datos del usuario y redireccionando al formulario de INGRESO, para que efectivamente puede utilizar la página como usuario registrado.
Si el usuario optara por abortar el registro, mediante el botón INICIO, puede regresar el inicio sin registrarse.
Registrarse en la página otorga acceso a ciertas funcionalidades descriptas posteriormente.

## INGRESAR
Una vez que el usuario, previamente registrado, ingresa, es redireccionado al inicio con un mensaje de bienvendia personalizado (Bienvenido, nombre_de_usario). También se modifica el navbar, mostrando la opción CERRAR SESIÓN para salir y una imagen de avatar sin definir. Presionando sobre esta imagen, nos lleva a mostrar el perfil de usuario, que por el momento solo contendrá el nombre de usuario.
Aquí aparece la opción EDITAR USUARIO y VOLVER. Éste último, nos lleva de regreso a inicio sin modificar nada.
El botón de EDITAR USUARIO abre un formulario para registrar más información de este usuario:
- email: permite modificar el ingresado al registrarnos (es obligatorio)
- Contraseña: si no se completa, permite seguir utilizando la contraseña registrada previamente.
- Confirma contraseña: ídem el anterior
- Nombre: ingresar nombre del usuario (es obligatorio)
- Apellido: ingresar apellido del usuario (no obligatorio)
- Avatar: elegir una imagen de avatar (no obligatorio)
- Link: dirección web del usuario (no obligatorio)
- Descripción: información adicional que el usuario quiera mostrar o compartir
Con el botón EDITAR PERFIL se confirman los datos ingresados.
Si se elige una imagen de avatar, en el navbar aparecerá la elegida, en reemplazo del avatar sin definir, la cual tendrá la misma funcionalidad que la anterior (redirigir al formulario de edición del perfil).

## LIBROS
En esta sección se puede ver un listado de los libros y autores que recomiendan los usuarios.
Si no está registrado, solamente puede acceder a ver el listado y utilizar la función BUSCAR LIBRO. Los botones EDITAR, BORRAR y AGREGAR LIBRO lo redireccionará al formulario de INGRESAR.
Esta función de BUSCAR LIBRO nos pide ingresar una palabra o fragmento de ella, que será buscada tanto en los títulos de los libros o en el nombre del autor. Haciendo scroll se pueden observar los resultados de la búsqueda o un cartel que informa que no hay resultados.
El botón VOLVER nos lleva de nuevo al listado de libros.
Si el usuario está registrado, tiene acceso a las funciones:
- AGREGAR LIBRO: se accede al formulario de carga de libro, debiendo ingresar Título, Autor e ISBN (International Standard Book Number, solo números en un máximo de 13 dígitos).
- EDITAR: permite ingresar al libro seleccionado para modificar alguno de sus datos. El botón ACTUALIZAR guarda los cambios efectuados.
- BORRAR: permite borrar el libro seleccionado. Esté función no tiene confirmación de borrado, así que se debe ser cuidadoso con su uso.
En todos los casos en que aparece el botón VOLVER, nos lleva de regreso al listado de libros sin efectuar ningún cambio.

### Acerca
La idea de este proyecto es el primer paso previo a la entrega final, que será 
un blog respecto a libros y comidas que podemos relacionar, ya sea a la historia,
región donde transcurre o autor. 

### Funcionamiento  
En el archivo `requirements.txt` se listan los requerimientos para el 
funcionamiento del proyecto.  
En el archivo `.env` se aloja la `SECRET_KEY` de Django.  

### Descripción
La barra de navegación contiene 5 secciones que se detallan a continuación:

| SECCIÓN | DESCRIPCIÓN |
| -- | -- |
| INICIO | Página de bienvenida.  Aquí funcionará el botón de registro de usuarios.  
| LIBROS | Nos lleva al formulario para cargar los libros que se almacenarán en la base de datos. El formulario solicita: Título, Autor,  ISBN. Este último solicita el ingreso de números (hasta 13 dígitos), sin guiones.  |
| RECETAS | Lleva al formulario para cargar recetas, donde se solicita: Nombre, Preparación. |
| BLOG | Lleva al formulario de carga de posteos para el blog. Este formulario solicita: Título, Subtítulo, Autor, Contenido, Fecha (con formato AAAA-MM-DD)  |
| BUSCAR LIBROS | Esta sección permite buscar libros en la base de datos, con la opción de hacerlo por palabra que se encuentre en el título o por autor.  Abajo de estos formularios, aparecen los resultados de la búsqueda y si no los hubiera, envía un mensaje.  

Se provee una pequeña base de datos para poder comprobar los formularios de búsqueda.  

Autores ingresados (para comprobar la búsqueda por autor):  
- J. K. Rowling
- Mark Twain
- Emily Bronte
- Charlotte Bronte  

Libros ingresados (para buscar por nombre):  
- Harry Potter y el cáliz de fuego
- Harry Potter y las reliquias de la muerte
- Harry Potter y la cámara secreta
- Cumbres borrascosas
- Jane Eyre
- Las aventuras de Tom Sawyer
- Las aventuras de Huckleberry Finn


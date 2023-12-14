<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!-- 
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links -->

<!--
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url] -->



<!-- PROJECT LOGO -->
*Esta herramienta digital es un prototipado para el Trabajo de Final de Grado de la carrera Licenciatura en Informatica de la **Universidad Siglo 21**. Puedes conocer más sobre la universidad en [21.edu.ar](https://21.edu.ar/)*

---

<div align="center">
<h2 align="center"> Sistema de Medición de Producción en Yacimientos Hidrocarburíferos</h2>
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" alt="Logo" height="100">
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRprKd5aRy8vxodob4oY-zWqu4ri9efRBKa7Uv1RQEA2LwF2OTaDDDUuQvM8L5u37orzww&usqp=CAU" alt="Logo" height="100">
</div>
<br>
<!-- <p align="center"> Logo e imagen o gif de la interfaz principal de la herramienta</p>
<p align="center"><img src="https://www.webdevelopersnotes.com/wp-content/uploads/create-a-simple-home-page.png"/></p>  -->

## Tabla de contenidos:

- [Objetivo del Prototipo](#objetivo-del-prototipo)
- [Guía de instalación](#guía-de-instalación)
- [Guía de usuario](#guía-de-usuario)
- [Demostración](#demostración)
- [Dependencias](#dependencias)
<!-- - [Información adicional](#información-adicional)
- [Licencia](#licencia) -->


## Objetivo del Prototipo

Desarrollar un sistema que implemente los sensores de medición en los pozos,
los transmita por comunicación inalámbrica, los almacene en una base de datos para luego, publicar la información y sea consumida de diferentes aplicaciones internas y externas a la compañía.

## Guía de instalación

### Pre Requisitos
Para descargar el repositorio deberas tener instalado [Git](https://git-scm.com/downloads).

Para ejecutar localmente el proyecto, deberas tener instalado [Docker Desktop](https://docs.docker.com/desktop/).

### Instalación
Primero deberas clonar el repositorio ejecutando los siguientes comandos:

```
mkdir project
cd project
git clone https://github.com/JEPICC/TFG.git
```

Luego deberas ejecutar el comando "docker-compose" para construir la aplicacion:

```
docker-compose up
```

## Guía de Usuario

### Backend

El servidor API se ejecutar en el puerto 8000, y podras ingresar desde el navegador a la documentacion de la api, desde la siguiente direccion:
```
http://localhost:8000
```
Para generar datos de prueba, deberas ingresa a la siguiente direccion:
```
http://localhost:8000/services/generate
```
Para borrar los datos de prueba, deberas ingresa a la siguiente direccion:
```
http://localhost:8000/services/drop
```
### Frontend
Para ingresar a la aplicacíon de React, deberas ingresar en el navegador a:
```
http://localhost:5173/
```
## Demostración
Video demo de aplicación [VIDEO](Demostracion.webm) para detalles

## Dependencias
A continuacion se describen los Herramientas, Frameworks y Librerias utilizadas en el proyecto:

  * [![Docker][Docker]][Docker-url]
  * [![FastAPI][FastAPI]][FastAPI-url]
  * [![JavaScript][JavaScript]][JavaScript-url]
  * [![MongoDB][MongoDB]][MongoDB-url]
  * [![Pandas][Pandas]][Pandas-url]
  * [![Python][Python]][Python-url]
  * [![React.js][React.js]][React-url]
  * [![Visual Studio Code][Visual Studio Code]][Visual Studio Code-url]

## Licencia 📄

Este proyecto está bajo la Licencia (MIT) - mira el archivo [LICENSE](LICENSE) para detalles

<!-- ## Autor/es

Nombra a el/los autor/es original/es. Consulta con ellos antes de publicar un email o un nombre personal. Una manera muy común es dirigirlos a sus cuentas de redes sociales. -->

<!-- ## Información adicional

Esta es la sección que permite agregar más información de contexto al proyecto como alguna web de relevancia, proyectos similares o que hayan usado la misma tecnología.
 -->

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[Docker]: https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white
[Docker-url]: https://www.docker.com/
[FastAPI]: https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi
[FastAPI-url]: https://fastapi.tiangolo.com/
[JavaScript]: https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E
[JavaScript-url]: https://developer.mozilla.org/es/docs/Web/JavaScript
[MongoDB]: https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white
[MongoDB-url]: https://www.mongodb.com/es
[Pandas]: https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white
[Pandas-url]: https://pandas.pydata.org/
[Python]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://www.python.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Visual Studio Code]: https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white
[Visual Studio Code-url]: https://code.visualstudio.com/
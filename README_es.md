# Generador de Claves SSH

[🇺🇸 English](README.md) | [🇫🇷 Français](README_fr.md) | [🇯🇵 日本語](README_ja.md) | [🇨🇳 简体中文](README_zh-cn.md) | [🇩🇪 Deutsch](README_de.md) | [🇪🇸 Español](README_es.md)

Este proyecto es una API simple que genera pares de claves Ed25519. Utiliza Flask en el backend para generar las claves y proporciona las claves pública y privada a través de una respuesta JSON.

## Características

* **Generación de claves:** Genera pares de claves SSH Ed25519.
* **Punto de conexión de la API:** Proporciona un punto de conexión de la API (`/generate`) para generar el par de claves.
* **Compatibilidad:** Las claves SSH generadas son adecuadas para su uso con plataformas como GitHub, GitLab y Bitbucket.

## Explicación

La generación segura de claves SSH implica operaciones criptográficas complejas. La implementación de estas operaciones directamente en JavaScript en un entorno de navegador es significativamente más compleja y plantea problemas de seguridad. Por lo tanto, este proyecto aprovecha Python con la biblioteca `cryptography` para manejar la generación de claves en el lado del servidor.

Si bien las plataformas sin servidor como Cloudflare Workers son excelentes para implementar JavaScript, no están diseñadas para ejecutar código Python directamente. En consecuencia, este proyecto está configurado para su implementación en Vercel, que admite funciones sin servidor de Python. Esto nos permite utilizar Python para la generación segura de claves. Las claves generadas se pueden utilizar para autenticarse con plataformas populares de alojamiento de código como GitHub, GitLab y Bitbucket, lo que agiliza el proceso de configuración para los desarrolladores. La estructura del proyecto es flexible y los usuarios pueden adaptarla para la implementación en otras plataformas como Netlify que admiten funciones de backend o renderizado del lado del servidor.

## Configuración

### Requisitos previos

* Python 3.x
* pip (instalador de paquetes de Python)

### Instalación

1.  Clona el repositorio.
2.  Navega hasta el directorio del repositorio.
3.  Instala los paquetes de Python necesarios:

    ```bash
    pip install -r requirements.txt
    ```

### Ejecución local

1.  Ejecuta la aplicación Flask:

    ```bash
    python index.py
    ```
2.  La API estará disponible en la dirección especificada (generalmente `http://127.0.0.1:5000`).

### Implementación en Vercel

1.  Instala la CLI de Vercel.
2.  Realiza la implementación con Vercel. El archivo `vercel.json` está configurado para reescribir todas las solicitudes a `/api/index`.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT.

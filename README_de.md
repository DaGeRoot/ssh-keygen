# SSH-Schlüsselgenerator

[🇺🇸 English](README.md) | [🇫🇷 Français](README_fr.md) | [🇯🇵 日本語](README_ja.md) | [🇨🇳 简体中文](README_zh-cn.md) | [🇩🇪 Deutsch](README_de.md) | [🇪🇸 Español](README_es.md)

Dieses Projekt ist eine einfache API, die Ed25519-Schlüsselpaare generiert. Es verwendet Flask im Backend, um die Schlüssel zu generieren, und stellt die öffentlichen und privaten Schlüssel über eine JSON-Antwort bereit.

## Funktionen

* **Schlüsselgenerierung:** Generiert Ed25519-SSH-Schlüsselpaare.
* **API-Endpunkt:** Stellt einen API-Endpunkt (`/generate`) zum Generieren des Schlüsselpaares bereit.
* **Kompatibilität:** Die generierten SSH-Schlüssel sind für die Verwendung mit Plattformen wie GitHub, GitLab und Bitbucket geeignet.

## Erklärung

Die sichere Generierung von SSH-Schlüsseln umfasst komplexe kryptografische Operationen. Die direkte Implementierung dieser Operationen in JavaScript in einer Browserumgebung ist wesentlich komplexer und birgt Sicherheitsrisiken. Daher verwendet dieses Projekt Python mit der Bibliothek `cryptography`, um die Schlüsselgenerierung auf der Serverseite abzuwickeln.

Während Serverless-Plattformen wie Cloudflare Workers hervorragend für die Bereitstellung von JavaScript geeignet sind, sind sie nicht für die direkte Ausführung von Python-Code ausgelegt. Daher ist dieses Projekt für die Bereitstellung auf Vercel konfiguriert, das Python-Serverless-Funktionen unterstützt. Dies ermöglicht es uns, Python für die sichere Schlüsselgenerierung zu verwenden. Die generierten Schlüssel können dann zur Authentifizierung bei beliebten Code-Hosting-Plattformen wie GitHub, GitLab und Bitbucket verwendet werden, wodurch der Einrichtungsprozess für Entwickler optimiert wird. Die Projektstruktur ist flexibel und Benutzer können sie an die Bereitstellung auf anderen Plattformen wie Netlify anpassen, die Backend-Funktionen oder serverseitiges Rendering unterstützen.

## Einrichtung

### Voraussetzungen

* Python 3.x
* pip (Python-Paketinstallationsprogramm)

### Installation

1.  Klonen Sie das Repository.
2.  Navigieren Sie zum Repository-Verzeichnis.
3.  Installieren Sie die erforderlichen Python-Pakete:

    ```bash
    pip install -r requirements.txt
    ```

### Lokales Ausführen

1.  Führen Sie die Flask-Anwendung aus:

    ```bash
    python index.py
    ```
2.  Die API ist unter der angegebenen Adresse (normalerweise `http://127.0.0.1:5000`) verfügbar.

### Bereitstellung auf Vercel

1.  Installieren Sie die Vercel-CLI.
2.  Stellen Sie die Anwendung mit Vercel bereit. Die Datei `vercel.json` ist so konfiguriert, dass alle Anforderungen an `/api/index` umgeleitet werden.

## Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert.

# Générateur de Clés SSH

[🇺🇸 English](README.md) | [🇫🇷 Français](README_fr.md) | [🇯🇵 日本語](README_ja.md) | [🇨🇳 简体中文](README_zh-cn.md) | [🇩🇪 Deutsch](README_de.md) | [🇪🇸 Español](README_es.md)

Ce projet est une API simple qui génère des paires de clés Ed25519. Il utilise Flask côté serveur pour générer les clés et fournit les clés publique et privée via une réponse JSON.

## Fonctionnalités

* **Génération de Clés :** Génère des paires de clés SSH Ed25519.
* **Point de Terminaison API :** Fournit un point de terminaison API (`/generate`) pour générer la paire de clés.
* **Compatibilité :** Les clés SSH générées sont adaptées à une utilisation avec des plateformes comme GitHub, GitLab et Bitbucket.

## Explication

La génération sécurisée de clés SSH implique des opérations cryptographiques complexes. La mise en œuvre de ces opérations directement en JavaScript dans un environnement de navigateur est beaucoup plus complexe et pose des problèmes de sécurité. Par conséquent, ce projet utilise Python avec la bibliothèque `cryptography` pour gérer la génération de clés côté serveur.

Bien que les plateformes sans serveur comme Cloudflare Workers soient excellentes pour déployer du JavaScript, elles ne sont pas conçues pour exécuter directement du code Python. Par conséquent, ce projet est configuré pour un déploiement sur Vercel, qui prend en charge les fonctions sans serveur Python. Cela nous permet d’utiliser Python pour la génération sécurisée de clés. Les clés générées peuvent ensuite être utilisées pour s’authentifier auprès de plateformes d’hébergement de code populaires comme GitHub, GitLab et Bitbucket, ce qui simplifie le processus de configuration pour les développeurs. La structure du projet est flexible et les utilisateurs peuvent l’adapter pour un déploiement sur d’autres plateformes comme Netlify qui prennent en charge les fonctions backend ou le rendu côté serveur.

## Configuration

### Prérequis

* Python 3.x
* pip (gestionnaire de packages Python)

### Installation

1.  Clonez le dépôt.
2.  Naviguez jusqu’au répertoire du dépôt.
3.  Installez les packages Python requis :

    ```bash
    pip install -r requirements.txt
    ```

### Exécution Locale

1.  Exécutez l’application Flask :

    ```bash
    python index.py
    ```
2.  L’API sera disponible à l’adresse spécifiée (généralement `http://127.0.0.1:5000`).

### Déploiement sur Vercel

1.  Installez l’interface de ligne de commande Vercel.
2.  Déployez à l’aide de Vercel. Le fichier `vercel.json` est configuré pour réécrire toutes les requêtes vers `/api/index`.

## Licence

Ce projet est sous licence MIT.

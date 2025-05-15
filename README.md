# SSH Key Generator

[🇺🇸 English](README.md) | [🇫🇷 Français](README_fr.md) | [🇯🇵 日本語](README_ja.md) | [🇨🇳 简体中文](README_zh-cn.md) | [🇩🇪 Deutsch](README_de.md) | [🇪🇸 Español](README_es.md)

This project is a simple API that generates Ed25519 key pairs. It uses Flask on the backend to generate the keys and provides the public and private keys via a JSON response.

## Features

* **Key Generation:** Generates Ed25519 SSH key pairs.
* **API Endpoint:** Provides an API endpoint (`/generate`) to generate the key pair.
* **Compatibility:** The generated SSH keys are suitable for use with platforms like GitHub, GitLab, and Bitbucket.

## Explanation

Generating SSH keys securely involves complex cryptographic operations. Implementing these operations directly in JavaScript within a browser environment is significantly more complex and poses security considerations. Therefore, this project leverages Python with the `cryptography` library to handle the key generation on the server-side.

While serverless platforms like Cloudflare Workers are excellent for deploying JavaScript, they are not designed to run Python code directly. Consequently, this project is configured for deployment on Vercel, which supports Python serverless functions. This allows us to use Python for the secure key generation. The generated keys can then be used to authenticate with popular code hosting platforms like GitHub, GitLab, and Bitbucket, streamlining the setup process for developers. The project's structure is flexible, and users can adapt it for deployment on other platforms like Netlify that support backend functions or server-side rendering.

## Setup

### Prerequisites

* Python 3.x
* pip (Python package installer)

### Installation

1.  Clone the repository.
2.  Navigate to the repository directory.
3.  Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

### Running Locally

1.  Run the Flask application:

    ```bash
    python index.py
    ```
2.  The API will be available at the specified address (usually `http://127.0.0.1:5000`).

### Deployment to Vercel

1.  Install the Vercel CLI.
2.  Deploy using Vercel. The `vercel.json` file is configured to rewrite all requests to `/api/index`.

## License

This project is licensed under the MIT License.

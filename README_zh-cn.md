# SSH 密钥生成器

[🇺🇸 English](README.md) | [🇫🇷 Français](README_fr.md) | [🇯🇵 日本語](README_ja.md) | [🇨🇳 简体中文](README_zh-cn.md) | [🇩🇪 Deutsch](README_de.md) | [🇪🇸 Español](README_es.md)

本项目是一个简单的 API，用于生成 Ed25519 密钥对。它在后端使用 Flask 生成密钥，并通过 JSON 响应提供公钥和私钥。

## 功能

* **密钥生成:** 生成 Ed25519 SSH 密钥对。
* **API 终结点:** 提供一个 API 终结点 (`/generate`) 来生成密钥对。
* **兼容性:** 生成的 SSH 密钥适用于 GitHub、GitLab 和 Bitbucket 等平台。

## 说明

安全地生成 SSH 密钥涉及复杂的加密操作。在浏览器环境中直接使用 JavaScript 实现这些操作非常复杂，并且存在安全隐患。因此，本项目利用 Python 和 `cryptography` 库在服务器端处理密钥生成。

虽然 Cloudflare Workers 等无服务器平台非常适合部署 JavaScript，但它们并非设计用于直接运行 Python 代码。因此，本项目配置为部署在支持 Python 无服务器函数的 Vercel 上。这使我们能够使用 Python 进行安全的密钥生成。然后，生成的密钥可用于在 GitHub、GitLab 和 Bitbucket 等流行的代码托管平台上进行身份验证，从而简化开发人员的设置过程。项目的结构非常灵活，用户可以对其进行调整，以便部署在支持后端函数或服务器端渲染的 Netlify 等其他平台上。

## 设置

### 准备工作

* Python 3.x
* pip (Python 包安装程序)

### 安装

1.  克隆存储库。
2.  导航到存储库目录。
3.  安装所需的 Python 包：

    ```bash
    pip install -r requirements.txt
    ```

### 在本地运行

1.  运行 Flask 应用程序：

    ```bash
    python index.py
    ```
2.  API 将在指定的地址 (通常为 `http://127.0.0.1:5000`) 上可用。

### 部署到 Vercel

1.  安装 Vercel CLI。
2.  使用 Vercel 进行部署。`vercel.json` 文件配置为将所有请求重写到 `/api/index`。

## 许可证

本项目根据 MIT 许可证获得许可。

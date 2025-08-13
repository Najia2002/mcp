# 🧠 MCP avec Groq (Model Context Protocol)

Ce projet permet de créer une **interface d’intelligence artificielle** basée sur Groq (LLaMA3), capable de comprendre des questions et d’exécuter des actions automatisées, comme **bloquer une IP** ou effectuer une requête **Whois**, via un serveur FastAPI.

---

## 🚀 Fonctionnalités

- ✅ Compréhension des intentions via Groq API.
- ✅ Exécution automatique d’actions (`block_ip`, `whois`, etc.).
- ✅ Communication client ↔️ serveur via HTTP.
- ✅ Extensible avec de nouvelles actions.

---

## 🧱 Structure du projet

```
mcp_project/
│
├── mcp/
│   ├── client/
│   │   ├── groq_client.py       # Gère les appels à Groq
│   │   └── mcp_client.py        # Point d’entrée côté utilisateur
│   │
│   └── server/
│       └── server.py            # Serveur FastAPI (réception et exécution des actions)
│
├── requirements.txt             # Dépendances du projet
└── README.md                    

---

## ⚙️ Installation


```

1. Installe les dépendances :

```bash
pip install -r requirements.txt
```

2. Lance le serveur FastAPI :

```bash
uvicorn mcp.server.server:app --reload
```

3. Utilise le client :

```bash
python mcp/client/mcp_client.py
```

---

## 🔑 Configuration

Avant de lancer le client, assure-toi d’avoir une **clé API Groq** valide 

## 🧪 Exemple d’utilisation

```
💬 Ta question : Peux-tu bloquer l’IP 8.8.8.8 ?
📦 Interprétation Groq : {"action": "block_ip", "params": {"ip": "8.8.8.8"}}
🚀 Action envoyée au serveur...
✅ Réponse : IP 8.8.8.8 bloquée avec succès.
```

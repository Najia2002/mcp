import requests
from groq_client import GroqClient

# Remplace par ta clé API Groq
groq_api_key = "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"
groq_client = GroqClient(groq_api_key)

def ask_mcp(question: str):
    print("Envoi à Groq pour interprétation...")
    parsed = groq_client.interpret_question(question)
    print("Interprétation :", parsed)

    if not parsed or "action" not in parsed:
        print("Groq n’a pas pu interpréter la question.")
        print("Réponse LLM :", groq_client.simple_completion(question))  # réponse directe
        return

    url = "http://localhost:8000/react/execute"
    response = requests.post(url, json=parsed, timeout=10)

    if response.ok:
        result = response.json()
        # Si le serveur retourne une erreur "Unknown action"
        if isinstance(result, dict) and "error" in result and "Unknown action" in result["error"]:
            print("Action inconnue dans le serveur MCP.")
            print("Réponse LLM :", groq_client.simple_completion(question))  # réponse directe
        else:
            print("Réponse du serveur MCP :", result)
    else:
        print("Erreur serveur :", response.status_code, response.text)

# === Interface en ligne de commande ===
if __name__ == "__main__":
    while True:
        question = input("\n Ta question : ")
        if question.lower() in ["exit", "quit"]:
            break
        ask_mcp(question)

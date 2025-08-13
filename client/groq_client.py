from groq import Groq
import json

class GroqClient:
    def __init__(self, api_key):
        self.client = Groq(api_key=api_key)

    def interpret_question(self, question: str):
        prompt = f"""
Tu es un agent MCP. Ta tâche est de convertir la question de l'utilisateur en action JSON :
{{
  "action": "...",
  "params": {{ ... }}
}}

Exemples :
Q: Peux-tu bloquer l’IP 8.8.8.8 ?
A: {{
  "action": "block_ip",
  "params": {{ "ip": "8.8.8.8" }}
}}

Q: Qui est derrière google.com ?
A: {{
  "action": "whois",
  "params": {{ "domain": "google.com" }}
}}

Maintenant :
Q: {question}
A:
"""
        response = self.client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
            timeout=10
        )

        content = response.choices[0].message.content.strip()
        try:
            return json.loads(content)
        except json.JSONDecodeError:
            return {"raw_text": content}

    def simple_completion(self, question: str) -> str:
        """
        Renvoie une réponse texte libre du LLM.
        Utilisé quand l'action MCP est inconnue.
        """
        response = self.client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[{"role": "user", "content": question}],
            temperature=0.7,
            timeout=10
        )
        return response.choices[0].message.content.strip()

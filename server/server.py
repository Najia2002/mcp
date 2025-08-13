from fastapi import FastAPI, Request
import json

app = FastAPI()

# Charger les actions depuis config.json
with open("config.json") as f:
    actions_config = json.load(f)["actions"]

@app.post("/react/execute")
async def execute_action(request: Request):
    print("Requête reçue")
    data = await request.json()
    print("Contenu de la requête :", data)
    action_name = data.get("action")
    params = data.get("params", {})

    if action_name not in actions_config:
        return {"error": f"Unknown action: {action_name}"}

    required_params = actions_config[action_name].get("params", [])
    missing_params = [p for p in required_params if p not in params]
    if missing_params:
        return {"error": f"Missing parameters: {', '.join(missing_params)}"}

    # Actions simulées
    if action_name == "block_ip":
        return {"status": f"Blocked IP {params['ip']}"}
    elif action_name == "whois":
        return {"status": f"WHOIS data for {params['domain']}"}

    return {"status": f"Executed {action_name} with params {params}"}

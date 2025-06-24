import os
import requests
import yaml

SNYK_API = "https://api.snyk.io"
HEADERS = {
    "Authorization": f"token {os.environ['SNYK_TOKEN']}",
    "Content-Type": "application/vnd.api+json"
}

def list_projects():
    resp = requests.get(f"{SNYK_API}/rest/orgs/38bc7259-fb9b-4413-b69a-741f25d5d5bf/projects", headers=HEADERS)
    resp.raise_for_status()
    return [proj["attributes"]["name"] for proj in resp.json()["data"]]

def import_project(repo, branch):
    url = f"{SNYK_API}/rest/orgs/38bc7259-fb9b-4413-b69a-741f25d5d5bf/integrations/be0561b8-5c07-4ae4-853e-5acaf59967ea/import"
    payload = {
        "target": {
            "name": repo,
            "branch": branch
        }
    }
    resp = requests.post(url, json=payload, headers=HEADERS)
    if resp.status_code != 201:
        print(f"❌ Failed to import {repo}: {resp.status_code} {resp.text}")
    else:
        print(f"✅ Imported {repo}")

def main():
    with open("snyk-projects.yml") as f:
        projects = yaml.safe_load(f)["projects"]

    for proj in projects:
        repo = proj["name"]
        branch = proj.get("branch", "main")

        existing = list_projects()
        if proj["name"] in existing:
            print(f"✅ Project exists: {proj['name']}")
        else:
            print(f"🆕 Importing: {repo}")
            import_project(repo, branch)

if __name__ == "__main__":
    main()

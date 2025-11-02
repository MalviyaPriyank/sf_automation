import time
import base64
import json
from google.oauth2 import service_account
from googleapiclient import discovery

# CONFIGURATION
ORG_ID = "organizations/1234567890"
PROJECT_ID = "openflow-477018"
PROJECT_NAME = "OpenflowTest"
SERVICE_ACCOUNT_ID = "cloud-search-sa"
SERVICE_ACCOUNT_DISPLAY = "Cloud Search Service Account"
SERVICE_ACCOUNT_ROLES = [
    "roles/cloudsearch.serviceAgent",
    "roles/cloudsearch.user",
]
ADMIN_KEY_FILE = "admin_key.json"
SA_KEY_OUTPUT = "cloud_search_sa.json"

# Authenticate using an admin-level service account
admin_creds = service_account.Credentials.from_service_account_file(
    ADMIN_KEY_FILE,
    scopes=["https://www.googleapis.com/auth/cloud-platform"]
)
print("Authentication done")

# 1️⃣ Create the project
crm_service = discovery.build('cloudresourcemanager', 'v3', credentials=admin_creds)

print("Creating project...")
project_body = {
    "projectId": PROJECT_ID,
    "displayName": PROJECT_NAME,
    #"parent": {"type": "organization", "id": ORG_ID.split("/")[1]}
    "parent":ORG_ID,
    "tags": {
        "environment": "dev",   # or whatever your org requires
        "cost_center": "1234"   # example
    }
}
from googleapiclient import discovery
print("enable cloud resource manager API")
admin_project_id = "984368412433"  # the one from the error
serviceusage = discovery.build('serviceusage', 'v1', credentials=admin_creds)
serviceusage.services().enable(
    name=f"projects/{admin_project_id}/services/cloudresourcemanager.googleapis.com"
).execute()
print("Done")

print("Caller email:", admin_creds.service_account_email)


project = crm_service.projects().create(body=project_body).execute()
print(f"Project creation requested: {project['name']}")


# Wait until the project becomes active
def wait_for_project_ready(project_id):
    for i in range(20):
        p = crm_service.projects().get(name=f"projects/{project_id}").execute()
        if p["state"] == "ACTIVE":
            print("✅ Project is active.")
            return
        print("Waiting for project to become active...")
        time.sleep(5)
    raise TimeoutError("Project not activated in time.")

wait_for_project_ready(PROJECT_ID)

# 2️⃣ Enable the Cloud Search API
serviceusage = discovery.build('serviceusage', 'v1', credentials=admin_creds)
print("Enabling Cloud Search API...")
serviceusage.services().enable(
    name=f"projects/{PROJECT_ID}/services/cloudsearch.googleapis.com"
).execute()

print("✅ Cloud Search API enabled.")

# 3️⃣ Create a service account
iam_service = discovery.build('iam', 'v1', credentials=admin_creds)
print("Creating service account...")
sa = iam_service.projects().serviceAccounts().create(
    name=f"projects/{PROJECT_ID}",
    body={
        "accountId": SERVICE_ACCOUNT_ID,
        "serviceAccount": {"displayName": SERVICE_ACCOUNT_DISPLAY}
    }
).execute()

sa_email = sa["email"]
print(f"✅ Created service account: {sa_email}")

# 4️⃣ Create a service account key
print("Creating service account key...")
key = iam_service.projects().serviceAccounts().keys().create(
    name=sa["name"],
    body={"privateKeyType": "TYPE_GOOGLE_CREDENTIALS_FILE"}
).execute()

key_data = base64.b64decode(key["privateKeyData"])
with open(SA_KEY_OUTPUT, "wb") as f:
    f.write(key_data)

print(f"✅ Service account key saved to {SA_KEY_OUTPUT}")

# 5️⃣ Assign IAM roles to service account
print("Assigning IAM roles...")
policy = crm_service.projects().getIamPolicy(
    resource=PROJECT_ID,
    body={}
).execute()

bindings = policy.get("bindings", [])
for role in SERVICE_ACCOUNT_ROLES:
    found = next((b for b in bindings if b["role"] == role), None)
    if found:
        if f"serviceAccount:{sa_email}" not in found["members"]:
            found["members"].append(f"serviceAccount:{sa_email}")
    else:
        bindings.append({
            "role": role,
            "members": [f"serviceAccount:{sa_email}"]
        })

policy["bindings"] = bindings

crm_service.projects().setIamPolicy(
    resource=PROJECT_ID,
    body={"policy": policy}
).execute()

print("✅ Roles assigned successfully.")

# 6️⃣ Test using the new service account
print("Verifying service account credentials...")
from googleapiclient.discovery import build
from google.oauth2 import service_account

sa_creds = service_account.Credentials.from_service_account_file(
    SA_KEY_OUTPUT,
    scopes=["https://www.googleapis.com/auth/cloud_search.query"]
)

cloud_search = build('cloudsearch', 'v1', credentials=sa_creds)
print("✅ Cloud Search API client created successfully.")

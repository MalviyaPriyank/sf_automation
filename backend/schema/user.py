def individual_serial(user) -> dict:
  return {
    "id": str(user["_id"]),
    "name": str(user["name"]),
    "email": str(user["email"])
  }

def list_serial(users) -> list:
  return [individual_serial(user) for user in users]
def individual_serial(conversation) -> dict:
  return {
    "_id": str(conversation["_id"]),
    "userId": str(conversation["userId"]),
    "title": str(conversation["title"])
  }

def list_serial(conversations) -> list:
  return [individual_serial(conversation) for conversation in conversations]
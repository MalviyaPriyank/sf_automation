def individual_serial(message) -> dict:
  return {
    "_id": str(message["_id"]),
    "userId": str(message["userId"]),
    "role": str(message["role"]),
    "content": str(message["content"])
  }

def list_serial(messages) -> list:
  return [individual_serial(message) for message in messages]
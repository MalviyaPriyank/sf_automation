import asyncio
from fastapi import APIRouter, BackgroundTasks, HTTPException
from models.message import Message
from db.mongo import MongoService
import json
mongo_service = MongoService()
router = APIRouter()

# new imports start ==
from src.obj import session as snowflake_session
from services.data_agent import DataAgent
import logging
# new imports end ==

# async def enque_fake_reply(user_id: str):
#   await asyncio.sleep(5)
#   mongo_service.add_message(Message(userId=user_id, role="assistant", content="This is a delayed reply"))

logging.basicConfig(level=logging.WARNING, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logging.getLogger(__name__).setLevel(logging.INFO)

logger = logging.getLogger(__name__)

def build_agent():
  session_inst = snowflake_session.Session()
  session_inst.set_user('frosty')
  session_inst.set_password('Hellopehlaadmi@24')
  session_inst.set_account('kzekzkb-pm40264')
  session_state = session_inst.get_session()
  root = session_inst.get_root_object()
  return DataAgent(session_state=session_state, user_name="frosty", logger=logger, root=root)

@router.post("/message")
async def post_message(message: Message):
  try:
    mongo_service.add_message(message)
    logger.info("building agent")
    agent = build_agent()
    logger.info("build complete")
    agent.initialize_chat_history(message.content)
    reply_raw = agent.converse()                 # bytes/str like b'{"reply": "..."}'
    reply_obj = json.loads(reply_raw)
    reply_text = reply_obj.get("reply", "")
    assistant_msg = Message(userId=message.userId, role="assistant", content=reply_text)
    mongo_service.add_message(assistant_msg)
    return assistant_msg

  except Exception as e:
    logger.exception("agent error")
    raise HTTPException(status_code=500, detail="Agent processing failed") from e
  
@router.get("/message")
async def get(user_id: str):
  messages = mongo_service.get_message(user_id)
  return messages
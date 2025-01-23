import os
import sys
import boto3
from langchain_aws import ChatBedrock
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.embeddings import BedrockEmbeddings

sys.path.append(os.path.join(os.path.dirname(__file__),'../src'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../conf'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../schema'))
from conf import llm_config
from schema import streamlit_schema as ss
from src.utils import helper

class Bedrock:
    def __init__(self,
                 runtime=True,
                 region=llm_config.REGION,
                 temperature=llm_config.TEMPERATURE,
                 kb_model_id=llm_config.KB_MODEL_ID,
                 chat_model_id=llm_config.CHAT_MODEL_ID,
                 embeddings_model_id=llm_config.EMBEDDINGS_MODEL_ID):
        self.region = region
        self.temperature = temperature
        self.kb_model_id = kb_model_id
        self.chat_model_id = chat_model_id
        self.embeddings_model_id = embeddings_model_id
        self.client = boto3.client(llm_config.BEDROCK_RUNTIME_SERVICE, 
                                   aws_access_key_id=llm_config.ACCESS_KEY,
                                   aws_secret_access_key=llm_config.SECRET_KEY,
                                   region_name=self.region)
        self.embeddings_llm = BedrockEmbeddings(model_id=self.embeddings_model_id,
                                                client=self.client)
        self.kb_llm = ChatBedrock(model_id=self.kb_model_id,
                                  model_kwargs=dict(temperature=self.temperature),
                                  aws_access_key_id=llm_config.ACCESS_KEY,
                                  aws_secret_access_key=llm_config.SECRET_KEY,
                                  region_name=self.region)
        self.tools_config = llm_config.tools

    def converse(self,
                 messages):
        self.client = boto3.client(llm_config.BEDROCK_RUNTIME_SERVICE,
                                   aws_access_key_id=llm_config.ACCESS_KEY,
                                   aws_secret_access_key=llm_config.SECRET_KEY, 
                                   region_name=self.region)
        response = self.client.converse(
            modelId=self.chat_model_id,
            messages=messages,
            toolConfig=self.tools_config
        )
        output_message = response[ss.OUTPUT][ss.MESSAGE]
        content = output_message[ss.CONTENT]
        return content

    def create_kb(self,
                  docs,
                  tempdir='../../kb/'):
        split_docs = helper.chunk_split(docs=docs)
        vectorstore_faiss = FAISS.from_documents(documents=split_docs, embedding=self.embeddings_llm)
        vectorstore_faiss.save_local(folder_path=tempdir)
        return vectorstore_faiss, tempdir

    def get_retriever_obj(self):
        self.client = boto3.client(llm_config.BEDROCK_RUNTIME_SERVICE,
                                   aws_access_key_id=llm_config.ACCESS_KEY,
                                   aws_secret_access_key=llm_config.SECRET_KEY, 
                                   region_name=self.region)
        self.kb_llm = ChatBedrock(model_id=self.kb_model_id,
                                  model_kwargs=dict(temperature=self.temperature),
                                  aws_access_key_id=llm_config.ACCESS_KEY,
                                  aws_secret_access_key=llm_config.SECRET_KEY,
                                  region_name=self.region)
        
        faiss_obj = FAISS.load_local('kb/', self.embeddings_llm, allow_dangerous_deserialization=True)
        return RetrievalQA.from_chain_type(llm=self.kb_llm,
                                           retriever=faiss_obj.as_retriever())
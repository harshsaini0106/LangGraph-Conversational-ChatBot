from langgraph.graph import StateGraph,START,END
from typing import TypedDict,Annotated
from langchain_core.messages import BaseMessage
from langgraph.checkpoint.sqlite import SqliteSaver
from langchain_core.messages import HumanMessage
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langgraph.graph.message import add_messages
import sqlite3

from dotenv import load_dotenv
load_dotenv()
CONFIG = {'configurable': {'thread_id': 'thread-1'}}
llm=HuggingFaceEndpoint(
    repo_id='Qwen/Qwen2.5-7B-Instruct',
    task='text-generation'

)
model=ChatHuggingFace(llm=llm)


class ChatState(TypedDict):
    messages:Annotated[list[BaseMessage],add_messages]

def chat_node(state:ChatState):
    messages=state['messages']
    response=model.invoke(messages)
    return {'messages':[response]}

connection=sqlite3.connect(database='chatbot.db',check_same_thread=False)

checkpointer=SqliteSaver(conn=connection)

graph=StateGraph(ChatState)
graph.add_node('ChatNode',chat_node)
graph.add_edge(START,'ChatNode')
graph.add_edge('ChatNode',END)

chatbot=graph.compile(checkpointer=checkpointer)

# initial_state=chatbot.invoke({
#         "messages": [HumanMessage(content="hello")]
#     },
#     config=CONFIG)
# print(initial_state["messages"][-1].content)

def retrieve_all_threads():
    all_threads=set()
    for checkpoint in checkpointer.list(None):
        all_threads.add(checkpoint.config['configurable']['thread_id'])
    return list(all_threads)


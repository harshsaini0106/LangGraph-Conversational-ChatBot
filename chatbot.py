from langgraph.graph import StateGraph,START,END
from typing import TypedDict,Annotated
from langchain_core.messages import BaseMessage
from langgraph.checkpoint.memory import InMemorySaver
from langchain_core.messages import HumanMessage
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
# from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph.message import add_messages

from dotenv import load_dotenv
load_dotenv()
CONFIG = {'configurable': {'thread_id': 'thread-1'}}
llm=HuggingFaceEndpoint(
    repo_id='Qwen/Qwen2.5-7B-Instruct',
    task='text-generation'

)
model=ChatHuggingFace(llm=llm)

# model = ChatGoogleGenerativeAI(
#     model="gemini-2.5-fast",
#     temperature=0
# )


class ChatState(TypedDict):
    messages:Annotated[list[BaseMessage],add_messages]

def chat_node(state:ChatState):
    messages=state['messages']
    response=model.invoke(messages)
    return {'messages':[response]}

checkpointer=InMemorySaver()

graph=StateGraph(ChatState)
graph.add_node('ChatNode',chat_node)
graph.add_edge(START,'ChatNode')
graph.add_edge('ChatNode',END)

chatbot=graph.compile(checkpointer=checkpointer)

initial_state=chatbot.invoke({
        "messages": [HumanMessage(content="hello")]
    },
    config=CONFIG)
print(initial_state["messages"][-1].content)


# https://python.langchain.com/docs/modules/memory/types/buffer_window/
# memory (ConversationBufferWindowMemory)
from dotenv import load_dotenv
load_dotenv() 

from langchain_openai import ChatOpenAI
# ConversationChain : 대화 체인을 관리하는 데 사용됩니다.
from langchain.chains import ConversationChain
# ConversationBufferMemory : 대화 중 생성된 메모리를 관리
from langchain.memory import ConversationBufferWindowMemory

chat = ChatOpenAI(model_name="gpt-3.5-turbo-0125")

conversation = ConversationChain(llm=chat, memory=ConversationBufferWindowMemory(return_messages=False, k=3,))
print("[first question]")
print(conversation.invoke("뉴진스 맴버 1명 말해봐?")['response'])

print("\n[second question]")
print(conversation.invoke("다른 1명 더 말해봐?")['response'])

print("\n[third question]")
print(conversation.invoke("다른 1명 더 말해봐?")['response'])

print("\n[fourth question]")
print(conversation.invoke("지금까지 말한 뉴진스 맴버 다시 말해봐?")['response'])

print("\n[memory]")
print(conversation.memory.load_memory_variables({}))
# memory (ConversationBufferMemory)
from dotenv import load_dotenv
load_dotenv() 

from langchain_openai import ChatOpenAI
# ConversationChain : 대화 체인을 관리하는 데 사용됩니다.
from langchain.chains import ConversationChain
# ConversationBufferMemory : 대화 중 생성된 메모리를 관리
from langchain.memory import ConversationBufferMemory

chat = ChatOpenAI(model_name="gpt-3.5-turbo-0125")

print(chat.invoke("전세계의 국가중  GDP 상위 3개 국가는?").content)
print(chat.invoke("그 다음 3개 국가는?").content)

conversation = ConversationChain(llm=chat, memory=ConversationBufferMemory())
print("[first question]")
print(conversation.invoke("전세계의 국가중  GDP 상위 3개 국가는?"))

print("\n[second question]")
print(conversation.invoke("그 다음 3개 국가는?"))

print("\n[memory]")
print(conversation.memory.load_memory_variables({}))
# memory (chainBufferWindowMemory)
from dotenv import load_dotenv
load_dotenv() 

from langchain_openai import ChatOpenAI
from langchain.schema.runnable import RunnablePassthrough
from langchain.memory import ConversationSummaryBufferMemory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser

chat = ChatOpenAI(model_name="gpt-3.5-turbo-0125")

memory = ConversationSummaryBufferMemory(
    llm = chat, # LLM 설정
    max_token_limit=160, # 데이저 저장 Max 값 설정
    return_messages = True, # 결과값을 출력할지 설정, 기본 false 
)

prompt = ChatPromptTemplate.from_messages([
    ("system","You are a helpful AI talking to a human."),
    ("human","뉴진스가 누구야?"),
    ("ai", "뉴진스는 대한민국의 2022년 7월 22일, 데뷔한 ADOR 소속의 5인조 다국적 걸그룹입니다. 맴버는 민지, 하니, 다니엘, 해린, 혜인 이렇게 총 5명입니다."),
    MessagesPlaceholder(variable_name="history"),
    ("human","{question}")
])

def load_memory(_):
    return memory.load_memory_variables({})["history"]

chain = RunnablePassthrough.assign(history=load_memory) | prompt | chat | StrOutputParser()
def invoke_chain(question):
    result = chain.invoke({"question": question})
    memory.save_context(
        {"input": question},
        {"output": result}
    )
    return result

print("[first question]")
print(invoke_chain("뉴진스 맴버 1명 말해봐"))

print("\n[second question]")
print(invoke_chain("다른 1명 더 말해봐"))

print("\n[third question]")
print(invoke_chain("다른 1명 더 말해봐"))

print("\n[fourth question]")
print(invoke_chain("지금까지 말한 맴버 이름 말해봐"))
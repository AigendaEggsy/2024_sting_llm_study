from dotenv import load_dotenv
load_dotenv() 

from langchain.memory import ConversationSummaryBufferMemory
from langchain_openai import ChatOpenAI
from langchain.schema.runnable import RunnablePassthrough
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder

llm = ChatOpenAI(
    model_name="gpt-3.5-turbo-0125",   
    temperature=0.1
)

memory = ConversationSummaryBufferMemory(
    llm = llm,
    max_token_limit=80,
    return_messages = True,
)

prompt = ChatPromptTemplate.from_messages([
    ("system","You are a helpful AI talking to a human."),
    MessagesPlaceholder(variable_name="history"),
    ("human","{question}")
])

def load_memory(_):
    return memory.load_memory_variables({})["history"]

chain = RunnablePassthrough.assign(history=load_memory) | prompt | llm

def invoke_chain(question):
    result = chain.invoke({"question": question})
    memory.save_context(
        {"input": question},
        {"output": result.content}
    )
    print(memory.load_memory_variables({})["history"])
    print(result.content)

invoke_chain("전세계의 국가중 GDP 상위 3개 국가는?")
invoke_chain("그다음 국가는 뭐야?")
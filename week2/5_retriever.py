from dotenv import load_dotenv
load_dotenv()

from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough
from langchain.memory import ConversationSummaryBufferMemory
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder

vectorstore = FAISS.load_local(
    "FAISS_DB_INDEX",
    OpenAIEmbeddings(),
    allow_dangerous_deserialization=True
)

retriever = vectorstore.as_retriever()

chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

memory = ConversationSummaryBufferMemory(
    llm = chat,
    max_token_limit=160,
    return_messages = True, 
)

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a helpful assistant. \
        Answer questions using only the following context. \
        If you don't know the answer just say you don't know, \
        don't make it up:\n\n{context}",
    ),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{question}",),
])

def load_memory(*_):
    return memory.load_memory_variables({})["history"]

chain = (
    {
        "context":retriever,
        "question":RunnablePassthrough(),
        "history": load_memory,
    }
    | prompt
    | chat
    | StrOutputParser()
)

def invoke_chain(question):
    result = chain.invoke(question)
    memory.save_context(
        {"input": question},
        {"output": result}
    )
    return result

print(invoke_chain("뉴진스 맴버 1명 말해봐"))
print(invoke_chain("다른 1명 더 말해봐"))
print(invoke_chain("다른 1명 더 말해봐"))
print(invoke_chain("지금까지 말한 맴버 이름 말해봐"))
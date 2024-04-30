# Langchain 시작하기
# 참고 : https://python.langchain.com/docs/get_started/quickstart/

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(
    model_name="gpt-3.5-turbo-0125",
    temperature = 0.1
)

llm.invoke("how can langsmith help with testing?")

print(llm)

from langchain_core.prompts import ChatPromptTemplate
# 참조 : https://api.python.langchain.com/en/latest/prompts/langchain_core.prompts.chat.ChatPromptTemplate.html

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a world class technical documentation writer."),
    ("user", "{input}")
])

# chain.invoke({"input": "how can langsmith help with testing?"})
# chain = prompt | llm

from langchain_core.output_parsers import StrOutputParser

output_parser = StrOutputParser()

chain = prompt | llm | output_parser

# print(chain)
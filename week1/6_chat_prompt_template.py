# 6. ChatPromptTemplate
from dotenv import load_dotenv
load_dotenv() 

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate # 챗 프롬프트 생성하는 메서드
from langchain_core.output_parsers import StrOutputParser

chat = ChatOpenAI(model_name="gpt-3.5-turbo-0125")

template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a geography expert. And you only reply in {language}."), # 모델에게 사람이 지시하는 메시지
        ("ai", "Hi my name is {name}!"), # AI의 출력 메시지
        ("human", "What is the distance between {country_a} and {country_b}. Also, what is your name?"), # 사람이 입력하는 메시지
    ]
)

# 템플릿 내부에 변수값을 집어 넣어 완벽한 템플릿을 만듬
prompt = template.format_messages(
    language = "Korean",
    name = "Hyoin",
    country_a = "Korea",
    country_b = "USA"
)

print(f"\n[template]\n{template}\n")
print(f"[prompt]\n{prompt}\n\n")
print(chat.invoke(prompt).content)

# Quiz : LCEL Chaining을 사용해서 결과 작성하기
# chain =
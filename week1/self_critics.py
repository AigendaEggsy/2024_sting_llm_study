from dotenv import load_dotenv

load_dotenv()

from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain_experimental.smart_llm import SmartLLMChain

hard_question = "한 사람이 1입방미터의 구멍을 파는데 3일이 걸린다면, 그런 구멍을 30개 파는데 30명이 얼마나 걸릴까?"

prompt = PromptTemplate.from_template(hard_question)
llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo-0125")

chain = SmartLLMChain(
    ideation_llm=ChatOpenAI(temperature=0.9, model_name="gpt-4-turbo"),
    critique_llm=ChatOpenAI(temperature=0.9, model_name="gpt-3.5-turbo-16k-0613"),
    resolver_llm=ChatOpenAI(temperature=0.9, model_name="gpt-3.5-turbo"),
    prompt=prompt,
    n_ideas=3,
    verbose=True,
)

chain.run({})



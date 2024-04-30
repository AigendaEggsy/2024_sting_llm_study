# autogent 사용하기
from autogen import ConversableAgent
from dotenv import load_dotenv
import os

load_dotenv()

cathy = ConversableAgent(
    "cathy",
    system_message="네 이름은 'cathy'야. 너는 상상력이 풍부한 대학생이고 물리학을 정말 싫어해. 고집이 강한 편이고 너의 생각을 잘 바꾸려 하지 않아.",
    llm_config={"config_list": [{"model": "gpt-3.5-turbo-0125", "temperature": 0.9, "api_key": os.environ.get("OPENAI_API_KEY")}]},
    human_input_mode="NEVER",  # Never ask for human input.
)

joe = ConversableAgent(
    "joe",
    system_message="네 이름은 'joe'야. 너는 물리학 교수야. 물리를 싫어하는 사람에게 어떻해서든 물리학을 좋아하게 만들기위해 여러 재미있는 과학적 스토리를 이야기해.",
    llm_config={"config_list": [{"model": "gpt-3.5-turbo-0125", "temperature": 0.1, "api_key": os.environ.get("OPENAI_API_KEY")}]},
    human_input_mode="NEVER",  # Never ask for human input.
)

result = joe.initiate_chat(cathy, message="Cathy, 물리학을 좋아해?", max_turns=5)


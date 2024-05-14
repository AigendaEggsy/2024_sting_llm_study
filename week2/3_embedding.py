from dotenv import load_dotenv
load_dotenv() 

# https://platform.openai.com/docs/guides/embeddings
# https://api.python.langchain.com/en/latest/embeddings/langchain_community.embeddings.openai.OpenAIEmbeddings.html
from langchain_openai import OpenAIEmbeddings # OpenAI 임베딩 모델

embeddings_model = OpenAIEmbeddings()

# OpenAI 임베딩 모델을 사용하여 Text -> Vector DB화
embeddings = embeddings_model.embed_documents(
    [
        '안녕하세요!',
        '어! 오랜만이에요',
        '이름이 어떻게 되세요?',
        '날씨가 추워요',
        'Hello LLM!'
    ]
)

print(len(embeddings), len(embeddings[0]))
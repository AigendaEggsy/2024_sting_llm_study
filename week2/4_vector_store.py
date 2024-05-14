from dotenv import load_dotenv
load_dotenv()

from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import bs4

loader = WebBaseLoader(
    web_paths=("https://ko.wikipedia.org/wiki/NewJeans",),
    bs_kwargs=dict(
        parse_only=bs4.SoupStrainer("div", attrs={"id": ["bodyContent"]},)
    ),
)
docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 500,
    chunk_overlap  = 100,
    length_function = len,
)

splits = text_splitter.split_documents(docs)

# Vector Store
from langchain_openai import OpenAIEmbeddings # OpenAI 임베딩 모델
from langchain_community.vectorstores import FAISS # FAISS vectorstores

vectorstore = FAISS.from_documents(documents=splits, embedding=OpenAIEmbeddings())

# # 로컬에 저장
# DB_INDEX = "FAISS_DB_INDEX"
# vectorstore.save_local(DB_INDEX)

# # 로컬에서 불러오기
# new_db = FAISS.load_local(
#     DB_INDEX,
#     OpenAIEmbeddings(),
#     allow_dangerous_deserialization=True
# )

print(vectorstore)

query = '뉴진스 맴버는 누구야?'
# similarity_search : 메서드는 주어진 쿼리 문자열에 대해 벡터 스토어 내의 문서들 중에서 가장 유사한 문서들을 찾아내는 작업
docs = vectorstore.similarity_search(query)

for doc in docs:
    print(docs)
    print("========================================")
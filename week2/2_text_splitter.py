from langchain_community.document_loaders import WebBaseLoader
import bs4

loader = WebBaseLoader(
    web_paths=("https://ko.wikipedia.org/wiki/NewJeans",),
    bs_kwargs=dict(
        parse_only=bs4.SoupStrainer("div", attrs={"id": ["bodyContent"]},)
    ),
)
docs = loader.load()

# https://wikidocs.net/231430
from langchain_text_splitters import CharacterTextSplitter, RecursiveCharacterTextSplitter

# CharacterTextSplitter : 주어진 텍스트를 문자 단위로 분할
text_splitter = CharacterTextSplitter(
    separator = '',
    chunk_size = 500,
    chunk_overlap  = 100,
    length_function = len,
)

# RecursiveCharacterTextSplitter : 문자 리스트(['\n\n', '\n', ' ', ''])의 문자를 순서대로 사용하여 텍스트를 분할
# text_splitter = RecursiveCharacterTextSplitter(
#     chunk_size = 500,
#     chunk_overlap  = 100,
#     length_function = len,
# )

# docs를 설정된 청크사이즈로 분리
splits = text_splitter.split_documents(docs)

for split in splits:
    print(split)
print(len(splits))
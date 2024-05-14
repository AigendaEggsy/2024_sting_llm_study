# https://python.langchain.com/v0.1/docs/integrations/document_loaders/
# https://python.langchain.com/v0.1/docs/integrations/document_loaders/web_base/
from langchain_community.document_loaders import WebBaseLoader
import bs4

# 추출할 url 등록
url = "https://ko.wikipedia.org/wiki/NewJeans"

# WebBaseLoader : 특정 웹 페이지의 내용을 로드하고 파싱하기 위해 설계된 클래스
# 참고 : https://wikidocs.net/231644
loader = WebBaseLoader(
    # web_paths : 매개변수는 로드할 웹 페이지의 URL을 단일 문자열 또는 여러 개의 URL을 시퀀스 배열로 지정
    web_paths=(url,),
    # bs_kwargs : BeautifulSoup을 사용하여 HTML을 파싱할 때 사용되는 인자들을 딕셔너리 형태로 제공
    bs_kwargs=dict(
        # bs4.SoupStrainer : 특정 클래스 이름을 가진 HTML 요소만 파싱
        parse_only=bs4.SoupStrainer(
            "div",
            attrs={"id": ["bodyContent"]},
        )
    ),
)

docs = loader.load()

print(docs[0].page_content)



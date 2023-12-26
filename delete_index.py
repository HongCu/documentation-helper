import pinecone
import os
from dotenv import load_dotenv

load_dotenv()
# "75770cb4-5a42-4941-be7a-6dfc55a78157"
# "gcp-starter"
# medium-blogs-embeddings-index
def del_index():
    pinecone.init(
        api_key=os.environ["PINECONE_API_KEY"],
        environment=os.environ["PINECONE_ENVIRONMENT_REGION"]
        )
    # Pinecone Index 객체 생성
    index = pinecone.Index("medium-blogs-embeddings-index")

    # 인덱스 삭제
    index.delete()


print(del_index())
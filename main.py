from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()


def main():
    model = "models/text-embedding-004"
    embeddings = GoogleGenerativeAIEmbeddings(model=model)
    prompt = "技術記事のタイトルをよしなに生成してくがるAIの名称を考えてください。"
    embedding = embeddings.embed_documents([prompt])
    print(embedding)


if __name__ == "__main__":
    main()

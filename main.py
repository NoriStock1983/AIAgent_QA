import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

# .envファイルから環境変数を読み込む
load_dotenv()

def main():
    # ChatGoogleGenerativeAIクラスをインスタンス化します
    embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")
    prompt = "技術記事のタイトルをよしなに生成してくがるAIの名称を考えてください。"
    embedding = embeddings.embed_documents([prompt])
    print(embedding)

if __name__ == "__main__":
    main()

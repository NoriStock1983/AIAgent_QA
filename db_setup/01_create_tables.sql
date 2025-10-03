CREATE EXTENSION IF NOT EXISTS vector;


CREATE TABLE qa_order (
    id SERIAL PRIMARY KEY,
    main_category_code VARCHAR(4) NOT NULL,
    main_category_name VARCHAR(255) NOT NULL,
    sub_category_code VARCHAR(4) NOT NULL,
    sub_category_name VARCHAR(255) NOT NULL,
    question TEXT NOT NULL, -- 質問事項
    contents TEXT NOT NULL, -- 回答内容 
    embedding vector(768) ,
    metadata JSONB NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
)
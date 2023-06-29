#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   api.py
@Time    :   2023/06/28 23:24:29
@Author  :   Yida Hu
@Version :   1.0
@Desc    :   None
"""
from langchain import FAISS
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from configs.model_config import embedding_model_dict, vector_store_path
from loader.txt_loader import UnstructuredTxtLoader
from fastapi import FastAPI, UploadFile, File
from pathlib import Path

model_name = embedding_model_dict['text2vec-base']
model_kwargs = {'device': 'cpu'}
embeddings = HuggingFaceEmbeddings(model_name=model_name,
                                   model_kwargs=model_kwargs)
loader = UnstructuredTxtLoader()
app = FastAPI()

doc_search = None


@app.post("/uploadfile/")
async def upload_file(file: UploadFile = File(...)):
    # 指定上传文件的保存路径
    data_folder = Path("data")
    data_folder.mkdir(exist_ok=True)

    # 异步地将上传的文件保存到磁盘
    file_path = data_folder / file.filename
    contents = await file.read()
    with open(file_path, 'wb') as f:
        f.write(contents)

    # 从data目录下读取文件
    texts = loader.pdf_txt(file_path)
    global doc_search
    doc_search = FAISS.from_texts(texts, embeddings)
    # vector_store = FAISS.from_documents(texts, embeddings)
    # vector_store.save(vector_store_path)
    # 这里file_contents变量包含了文件的内容，你可以进一步处理或存储它
    return {"filename": file.filename, "content_length": len(texts)}


@app.post("/query/")
async def query(query: str):
    # vector_store = FAISS.load(vector_store_path)
    chain = load_qa_chain(OpenAI(), chain_type="stuff")
    docs = doc_search.similarity_search(query)
    answer = chain.run(input_documents=docs, question=query)
    return {"answer": answer, "documents": docs}
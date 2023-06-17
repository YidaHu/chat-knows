#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   search.py
@Time    :   2023/05/30 22:58:00
@Author  :   Yida Hu
@Version :   1.0
@Desc    :   None
"""
from langchain import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from configs.model_config import embedding_model_dict

from loader.txt_loader import UnstructuredTxtLoader

model_name = embedding_model_dict['text2vec-base']
model_kwargs = {'device': 'cpu'}
embeddings = HuggingFaceEmbeddings(model_name=model_name,
                                   model_kwargs=model_kwargs)

loader = UnstructuredTxtLoader()
texts = loader.pdf_txt("data/suzhou.txt")
# embeddings = OpenAIEmbeddings()

doc_search = FAISS.from_texts(texts, embeddings)
chain = load_qa_chain(OpenAI(), chain_type="stuff")
query = "苏州有哪些好玩的地方"
docs = doc_search.similarity_search(query)
answer = chain.run(input_documents=docs, question=query)
print(answer)
print(docs)

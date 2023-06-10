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

from loader.pdf_loader import UnstructuredPaddlePDFLoader

model_name = "roberta-large-nli-stsb-mean-tokens"
model_kwargs = {'device': 'cuda'}
embeddings = HuggingFaceEmbeddings(model_name=model_name, model_kwargs=model_kwargs)

loader = UnstructuredPaddlePDFLoader()
texts = loader.pdf_txt("java-interview.pdf")
# embeddings = OpenAIEmbeddings()
# embeddings = HuggingFaceEmbeddings()

docsearch = FAISS.from_texts(texts, embeddings)
chain = load_qa_chain(OpenAI(), chain_type="stuff")
query = "Java的特性"
docs = docsearch.similarity_search(query)
answer = chain.run(input_documents=docs, question=query)
print(answer)
print(docs)

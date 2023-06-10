#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   pdf_loader.py
@Time    :   2023/05/27 19:18:53
@Author  :   Yida Hu
@Version :   1.0
@Desc    :   None
"""

from PyPDF2 import PdfReader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import ElasticVectorSearch, Pinecone, Weaviate, FAISS

from textsplitter.ali_text_splitter import AliTextSplitter


class UnstructuredPaddlePDFLoader():
    """Loader that uses unstructured to load pdf files."""

    def pdf_txt(self, filepath):
        """Convert pdf to txt file."""
        reader = PdfReader(filepath)
        raw_text = ''
        for i, page in enumerate(reader.pages):
            text = page.extract_text()
            if text:
                raw_text += text
        # text_splitter = CharacterTextSplitter(
        #     separator="\n",
        #     chunk_size=1000,
        #     chunk_overlap=200,
        #     length_function=len,
        # )
        text_splitter = AliTextSplitter()
        texts = text_splitter.split_text(raw_text)
        return texts


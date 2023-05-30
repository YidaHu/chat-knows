#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   embedding.py
@Time    :   2023/05/30 22:48:22
@Author  :   Yida Hu
@Version :   1.0
@Desc    :   None
"""

from langchain.embeddings.huggingface import HuggingFaceEmbeddings

from typing import Any, List


class MyEmbeddings(HuggingFaceEmbeddings):
    def __init__(self, **kwargs: Any):
        super().__init__(**kwargs)
        
    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        """文本向量化，使用HuggingFace transformer model.

        Args:
            texts: 待向量文本集合.

        Returns:
            向量集合.
        """
        texts = list(map(lambda x: x.replace("\n", " "), texts))
        embeddings = self.client.encode(texts, normalize_embeddings=True)
        return embeddings.tolist()

    def embed_query(self, text: str) -> List[float]:
        """对Query进行文本向量，使用HuggingFace transformer model.

        Args:
            text: 待向量文本呢.

        Returns:
            向量文本.
        """
        text = text.replace("\n", " ")
        embedding = self.client.encode(text, normalize_embeddings=True)
        return embedding.tolist()

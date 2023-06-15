#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   txt_loader.py
@Time    :   2023/06/15 22:38:35
@Author  :   Yida Hu
@Version :   1.0
@Desc    :   None
"""


from textsplitter.ali_text_splitter import AliTextSplitter


class UnstructuredTxtLoader():
    """Loader that uses unstructured to load txt files."""

    def pdf_txt(self, filepath):
        """Convert txt to list."""
        raw_text = ''
        # 读取txt文件
        with open(filepath, 'r', encoding='utf-8') as f:
            raw_text = f.read()
        text_splitter = AliTextSplitter()
        
        texts = text_splitter.split_text(raw_text)
        return texts


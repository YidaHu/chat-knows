# chat-knows

EN | [中文文档](README.zh.md)

Chat-Knows is an intelligent question-answering service based on a local knowledge base. It leverages document vectorization and vector search techniques to provide accurate answers to questions and reference relevant documents.

## 📒Introduction

Chat-Knows combines knowledge and information from unstructured document collections with the ChatGPT conversational model to deliver more accurate and relevant responses. The system workflow is as follows:

- Allows you to chat with uploaded documents in formats such as PDF and Word using GPT capabilities.
- Intelligently divides the documents into smaller chunks and utilizes a powerful deep averaging network encoder to generate embeddings.
- Performs a semantic search on the content of the uploaded files, passing the most relevant embeddings to the LLM.
- Generates precise responses, including references to the sources of the information, which increases the credibility of the responses and helps quickly locate relevant information.

## 🔧Features

- Document Upload: Upload unstructured documents to the Chat-Knows repository.
- Vectorization: Convert uploaded documents into numerical vector representations.
- Vector Search: Efficient vector search and relevance ranking based on the vectorized document collection.
- ChatGPT Interface: Integration with the ChatGPT model to provide answer retrieval and access to reference documents.

## ❓How to Use

1. Clone the repository:

```shell
git clone https://github.com/YidaHu/chat-knows.git
```
2. Upload Documents: Upload your unstructured documents to the repository, ensuring they meet the supported format requirements.

3. Vectorization and Indexing: Use the provided tools and scripts to vectorize and index the uploaded documents.

4. Start ChatGPT: Configure the ChatGPT model and launch the chat interface.

5. Ask and Answer: Use the ChatGPT interface to ask questions to Chat-Knows and retrieve answers and related reference documents.

## 🪤Development and Deployment

### Running the Script for Testing

To experience the project, you can execute the following command to deploy the API using FastAPI

```shell
uvicorn api:app --reload
```
This will run a script named api.py and deploy the API using the FastAPI framework. The --reload flag enables automatic reloading of the application when code changes are detected.

## 💡Contribution
Contributions, issue reports, and improvement suggestions are welcome! If you wish to contribute code, please read the contribution guidelines and submit a pull request. If you find any issues or have any suggestions, please submit an issue.

Please ensure that your contributions adhere to the project's code of conduct and comply with the open-source license.

from llama_index import (
    SimpleDirectoryReader,
    ServiceContext,
    get_response_synthesizer,
)
from llama_index.indices.document_summary import DocumentSummaryIndex
from llama_index.llms import OpenAI
import openai
from pathlib import Path

#openai.api_key = "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"


def load_documents(documents_directory):
    document_titles = [str(path) for path in Path(documents_directory).glob("*")]
    documents = SimpleDirectoryReader(documents_directory).load_data()
    documents_ = []
    for document_title in document_titles:
        documents = SimpleDirectoryReader(input_files=[document_title]).load_data()
        documents[0].doc_id = document_title
        documents_.extend(documents)
    return documents_

def build_summary_index(documents_directory, llm_model="gpt-3.5-turbo"):
    print ("Building summary index from your documents")
    documents =  load_documents(documents_directory)
    chatgpt = OpenAI(temperature=0, model=llm_model)
    service_context = ServiceContext.from_defaults(llm=chatgpt, chunk_size=1024)
    response_synthesizer = get_response_synthesizer(
        response_mode="tree_summarize", use_async=True
    )
    doc_summary_index = DocumentSummaryIndex.from_documents(
        documents,
        service_context=service_context,
        response_synthesizer=response_synthesizer,
        show_progress=True,
    )
    return doc_summary_index

def get_document_summary(doc_summary_index, documents_directory, document_title):
    document_path = os.path.join(documents_directory, document_title)
    return doc_summary_index.get_document_summary(document_title)


def main():
    documents_directory = input("Enter documents directory name: ")
    openai.api_key = input("Enter OpenAI API key: ")
    doc_summary_index = build_summary_index(documents_directory)
    while True:
        document_title = input('Enter document title to get summary(or type "exit" to quit): ')
        if document_title.lower() == "exit":
            break
        print(get_document_summary(doc_summary_index, documents_directory, document_title))

if __name__ == "__main__":
    main()
from haystack.nodes import PDFToTextConverter, PreProcessor
from haystack import Document
import os

def load_documents_from_directory(directory_path):
    converter = PDFToTextConverter()
    preprocessor = PreProcessor(split_by="word", split_length=200, split_respect_sentence_boundary=True)

    documents = []
    for filename in os.listdir(directory_path):
        if filename.endswith(".pdf"):
            path = os.path.join(directory_path, filename)
            text = converter.convert(file_path=path, meta={"name": filename})
            docs = preprocessor.process([text])
            documents.extend(docs)
    return documents

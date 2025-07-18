# backend/haystack/document_loader.py
from haystack.nodes import PDFToTextConverter, PreProcessor
from haystack.document_stores import FAISSDocumentStore

def load_documents_from_directory(directory_path):
    converter = PDFToTextConverter(remove_numeric_tables=True, valid_languages=["en"])
    preprocessor = PreProcessor(
        clean_empty_lines=True,
        clean_whitespace=True,
        clean_header_footer=True,
        split_by="word",
        split_length=200,
        split_respect_sentence_boundary=True
    )

    documents = []
    for file in os.listdir(directory_path):
        if file.endswith(".pdf"):
            doc = converter.convert(file_path=os.path.join(directory_path, file), meta=None)
            processed_docs = preprocessor.process(doc)
            documents.extend(processed_docs)

    return documents

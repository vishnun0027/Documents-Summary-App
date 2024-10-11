from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader

def load_and_split_docs(url: str, chunk_size: int = 1000, chunk_overlap: int = 0):
    """
    Load documents from a URL and split them into chunks.

    Args:
        url (str): The URL to load documents from. Must be a string.
        chunk_size (int): The size of each chunk. Defaults to 1000.
        chunk_overlap (int): The overlap between chunks. Defaults to 0.

    Returns:
        list: A list of split documents.

    Raises:
        ValueError: If the provided URL is not a string or if no documents are found.
    """
    # Ensure that the URL is a string
    if not isinstance(url, str):
        raise ValueError("The URL must be a string.")

    # Load documents from the specified URL
    loader = WebBaseLoader(url)
    docs = loader.load()
    # Split the loaded documents into chunks
    text_splitter = CharacterTextSplitter.from_tiktoken_encoder(
        chunk_size=chunk_size, chunk_overlap=chunk_overlap
    )
    split_docs = text_splitter.split_documents(docs)
    print(f"Generated {len(split_docs)} documents.")
    return split_docs

# Example usage
# url = "https://arxiv.org/html/1706.03762v7"
# try:
#     split_documents = load_and_split_docs(url)
# except ValueError as e:
#     print(f"Error: {e}")

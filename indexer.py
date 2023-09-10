import os
import chardet
from bs4 import BeautifulSoup
from whoosh import index, qparser, searching
from whoosh.fields import Schema, ID, TEXT
import ctypes
print("Program is RUNNING")
# Set the directory where the index will be stored
index_dir = "index"

# Define the fields in the index schema
schema = Schema(doc_id=ID(stored=True), content=TEXT)

# Check if the index directory exists
if not os.path.exists(index_dir):
    # Create the index directory
    os.mkdir(index_dir)
    # Create a new index
    ix = index.create_in(index_dir, schema)
else:
    # Open the existing index
    ix = index.open_dir(index_dir)

# Open the index for writing
writer = ix.writer()

# Iterate through the documents in the "data" folder
for root, dirs, files in os.walk("data"):
    for file in files:
        # Open the document and read its content
        with open(os.path.join(root, file), "rb") as f:
            content = f.read()
        docID = root + "-" + file
        docID = docID.removeprefix("data\\")
        # Detect the encoding of the document
        encoding = chardet.detect(content)["encoding"]

        # If the encoding was not detected, use the default encoding
        if encoding is None:
            encoding = "iso-8859-1"

        # Decode the content using the detected or default encoding
        content = content.decode(encoding, errors="replace")

        # Parse the content as HTML using BeautifulSoup
        soup = BeautifulSoup(content, "lxml")

        # Extract the text content of the HTML document
        text = soup.get_text()

        # Add the extracted text to the index
        writer.add_document(doc_id=docID, content=text)


# Commit the changes to the index
writer.commit()
print("indexing is complete :) ")
MessageBox = ctypes.windll.user32.MessageBoxW
MessageBox(None, 'INDEXING COMPLETED', 'Python Indexer', 0)

from whoosh import index, qparser, scoring
from whoosh.fields import Schema, ID, TEXT
import ctypes
import os

index_dir = "index"
ix = index.open_dir(index_dir)

schema = Schema(doc_id=ID(stored=True), content=TEXT)
queries = [
    (401, "foreign minorities, Germany "),
    (402, "behavioral genetics"),
    (403 , "osteoporosis "),
    (404, "Ireland, peace talks"),
    (405, "cosmic events"),
    (406, "Parkinson's disease"),
    (407, "poaching, wildlife preserves"),
    (408, "tropical storms", ),
    (409, "legal, Pan Am, 103"), 
    (410, "Schengen agreement"),
    (411, "salvaging, shipwreck, treasure"),
    (412, "airport security"),
    (413, "steel production"),
    (414, "Cuba, sugar, exports"),
    (415, "drugs, Golden Triangle"),
    (416, "Three Gorges Project"),
    (417, "creativity "),
    (418, "quilts, income"),
    (419, "recycle, automobile tires"),
    (420, "carbon monoxide poisoning "),
]
with open("output.txt", "w") as f:
    # Create a parser for the "content" field
    parser = qparser.MultifieldParser(["content"], schema=schema)

    # Iterate through the search queries
    for query_id, query_str in queries:
        # Parse the query string
        query = parser.parse(query_str)
    
        # Search the index using the parsed query
        with ix.searcher(weighting=scoring.TF_IDF()) as searcher:
            results = searcher.search(query, limit=None)
            
            for rank, result in enumerate(results):
            # Extract the document ID and score
                doc_id = result["doc_id"]
                
                score = result.score
                # Write the result to the file
                f.write(f"{query_id} Q0 {doc_id} {rank+1} {score} GROUP4\n")

# Close the file
f.close()
MessageBox = ctypes.windll.user32.MessageBoxW
MessageBox(None, 'Search COMPLETED File can be found in ' + os.getcwd()+ "\\" + "output.txt", 'Python Searcher', 0)
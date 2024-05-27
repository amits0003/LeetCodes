class SearchEngine:
    def __init__(self):
        self.documents = {}  # Document ID to content mapping
        self.word_index = {}  # Word to document IDs and indexes mapping

    def add_document(self, doc_id, content):
        """
        Add a new document to the search engine.

        Parameters:
        - doc_id: Unique integer ID for the document.
        - content: Text content of the document.
        """
        self.documents[doc_id] = content.lower()
        self.update_word_index(doc_id, content.lower())

    def delete_document(self, doc_id):
        """
        Delete a document from the search engine.

        Parameters:
        - doc_id: Unique integer ID of the document to be deleted.
        """
        if doc_id in self.documents:
            content = self.documents[doc_id]
            del self.documents[doc_id]
            self.update_word_index(doc_id, content, delete=True)
            print(f"Document {doc_id} deleted.")
        else:
            print(f"Document {doc_id} not found.")

    def search_word(self, word):
        """
        Search for a specific word in the documents and report document IDs and word indexes.

        Parameters:
        - word: The word to search for.
        """
        word = word.lower()
        if word in self.word_index:
            print(f"Word '{word}' found in the following documents:")
            for doc_id, indexes in self.word_index[word].items():
                print(f"Document ID: {doc_id}, Indexes: {indexes}")
        else:
            print(f"Word '{word}' not found in any documents.")

    def update_word_index(self, doc_id, content, delete=False):
        """
        Update the word index based on the content of a document.

        Parameters:
        - doc_id: Unique integer ID of the document.
        - content: Text content of the document.
        - delete: Flag indicating whether to delete the document from the index.
        """
        words = content.split()
        for index, word in enumerate(words):
            word = word.lower()
            if word not in self.word_index:
                self.word_index[word] = {}

            if doc_id not in self.word_index[word]:
                self.word_index[word][doc_id] = []

            if not delete:
                self.word_index[word][doc_id].append(index)
            elif doc_id in self.word_index[word]:
                del self.word_index[word][doc_id]


def main():
    search_engine = SearchEngine()

    while True:
        command = input("Enter command (add, delete, search, exit): ").strip().lower()

        if command == "exit":
            break

        if command == "add":
            doc_id = int(input("Enter document ID: "))
            content = input("Enter document content: ")
            search_engine.add_document(doc_id, content)

        elif command == "delete":
            doc_id = int(input("Enter document ID to delete: "))
            search_engine.delete_document(doc_id)

        elif command == "search":
            word = input("Enter word to search: ")
            search_engine.search_word(word)

        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()

class StopWords:
    def __init__(self, filepath):
        """
        Args:
            filepath (str): Stopwords dosyasının yolu.
        """
        self.filepath = filepath
        self.stopwords = self.load_get_stopwords()

    def load_get_stopwords(self):
        """
        Returns:
            list: Stopwords'lerin listesi.
        """
        stopwords = []
        try:
            with open(self.filepath, 'r', encoding='utf-8') as file:
                stopwords = [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            print(f"File not found: {self.filepath}")
        except Exception as e:
            print(f"An error occurred: {e}")

        return stopwords

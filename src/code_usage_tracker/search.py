import re 


class SearchFile(object):
    def __init__(self, file_path, query):
        """
        initialising the ``SearchFile`` object
        """
        self.file_path = file_path
        self.query = query

    def search(self):
       
        try:
            with open(self.file_path, "r") as handle:
                document = handle.readlines()
            matches = 0
            for line in document:
                matches_ = re.findall(self.query.lower(), line.lower()) 
                matches += len(matches_)
            return matches
        except UnicodeDecodeError:
            return 0
        

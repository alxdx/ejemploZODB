import ZODB, ZODB.FileStorage

class Connection:
    def __init__(self):
        self.storage = ZODB.FileStorage.FileStorage('mydata.fs')
        self.db = ZODB.DB(self.storage)
    def getRoot(self):
        self.connection = self.db.open()
        self.root = self.connection.root()
        return self.root
    def getDB(self):
        return self.db
    def close(self):
        self.connection.close()
    

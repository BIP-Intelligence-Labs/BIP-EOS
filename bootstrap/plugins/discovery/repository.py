class DiscoveryRepository:
    def __init__(self):
        self.records=[]
    def save(self,url,document):
        self.records.append((url,document))
        return type("Record",(),{"url":url,"document":document})()

class APIService: #fake implementation, does not fetch data or upload data
    def upload(self, items):
        print("Uploading to API...")
        return True

    def download(self):
        print("Downloading from API...")
        return [] 
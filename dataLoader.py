import requests

class DataLoader:
    def __init__(self, url, filename):
        self.url = url
        self.filename = filename

    def download_file(self):
        response = requests.get(self.url)
        with open(self.filename, 'wb') as file:
            file.write(response.content)

    def parse_txt(self, variant_number):
        with open(self.filename, 'r') as file:
            lines = file.readlines()
        line = lines[variant_number].strip()
        parts = line.split()
        D = float(parts[1])
        fmin = float(parts[2])
        fmax = float(parts[3])
        return D, fmin, fmax
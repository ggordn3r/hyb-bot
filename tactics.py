class Tactics:
    def __init__(self) -> None:
        self.tactics = {}

    def load(self):
        import csv
        sheet = {}
        with open('tactics.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                sheet[row['Tactic']] = row['Description']
    
        self.tactics = sheet
    
    def draw(self):
        from random import choice
        # title, body = choice(list(self.tactics.items()))
        title = choice(list(self.tactics.keys()))
        body = self.tactics.get(title)
        return title, body

# if __name__ == "__main__":
#     parse_tactics()
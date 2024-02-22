from decrypt import extract_data
from dataset import data

val = extract_data(input("Enter Path: "))
text = ""

for value in val:
        value = int(value/40)
        if value in data.values():
            for key,  v in data.items():
                if v == value:
                     text = text + key          

print(text)

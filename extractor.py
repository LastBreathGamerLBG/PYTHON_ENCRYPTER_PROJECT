from convertor import convert

extract_data = []

def run(input, num):
    for i in range(len(input)):
        alpha  = input[i].lower()
        extract_data.append(alpha)
    convert(extract_data, num)
    
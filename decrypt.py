def extract_data(path):  
    file = path
    decrepted_data = []

    f = open(file,"r")
    encrypted = f.read()
    f.close()
    data_list = encrypted.split(",")
    
    if data_list[-1] == "":
        data_list.pop()

    for i in range(0, len(data_list)):
        result = data_list[i]
        decrepted_data.append(int(result))
    
    return decrepted_data
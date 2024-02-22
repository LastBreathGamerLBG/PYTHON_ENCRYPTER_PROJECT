from dataset import data

def convert(user, num):
    for i in user:
        if  i in data:
            result = data[i]*num
            f = open("encrypted.txt", "a")
            f.write(str(result)+",")
            f.close
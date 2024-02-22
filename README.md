#   PYTHON ENCRYPTER PROJECT

hello everyone this is a basic python encryptor which can encyrpt your text or whatever you want (make sure it is in dataset.py)

first download all files from github and extract it.

![1 png](https://github.com/LastBreathGamerLBG/PYTHON_ENCRYPTER_PROJECT/assets/160850941/00169ddc-23a0-47b7-8b5d-bc432386987a)

then open files in vs code or any code editor.

![Screenshot 2024-02-22 163430](https://github.com/LastBreathGamerLBG/PYTHON_ENCRYPTER_PROJECT/assets/160850941/51dfd3c5-b3b4-41bc-b451-1fe0374e6fcc)

in vs code open start_Encrypt.py and run it.

![Screenshot 2024-02-22 163459](https://github.com/LastBreathGamerLBG/PYTHON_ENCRYPTER_PROJECT/assets/160850941/963646c1-ba48-48c4-ba7d-bb1b63025b8d)

it will ask you to input text just type and hit enter whatever you want to encrypt😊😊😊

it will create a txt file of encrypted text in form of multiplied number of dataset.

![png2](https://github.com/LastBreathGamerLBG/PYTHON_ENCRYPTER_PROJECT/assets/160850941/0fd518df-fffe-4a24-82ac-cb6cab7a77c1)

for decrypting use start_Decrypt.py just give the path of encrypted txt file.

![Screenshot 2024-02-22 164036](https://github.com/LastBreathGamerLBG/PYTHON_ENCRYPTER_PROJECT/assets/160850941/a4b3ceed-e6e4-4956-8a15-790bb983b818)


# How does it works?

there is a dataset for every character

![3](https://github.com/LastBreathGamerLBG/PYTHON_ENCRYPTER_PROJECT/assets/160850941/4d1585ec-0923-4fb4-8306-356bb59bdc83)


what does it do is simple it first extract all character from the text as it is a big string and store them in a list.

![4](https://github.com/LastBreathGamerLBG/PYTHON_ENCRYPTER_PROJECT/assets/160850941/d16c773d-4eb0-4f7e-89a0-7e7438bfc246)

then check i character is in data name dictionary and if it is then store the character numberical value in a second list 
and write it by separating every character with "," in a text file.

![5](https://github.com/LastBreathGamerLBG/PYTHON_ENCRYPTER_PROJECT/assets/160850941/3d6cbb06-7a4b-4b73-ab36-e36393487528)


for decrypting it uses that text file and store all numbers as a big string (text) and uses that "," to seprate them and store
them in a list called "decrepted_data".

![6](https://github.com/LastBreathGamerLBG/PYTHON_ENCRYPTER_PROJECT/assets/160850941/f8900899-4793-46fd-a9b3-4a9a0a6a3e66)

and then we  store items of of data set list (named data) in a key, value and check our numbered data in value 
note here we have to first divide the numbered data by the number we multiply then check for key.

if key found just store text of key in a new variable and print that variable.




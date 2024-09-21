import os 
import hashlib
# firstly you need to set the variables like (size, Means How much size you set the bloom_filter)hash_range,file_name,also you set bit_of_arry for set all the size into zero then the variables compleate you need to generate hashes  when the hashes is generate you need to add the hashes value into 1 if it compleate then you need to save this file in txt form and also create a func for read then all done you need to create a check func when it run is check from the file.txt if it ==0 means it False if it True means The item Exist in the file.txt

SIZE=10000
HASH_RANGE=3
FILE_NAME='bllom_filter_data1.txt'
BIT_OF_ARRAY = [0] * SIZE
file_current_path=os.getcwd()
file_folder_name='Bloom_Filter'

def gen_hash(item):
    hash_values=[]
    for i in range(HASH_RANGE):
        has_value=int(hashlib.sha256(f'{item}{i}'.encode()).hexdigest(),16)% SIZE
        hash_values.append(has_value)
    return hash_values

def add(item):
    for hash_value in gen_hash(item):
        BIT_OF_ARRAY[hash_value] = 1
    
def check(item):
    for hash_value in gen_hash(item):
        if BIT_OF_ARRAY[hash_value] == 0:
            print(f'False')
            return False
    print(f'True')
    return True


def save():
    # x=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # a=''.join(map(str,x))
    # print(a)
    file_path=os.path.join(file_current_path,file_folder_name,FILE_NAME)
    with open(file_path,'w')as f:
        f.write(''.join(map(str,BIT_OF_ARRAY)))
    return file_path

def load(file_path):
    global BIT_OF_ARRAY
    if os.path.exists(file_path):
        with open(file_path,'r')as f:
            BIT_OF_ARRAY = list(map(int,f.read()))


load(os.path.join(file_current_path,file_folder_name,FILE_NAME))
email="nasiruddin"
if check(email):
    print('Exsist')
else:
    add(email)
    save()
    print('Value Added')


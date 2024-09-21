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
    # print(a) #output=[000000000]
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

################################### Advance Code ##########################
class Bloom_Filter:
    def __init__(self,size=1000,num_hash=3,file_name="Bloom_Filter_data.txt") -> None:
        self.size=size
        self.num_hash=num_hash
        self.file_name=file_name
        self.bit_arry=[0] * size
        self.folder_name = "Bloom_Filter"
        self.current_path=os.getcwd()
        self.load_filter(os.path.join(self.current_path,self.folder_name,self.file_name))
    def _hash(self,item):
        hash_values=[]
        for i in range(self.num_hash):
            hash_value=int(hashlib.sha256(f"{item}{i}".encode()).hexdigest(),16)%self.size
            hash_values.append(hash_value)
        return hash_values

    def add(self,item):
        for hash_value in self._hash(item):
            print(f"Setting bit at index: {hash_value}")
            self.bit_arry[hash_value] = 1
    def check(self,item):
        for hash_value in self._hash(item):
            if self.bit_arry[hash_value] == 0:
                return False
        return True

    def save_filter(self):
        file_path=os.path.join(self.current_path,self.folder_name,self.file_name)
        with open(file_path,'w')as f:
            f.write(''.join(map(str,self.bit_arry)))
        print(f"Filter saved to {file_path}")

    def load_filter(self,file_path):
        if os.path.exists(file_path):
            print(f"Loading filter from {file_path}")
            with open(file_path,'r')as f:
                self.bit_arry=list(map(int,f.read()))
        else:
            print(f"File {file_path} does not exist. Starting with a fresh filter.")
                
bloom_filter = Bloom_Filter(size=10000,num_hash=3)
email="sknasiruddin@gmail.com"
if bloom_filter.check(email):
    print('Exists')
else:
    bloom_filter.add(email)
    bloom_filter.save_filter()
    print('Value Added')

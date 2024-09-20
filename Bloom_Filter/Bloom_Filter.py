import os 
import hashlib
#``
class Bloom_Filter:
    def __init__(self,size=1000,num_hash=3,file_name="Bloom_Filter_data.txt") -> None:
        self.size=size
        self.num_hash=num_hash
        self.file_name=file_name
        self.bit_arry=[0] * size
        self.current_path=os.getcwd()
        self.load_filter(os.path.join(self.current_path,self.file_name))
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
        file_path=os.path.join(self.current_path,self.file_name)
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

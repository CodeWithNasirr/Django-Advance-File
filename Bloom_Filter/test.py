import os 
import hashlib
# firstly you need to set the variables like (size, Means How much size you set the bloom_filter)hash_range,file_name,also you set bit_of_arry for set all the size into zero then the variables compleate you need to generate hashes  when the hashes is generate you need to add the hashes value into 1 if it compleate then you need to save this file in txt form and also create a func for read then all done you need to create a check func when it run is check from the file.txt if it ==0 means it False if it True means The item Exist in the file.txt

class Bloom_filter:
    def __init__(self,size=10000,hash_range=3,file_name='test1.txt') -> None:
        self.size=size
        self.hash_range=hash_range
        self.file_name=file_name
        self.current_file=os.getcwd()
        self.bit_of_arry= [0] * size
        self.load(os.path.join(self.current_file,self.file_name))

    def gen_hash(self,item):
        hash_values=[]
        for i in range(self.hash_range):
            hash_value = int(hashlib.sha256(f"{item}{i}".encode()).hexdigest(),16) % self.size
            hash_values.append(hash_value)
        return hash_values
    
    def add(self,item):
        for hash_value in self.gen_hash(item):
            self.bit_of_arry[hash_value] = 1

    def check(self,item):
        for hash_value in self.gen_hash(item):
            if self.bit_of_arry[hash_value] == 0 :
                return False
        return True

    def save(self):
        file_path=os.path.join(self.current_file,self.file_name)
        with open(file_path,'w')as f:
            f.write(''.join(map(str,self.bit_of_arry)))
        print(f"Filter saved to {file_path}")
        return file_path
    def load(self,file_path):
        if os.path.exists(file_path):
            with open(file_path,'r')as f:
                self.bit_of_arry=list(map(int,f.read()))

bloom_filter=Bloom_filter()
email="masfgsgsdnasf"
if bloom_filter.check(email):
    print('Exists')
else:
    bloom_filter.add(email)
    bloom_filter.save()
    print('Value Add')

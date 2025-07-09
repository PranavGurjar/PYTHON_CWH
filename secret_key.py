import random
import string


def encode(key):
    if(len(key)<=3):
        return key[::-1]
    else:
        random_str1 = ''.join(random.choices(string.ascii_lowercase, k=3))
        random_str2 = ''.join(random.choices(string.ascii_lowercase, k=3))
        key = list(key)
        first_index = key[0]
        key.append(first_index)
        key.pop(0) 
        new_key = ''.join(key) 
        return random_str1+new_key+random_str2
    
    
def decode(encode_key):
    if len(encode_key)<=3:
        return encode_key[::-1]
        
    else:
        encode_key = list(encode_key)
        encode_key = encode_key[3:len(encode_key)-3]
        last_index = encode_key[-1]
        encode_key.insert(0, last_index)
        encode_key = encode_key[:len(encode_key)-1]
        decode_key = ''.join(encode_key) 
        return decode_key
        
        

key = input("Enter the secret key : ")

encode_key = encode(key)
print("Encode : ",encode_key)

decode_key = decode(encode_key)
print("Decode : ",decode_key)



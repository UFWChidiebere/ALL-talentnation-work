def rle_encode(text: str)-> str:
    if not text:
        return ""
    encoded = []
    i = 0
    while i < len(text):
        char = text[i]
        count = 0
        while i < len(text) and text[i] == char:
            count += 1
            i += 1
        encoded.append(char + str(count))
    return "".join(encoded)



def rle_decode(encoded: str)-> str:
    decoded = []
    i = 0
    while i < len(encoded):
        char = encoded[i]
        i += 1
        num_str = ""
        while i < len(encoded) and encoded[i].isdigit():
            num_str += encoded[i]
            i += 1
        decoded.append(char * int(num_str))
    return "".join(decoded)


'''this is the answer for the bonus part'''
def compression_ration(text: str) -> float:
    if not text:
        return 0.0
    return len(rle_encode(text)) / len(text) 

print(rle_encode("aaabbc"))        
print(rle_encode("aaaaaaaaaaaab")) 
print(rle_decode("a12b1"))         
print(rle_encode(""))              


print(' ' * 10)

print(compression_ration("aaabbc"))        
print(compression_ration("aaaaaaaaaaaab")) 
print(compression_ration("a12b1"))         
print(compression_ration(""))     

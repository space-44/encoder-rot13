import codecs
import asyncio

func = input("0 - encode; 1 - decode:  ")

def decode_text(j):
    h = codecs.decode(j, "rot13")
    print(h)
def encode_text(z):
    b = codecs.encode(z, "rot13")
    print(b)

async def main(x):
    if x == "0":
        enc_text = input("enter your text to encode:  ")
        encode_text(enc_text)
    if x == "1":
        dec_text = input("enter your text to decode:  ")
        decode_text(dec_text)
    
asyncio.run(main(func))
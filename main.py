# Imports
from time import sleep

# Function to encode the input
def encode(x):
    replacedict = {
        "a" : "p",
        "b" : "o",
        "c" : "n",
        "d" : "m",
        "e" : "f",
    }

    


# Function to decode the message and print
def decode(x):
    pass
# Function to take input
SelectType = input("Encode or Decode: ")
userin = input("Enter text: ")

# Decides whether encode or decode
if SelectType == "Encode" or "encode":
    encode(list(userin))
elif SelectType == "Decode" or "decode":
    decode(userin)
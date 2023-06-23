# Imports
from time import sleep

# Function to encode the input
def encode(x):
    pass

# Function to decode the message and print
def decode(x):
    pass
# Function to take input
userin = input("Enter text: ")
SelectType = input("Encode or Decode: ")

# Decides whether encode or decode
if SelectType == "Encode" or "encode":
    encode(userin)
elif SelectType == "Decode" or "decode":
    decode(userin)
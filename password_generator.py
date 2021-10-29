import random
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--small", action="store_true")
parser.add_argument("-c", "--capital", action="store_true")
parser.add_argument("-d", "--digit", action="store_true")
parser.add_argument("-S", "--symbol", action="store_true")
parser.add_argument("-l", "--length", default=0, type=int)

args = parser.parse_args()

if args.small==0 and args.capital==0 and args.digit==0 and args.symbol==0:
    args.small = 1
    args.capital = 1
    args.digit = 1
    args.symbol = 1
if args.length==0:
    args.length = 16
small = "abcdefghijklmnopqrstuvwxyz"
capital= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digit = "0123456789"
symbol = "~`!@#$%^&*()-=_+:;<>?,./"

string = ""
if args.small==1:
    string+=small
if args.capital==1:
    string+=capital
if args.digit==1:
    string+=digit
if args.symbol==1:
    string+=symbol
password = ""
for i in range(args.length):
    password+=random.choice(string)
print(password)
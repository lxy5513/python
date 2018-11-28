import argparse
parser = argparse.ArgumentParser()

parser.add_argument("-v", "--verbosity", help="increase output verbositya", dest='dest')
args = parser.parse_args()

## 有dest时用dest里面的值调用，没有时用长参数来调用 
#  print(args.verbosity) 
print(args.dest)

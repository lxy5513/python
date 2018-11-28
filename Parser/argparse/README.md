### `argparse.ArgumentParser`

來看看它的樣子:

```
ArgumentParser(prog=None, usage=None, description=None, epilog=None)
```

這邊我省略了一些很少用到的 keyword 參數。

- `prog` : program 的名字，你也可以以把它覆寫成任何你喜歡的字串。以例子來說，假設你是在 `example.py` 裡用了 `ArguemntParser` ，而且沒有特別指定 `prog` 是什麼的話 (也就是保持 `None`)， `prog` 會被自動指定成 `example.py` 。
- `usage` : 字串，主要是會顯示來告知使用者說應該怎麼使用你寫的 program (也就是 `example.py`)。保持 `None` 的話就會自動根據你設定的參數產生相對應的說明字串 (後面會解釋)。
- `description` : 字串，通常是一段簡短的說明，用來告知使用者說這個程式在做什麼。
- `epilog` : 字串，會出現在參數說明字串的最後面，通常是一些補充資料。 



### 加入參數

參數基本上分兩種，一種是位置參數 (positional argument)，另一種就是選擇性參數 (optional argument)，主要差別在於參數指定方式的不同 

#### optional arguments 

1. 一种是通过一个`-`来指定的短参数，如`-h`；

2. 一种是通过`--`来指定的长参数，如`--help`

   > 如果没有dest参数，就用长参数来调用传入的值 

#### action='store_ture'

单独出现时，只需指定参数，不需要传值 ---> 值是True  

出现两个时，命令互斥 只能指定一个参数



```python
from argparse import ArgumentParser
parser = ArgumentParser()

## 位置参数必须在选择性参数之前 且没有default， 用第一个参数来调用
parser.add_argument("pos1", help="positional argument 1")
## 选择性参数  有dest时用dest里面的值调用，没有时用长参数来调用 
parser.add_argument("-o", "--optional-arg", help="optional argument", dest="opt", default="default")

args = parser.parse_args()
print("positional arg:", args.pos1)
print("optional arg:", args.opt)
```







### `Parser.add_subparser`

``````python
#!/usr/bin/env python3
# coding: utf8
import sys
import subprocess
import argparse
from pathlib import Path

def ls(path, flags=None):
    if not flags:
        flags = []
    if ~path.is_dir() or ~path.exists():
        print(f'{path!s} does not exist or is not a directory')
        return 1
    cmd = ['ls'] + flags + [str(path)]
    return subprocess.call(cmd)
def man(what, n=1):
    cmd = ['man'] + [str(n)] + [what]
    return subprocess.call(cmd)
def echo(msg):
    print(msg)
    return 0

def _build_parser():
    parser = argparse.ArgumentParser()
    subcmd = parser.add_subparsers(
        dest='subcmd', help='subcommands', metavar='SUBCOMMAND')
    ## 
    subcmd.required = True

    # ls
    ls_parser = subcmd.add_parser('ls',
                                  help='listing given directory')
    ls_parser.add_argument('path',
                           type=Path,
                           help='path of the directory',
                           metavar='DIR')
    ls_parser.add_argument('--flag',
                           dest='flags',
                           help='flag for ls command (multiple flag)',
                           action='append')
    # man
    man_parser = subcmd.add_parser('man',
                                   help='show man page')
    man_parser.add_argument('what')
    man_parser.add_argument('-n', type=int, help='section number')

    # echo
    echo_parser = subcmd.add_parser('echo',
                                    help='echo a given message')
    echo_parser.add_argument('msg', help='the message', metavar='\'MESSAGE\'')
    return parser


if __name__ == '__main__':
    parser = _build_parser()
    args = parser.parse_args()

    if args.subcmd == 'ls':
        ret = ls(args.path, args.flags)
    elif args.subcmd == 'man':
        ret = man(args.what, n=args.n)
    else:
        ret = echo(args.msg)
``````





簡單說明一下:

1. 使用 `ArgumentParser.add_subparsers` 去建立一去建立一個 “group”，以這個例子來說，可以想像成 `ls_parser` 、 `man_parser` 和 `echo_parser` 都是這個 group 下的 parser
2. 使用 `subcmd` 這個 group 下的 `add_parser` 去建立 parser。回傳的會是一個 `ArgumentParser` ，所以 part 1 裡講得的東西通通能用 (甚至可以覆用這篇說的，在 subcmd 下加 subsubcmd….)，只是它定義的會是 `main.py <subcmd> ...` 裡的 `...` 會被怎麼 parse
3. 建立好 parser 之後，跟 part 1 一樣的流程使用，唯一不同的地方是要自己根據 `args.subcmd` 的值決定要 call 那個 function
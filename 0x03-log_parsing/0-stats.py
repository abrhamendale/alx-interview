#!/usr/bin/env python3
"""
Log parsing
"""


import sys
from time import sleep
import ipaddress
import re

ln = 0
t_size = 0
st_code = [200, 301, 400, 401, 403, 404, 405, 500]
st_count = [0, 0, 0, 0, 0, 0, 0, 0]
for lin in sys.stdin:
    if 'Exit' == lin.rstrip():
        break
    ln = ln + 1
    line = str(lin)
    c = 0
    ipaddr = ""
    dat = ""
    htm = ""
    st = ""
    fsize = ""
    valid = 1
    #print(line)
    for i in range(0, len(line)):
        c = c + 1
        if line[i] == ' ':
            break
        ipaddr = ipaddr + line[i]
    x = re.search("^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.?\b){4}$", ipaddr)
    if x:
        pass
    else:
        valid = 0
    #print("IP:",ipaddr)
    """
    IP
    """
    for i in range(c + 3, len(line)):
        c = c + 1
        if line[i] == ']':
            break
        dat = dat + line[i]
    x = re.search("r'\d{4}-\d?\d-\d?\d (?:2[0-3]|[01]?[0-9]):[0-5]?[0-9]:[0-5]?[0-9]'", dat)
    #print("Date:", dat)
    """
    DATE
    """
    for i in range(c + 5, len(line)):
        c = c + 1
        if line[i] == '\"':
            break
        htm = htm + line[i]
    if line[c] != ' ':
        valid = 0
    #print("htm:", htm)
    """
    HTML
    """
    c = c + 6
    st = st + line[c:c + 3]
    if line[c + 4] != ' ':
        valid = 0
    if int(st) not in st_code:
        valid = 0
    #print("st:", st)
    """
    Status code
    """
    for i in range(len(st_code)):
        if int(st) == st_code[i]:
            st_count[i] = st_count[i] + 1
    #print("Status check:", st_count)
    c = c + 4
    for i in range(c, len(line)):
        c = c + 1
        fsize = fsize + line[i]
    #print("size:", fsize)
    """
    File size
    """
    t_size = t_size + int(fsize)

    if ln % 10 == 0:
        print("File size:", t_size)
        print("200:", st_count[0])
        print("401:", st_count[1])
        print("403:", st_count[2])
        print("404:", st_count[3])
        print("405:", st_count[4])
        print("500:", st_count[5])
    #/d{1,3}/./d{1,3}/./d{1,3}/./d{1,3}/w/-/w/[]
    #/d{1,4}/-/d{1,2}/-/d{1,2}/t/d{1,2}/:/d{1,2}/:/d{1,2}/./d{1,6}
    #[2345][0][01345]

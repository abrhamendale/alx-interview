#!/usr/bin/python3
"""
Log parsing
"""


import sys
from datetime import datetime
import ipaddress
import re

ln = 0
t_size = 0
st_code = [200, 301, 400, 401, 403, 404, 405, 500]
st_count = [0, 0, 0, 0, 0, 0, 0, 0]
for line in sys.stdin:
    if 'Exit' == line.rstrip():
        break
    ln = ln + 1
    lin = str(line)
    c = 0
    ipaddr = ""
    dat = ""
    htm = ""
    st = ""
    fsize = ""
    valid = 1
    for i in range(0, len(lin)):
        c = c + 1
        if line[i] == ' ':
            break
        ipaddr = ipaddr + lin[i]
    """
    x = re.search("^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.?\b){4}$", ipaddr)
    """
    try:
        ipaddress.IPv4Network(ipaddr)
        pass
    except ValueError:
        pass
    """
    IP
    """
    for i in range(c + 3, len(lin)):
        c = c + 1
        if lin[i] == ']':
            break
        dat = dat + lin[i]
    try:
        res = bool(datetime.strptime(dat, "YYYY-MM-DD hh:mm:ss. ffffff"))
    except ValueError:
        res = False
    """
    x = re.search("r'\d{4}-\d?\d-\d?\d (?:2[0-3]|[01]?[0-9]):[0-5]?[0-9]:[0-5]?[0-9]'", dat)
    """
    """
    DATE
    """
    for i in range(c + 5, len(lin)):
        c = c + 1
        if lin[i] == '\"':
            break
        htm = htm + lin[i]
    if lin[c + 5] != ' ' or htm != "GET /projects/260 HTTP/1.1":
        valid = 0
    """
    HTML
    """
    c = c + 6
    st = st + lin[c:c + 3]
    if lin[c + 3] != ' ':
        valid = 0
    if int(st):
        pass
    else:
        continue
    """
    if st not in st_code:
        valid = 0
    print(valid)
    """
    """
    Status code
    """
    for i in range(len(st_code)):
        if int(st) == st_code[i]:
            st_count[i] = st_count[i] + 1
    c = c + 4
    for i in range(c, len(lin)):
        c = c + 1
        fsize = fsize + lin[i]
    """
    File size
    """
    t_size = t_size + int(fsize)

    if ln % 10 == 0 and valid == 1:
        print("File size:", t_size)
        for i in range(0, 8):
            if st_count[i]:
                print(str(st_code[i]) + ":", st_count[i])
    """
    /d{1,3}/./d{1,3}/./d{1,3}/./d{1,3}/w/-/w/[]
    /d{1,4}/-/d{1,2}/-/d{1,2}/t/d{1,2}/:/d{1,2}/:/d{1,2}/./d{1,6}
    [2345][0][01345]
    """

# N0PSctf 2025
by A.Tao

## Read the Bytes! - 50 / Reverse, 101

> Look who's there! New students! Fine, this time we will focus on reverse engineering. This could help you against PwnTopia one day!  
> I give you now a Python program and its output. Try to understand how it works!  
> Author: algorab  
> appendix file: [challenge.py](./challenge.py)


## Solution
- 將challenge.py第8行起各行的字串，去除「#」符號。
- 剩下的字元視為10進位數值，複製到[CyerChef]( https://gchq.github.io/CyberChef/ )。
- 使用「From Decimal」operation，設定Delimiter為CRLF，將10進位數值轉成ASCII字元，可得flag
- Flag: B4BY{4_Ch4raC73r_1s_Ju5t_4_nUm83r!}

## Reference
- [CyerChef]( https://gchq.github.io/CyberChef/ )
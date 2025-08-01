# N0PSctf - 2025
###### Contributed by [@scott987](https://github.com/scott987)

## A515 / MISC

> We just received this sign from Foreniego, one of the wanderers of Pwntopia. He's known for drifting between Topias, never settling down, and always leaving behind a few secrets. We've been told there's something hidden in the sign he sent us, maybe it holds a clue that will help in the steps ahead. Can you uncover the truth he's hiding?
> HINTS
> This data seems to have to be rearranged…
>
> [BLUE.png](https://raw.githubusercontent.com/isip-hs-whoami/CTF-writeup/refs/heads/main/N0PSctf%202025/A515/Blue.png)

### Solution
根據提示猜測這張圖片的IDAT Chunk應該要重新排列，因此我參考了[這個的程式](https://github.com/lanjelot/ctfs/blob/master/scripts/stega/png-reorder-idats.py)，並測試產生出來的圖，程式碼如下：

```python=
# python2

import struct
import sys
from random import shuffle
from time import sleep

def crc32(data):
    #import binascii
    #return binascii.crc32(data)
    import zlib
    return zlib.crc32(data)

def read_chunk2(filename):
    import png
    f = png.Reader(filename)
    chunk = f.chunk(lenient=True)
   
    crc = (binascii.crc32(chunk[0] + chunk[1]) & 0xffffffff)
    raw = struct.pack(">L", len(chunk[1])) + chunk[0] + chunk[1] + struct.pack(">L", crc)
    return raw

def read_chunk(f):
    chk_len = f.read(4)
    if len(chk_len) == 0:
        return None
    size = struct.unpack('>I', chk_len)[0]
    chk_type = f.read(4)
    chk_data = f.read(size)
    chk_crc = f.read(4)
    assert struct.pack('>l', crc32(chk_type + chk_data)) == chk_crc
    return chk_type, chk_data, chk_len + chk_type + chk_data + chk_crc

with open('BLUE.png', 'rb') as f:
    header = f.read(8)
    idat = []
    end = None

    prefix = header
    while True:
        chunk = read_chunk(f)
        if chunk is None:
            break
        typ, data, raw = chunk
        print('got %s' % typ)
        if typ == 'IDAT':
            idat.append(raw)
        elif typ == 'IEND':
            end = raw
        else:
            prefix += raw

    order = [] 
    for i in order:
        prefix += idat[i]

    out = prefix
    for i in range(len(idat)):
        out += idat[i]
        out += end
        open(str(i) + '.png', 'wb').write(out)
        out = prefix
```

其中第67行 order是將正確的順序排列好，後面疊加其他IDAT chunk產出圖片，得到以下圖片：

![order 0](https://raw.githubusercontent.com/isip-hs-whoami/CTF-writeup/refs/heads/main/N0PSctf%202025/A515/order0.png)

可以發現第11個IDAT應該就是第一個排序，後續將order改成:
```python
order = [11]
```
得到下面這些圖，並可發現下個順序是第12個IDAT：

![order 1](https://raw.githubusercontent.com/isip-hs-whoami/CTF-writeup/refs/heads/main/N0PSctf%202025/A515/order1.png)

最後發現order的順序到第六個：
```python
order = [11,12,10,14,16,15]
```
就能獲得足夠的flag資訊：

![order 6](https://raw.githubusercontent.com/isip-hs-whoami/CTF-writeup/refs/heads/main/N0PSctf%202025/A515/order6.png)

最後得到flag:`N0PS{1M4G3_R3C0NSTRUC7I0N}`


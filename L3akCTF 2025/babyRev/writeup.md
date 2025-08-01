# L3akCTF - 2025
###### Contributed by [@scott987](https://github.com/scott987)

## babyRev / Rev

>They always give you strings challenges, we are not the same, we do better.
>
> [babyrev](https://github.com/isip-hs-whoami/CTF-writeup/blob/main/L3akCTF%202025/babyRev/babyrev)

### Solution
反編譯檔案後會發現單純就是替換式加密：

![reverse](https://github.com/isip-hs-whoami/CTF-writeup/blob/main/L3akCTF%202025/babyRev/reverse.png?raw=true)

因此簡單的將替換表的文字轉回即可：
```python=
a = input()

remap = {}
remap[0x61] = 0x71
remap[0x62] = 0x77
remap[99] = 0x65
remap[100] = 0x72
remap[0x65] = 0x74
remap[0x66] = 0x79
remap[0x67] = 0x75
remap[0x68] = 0x69
remap[0x69] = 0x6f
remap[0x6a] = 0x70
remap[0x6b] = 0x61
remap[0x6c] = 0x73
remap[0x6d] = 100
remap[0x6e] = 0x66
remap[0x6f] = 0x67
remap[0x70] = 0x68
remap[0x71] = 0x6a
remap[0x72] = 0x6b
remap[0x73] = 0x6c
remap[0x74] = 0x7a
remap[0x75] = 0x78
remap[0x76] = 99
remap[0x77] = 0x76
remap[0x78] = 0x62
remap[0x79] = 0x6e
remap[0x7a] = 0x6d

for i in a:
    if ord(i) in remap:
        print(chr(list(remap.keys())[list(remap.values()).index(ord(i))]), end="")
    else:
        print('_', end="")
```

最後得到flag:`L3AK{you_are_not_gonna_guess_me}`
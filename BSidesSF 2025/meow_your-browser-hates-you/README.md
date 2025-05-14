# BSidesSF 2025 CTF
 供稿 人： kevin 
# meow - 100  / Terminal , 101
 
> Terminal Challenges Welcome
> 
> Flag Path: /home/ctf/flag.txt
> Author: Daniel Pendolinio
> 
> Web Terminal: https://meow-203d6dfd.term.challenges.bsidessf.net (or socat STDIO,raw,echo=0,escape=0x03 TCP:meow-203d6dfd.challenges.bsidessf.net:4445)
>  
## Solution
這是一道簽到題, 直接開啟Web Terminal: 
ls後就可以看到flag.txt 

```
cat flag.txt
```

![image](https://hackmd.io/_uploads/B1alzOnJlx.png)


# your-browser-hates-you - 100  / Web , 101

We're pretty sure there's a flag on this page, but something is wrong with SSL and we can't get our browser to render it! Can you help?

(Note: you'll intentionally get an SSL error when you visit the page)
Author: ron
https://your-browser-hates-you-4a61071d.challenges.bsidessf.net

## Solution
這題的關鍵在於理解瀏覽器為何拒絕連線（SSL/TLS 錯誤）
可以用Python  requests 函式庫，並設定 verify=False

```
import requests
import warnings

# 忽略 requests 發出的 InsecureRequestWarning 警告 (可選)
from requests.packages.urllib3.exceptions import InsecureRequestWarning
warnings.simplefilter('ignore', InsecureRequestWarning)

url = "https://your-browser-hates-you-4a61071d.challenges.bsidessf.net"
 
    # 發送 GET 請求，關鍵是 verify=False 來忽略 SSL 驗證
response = requests.get(url, verify=False)
response.raise_for_status() # 檢查是否有 HTTP 錯誤 (如 404)

print(response.text)
```
 
![image](https://hackmd.io/_uploads/ry1cPOh1eg.png)


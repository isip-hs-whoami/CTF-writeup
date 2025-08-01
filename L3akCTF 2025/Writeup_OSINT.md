# L3akCTF 2025 
供稿 人： kevin 
![image](https://hackmd.io/_uploads/r1T00yV8gx.png)



# Mildly Disastrous 5ecurity  - 50  / Hash Cracking

> I hashed 3 passwords with MD5 - Can you crack them?
> 我用 MD5 對 3 個密碼進行了哈希處理 - 你能破解它們嗎？


> 53e182cbd4daa6680f1a7c7b85eba802 1bfcbffaf03174f022225a62ddf025a8 1853572d1b6ae6f644718a6b6df835f9
> 
> Use the rockyou.txt wordlist.
> Flag format: L3AK{pass1_pass2_pass3}
 ![image](https://hackmd.io/_uploads/Sk6wLIJUee.png)

 ## Solution
 
* 什麼是 MD5？ MD5 是一種「不可逆」的雜湊演算法，常用於密碼儲存。它能把任意長度的字串轉換成固定長度的雜湊值（32 個十六進位字元）。
* 為什麼可以破解？ 雖然 MD5 不可逆，但我們可以利用「字典檔」（例如 rockyou.txt）嘗試暴力比對，看看有哪些原始密碼的 MD5 值與目標雜湊吻合。
* 什麼是 rockyou.txt？ 它是常見的密碼清單，收錄了數百萬筆曾被洩漏的密碼，非常適合用來進行雜湊破解。

```python
import hashlib

# 三組目標雜湊值
target_hashes = [
    "53e182cbd4daa6680f1a7c7b85eba802",
    "1bfcbffaf03174f022225a62ddf025a8",
    "1853572d1b6ae6f644718a6b6df835f9"
]

# 儲存破解結果
cracked = {}

# 逐行讀取字典檔並進行比對
with open("rockyou.txt", "r", encoding="utf-8", errors="ignore") as f:
    for line in f:
        word = line.strip()
        hashed = hashlib.md5(word.encode()).hexdigest()
        if hashed in target_hashes:
            cracked[hashed] = word
            print(f"✔ 找到密碼：{hashed} -> {word}")
        if len(cracked) == len(target_hashes):
            break

# 組合 Flag 格式
if len(cracked) == len(target_hashes):
    passwords = [cracked[h] for h in target_hashes]
    flag = f"L3AK{{{'_'.join(passwords)}}}"
    print("🎉 成功破解所有密碼！")
    print("Flag:", flag)
else:
    print("❌ 有部分密碼尚未破解，請確認字典檔是否完整。")

```

* 使用 hashlib.md5() 將每個字典中的詞轉成 MD5 雜湊。
* 每轉一個詞，就與三組目標值比對看看是否一致。
* 找到吻合的，就記下對應的原始密碼。
* 當三組都破解成功，就依照題目格式印出 Flag。

![image](https://hackmd.io/_uploads/r1tHIIkUgl.png)

---



# Strange Transmission   - 50  / Hardware-RF

> I received this strange transmission and I'm not sure what to make of it! Weird beeps, static noise, then silence. Can you help me figure out what it all means?
> 我收到了這個奇怪的傳輸，我不確定該怎麼看待它！奇怪的嗶嗶聲，靜電噪音，然後是寂靜。你能幫我弄清楚這一切意味著什麼嗎？
![image](https://hackmd.io/_uploads/B1IcUWxIex.png)


## Solution
使用 Morse Code Adaptive Audio Decoder 網站
https://morsecode.world/international/decoder/audio-decoder-adaptive.html

將聲音上傳.可以得到
> O H W O W Y O U F O U N D O U R S E C R E T M O R S E C O D E A U D I O W E L L D O N E H E R E I S T H E F I R S T H A L F O F T H E F L A G L 3 A K O P E N B R A C K E T W E L C 0 M 3 U N D E R S C O R E T 0 U N D E R S C O R E T H 3 U N D E R S C O R E H 4 R D W 4 R 3 U N D E R S C O R E R F U N D E R S C O R E 

分析這段隱藏的訊息


好的，我們來一步步分析這段隱藏的訊息。
 

### 步驟 1: 解碼拼寫內容

我們將您提供的內容逐字翻譯：

*   `O H W O W` -> **OHWOW**
*   `Y O U F O U N D O U R S E C R E T M O R S E C O D E A U D I O` -> YOU FOUND OUR SECRET MORSE CODE AUDIO
*   `W E L L D O N E` -> WELL DONE
*   `H E R E I S T H E F I R S T H A L F O F T H E F L A G` -> **HERE IS THE FIRST HALF OF THE FLAG**
*   `L 3 A K` -> **L3AK**
*   `O P E N B R A C K E T` -> **{**
*   `W E L C 0 M 3` -> **WELC0M3** (這裡使用了Leet語，0取代O，3取代E)
*   `U N D E R S C O R E` -> **\_**
*   `T 0` -> **T0** (Leet語，0取代O)
*   `U N D E R S C O R E` -> **\_**
*   `T H 3` -> **TH3** (Leet語，3取代E)
*   `U N D E R S C O R E` -> **\_**
*   `H 4 R D W 4 R 3` -> **H4RDW4R3** (Leet語，4取代A，3取代E)
*   `U N D E R S C O R E` -> **\_**
*   `R F` -> **RF**
*   `U N D E R S C O R E` -> **\_**

### 步驟 2: 分析訊息結構

將上面解碼的內容組合起來，我們得到一段完整的訊息：

> "OHWOW YOU FOUND OUR SECRET MORSE CODE AUDIO WELL DONE. **HERE IS THE FIRST HALF OF THE FLAG**: L3AK{WELC0M3\_T0\_TH3\_H4RDW4R3\_RF\_"

訊息很清楚地告訴我們，`L3AK{WELC0M3_T0_TH3_H4RDW4R3_RF_` 是 FLAG 的**前半部分**。

### 步驟 3: 找出後半部分
 ![image](https://hackmd.io/_uploads/H1JloX5vee.png)
丟進audacity看頻譜

### 步驟 4: 組合完整的FLAG

現在我們將前半部分和後半部分組合起來：

*   **前半部分**: `L3AK{WELC0M3_T0_TH3_H4RDW4R3_RF_`
*   

因此，最終的 FLAG 是：

```
L3AK{WELC0M3_T0_TH3_H4RDW4R3_RF_c4teg0ry_w3_h0p3_you_h4ve_fun!}
```

 
 # Sunny Day   - 50  / OSINT

> https://geosint.ctf.l3ak.team/
> ![image](https://hackmd.io/_uploads/BJCCRYl8lx.png)

題目給的地點：https://maps.app.goo.gl/Jq9FU5F6iN8HfdnKA


 ## Solution
  L3AK{sUn5H1Ne_iN_L1ecHt3nSTe1n}
 先找找有用的線索
![image](https://hackmd.io/_uploads/H1vSk9eIxl.png)
![image](https://hackmd.io/_uploads/SJBDJclUll.png)
![image](https://hackmd.io/_uploads/S1J5y9gIex.png)
先找國旗
![image](https://hackmd.io/_uploads/B1Hp15lLxl.png)
再用google 以圖搜圖來找.
![image](https://hackmd.io/_uploads/ByXIbcg8lg.png)
定位後取得FLAG
![image](https://hackmd.io/_uploads/H1W2Zqx8ee.png)

# Lost Locomotives - 50  / OSINT
題目連結:[Link](https://geosint.ctf.l3ak.team/)

題目給的初如地點：[Link](https://maps.app.goo.gl/cQLAEqbpXrLxcMHZA)
https://maps.app.goo.gl/cQLAEqbpXrLxcMHZA
> ![image](https://hackmd.io/_uploads/Syj8fM-Llx.png)
> ![image](https://hackmd.io/_uploads/SyfazGWUel.png)
> ![image](https://hackmd.io/_uploads/Bk0YzfZIxx.png)
> ![image](https://hackmd.io/_uploads/BJ7ifM-Ulg.png)
 
 ## Solution
L3AK{cH00_Ch0o_1n_P3Ru}
先由火車下手.開始找.用google 以圖搜圖
![image](https://hackmd.io/_uploads/r1h7EG-Ilx.png)
這是在秘魯的馬丘比丘路途上的車站
在來找 923 火車還有車身的外觀
![image](https://hackmd.io/_uploads/H1th4MZ8lg.png)
![image](https://hackmd.io/_uploads/rJyzrfWLgx.png)
在google map 上找印加鐵路
![image](https://hackmd.io/_uploads/BkdJUMbUel.png)
找在河邊的車站就找到了
![image](https://hackmd.io/_uploads/SkhfRb-Uxx.png)


 # Mountain View   - 50  / OSINT

> https://geosint.ctf.l3ak.team/
> ![image](https://hackmd.io/_uploads/SJ8P_MZLge.png)
> ![image](https://hackmd.io/_uploads/B1qhOfWIgg.png)

 ## Solution
L3AK{y0sh1n0_HAs_gR3At_54KuRA_Bl0s5omS}
這是一塊很有名的牌子一找就找到一大堆了
![image](https://hackmd.io/_uploads/B1xmFfbUel.png)
![image](https://hackmd.io/_uploads/BJsJ_z-Ixl.png)

 # Grain of Truth  - 50  / OSINT

> https://geosint.ctf.l3ak.team/
> ![image](https://hackmd.io/_uploads/S1L2qG-Lgl.png)
> ![image](https://hackmd.io/_uploads/SkveozbLxe.png)
 ## Solution
一看就很有在地的親切, 首先找到電線桿.直接上台電查
https://linspace.somee.com/TPCToMap/
![image](https://hackmd.io/_uploads/rkxUjMbUgx.png)
![image](https://hackmd.io/_uploads/ryY5ifbLeg.png)
電線桿編號:K2812CB64


L3AK{Wh0_Kn3W_El3ctr1C_p0L3S_W3R3_so_Us3FuL!}
![image](https://hackmd.io/_uploads/SJjLcMZIle.png)



 # Elephant Enclosure   - 50  / OSINT

> https://geosint.ctf.l3ak.team/
> ![image](https://hackmd.io/_uploads/S1ddJQZIgx.png)
![image](https://hackmd.io/_uploads/BkH9Jm-Uxe.png)

 
 ## Solution
以最佳角度(舞台)來搜圖
![image](https://hackmd.io/_uploads/B1b7emZUee.png)
鎖定新加坡動物員
![image](https://hackmd.io/_uploads/Sy7wlmWLlg.png)
L3AK{E13ph4nTs_4R3_F4sT_AF_https://youtu.be/ccxNteEogrg}
 ![image](https://hackmd.io/_uploads/Skq5x7-Llg.png)



 




 

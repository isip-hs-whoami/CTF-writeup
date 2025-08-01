# L3akCTF 2025

---

Rewrited by A.Tao

# WhiteSpace - 50 / Misc
---
## Discription
Origin:  
> I used [this site](https://patorjk.com/software/taag/#p=display&f=3x5&t=Type%20Something%20) to make some ASCII art to save my super aswsome flag, but something happended and all the spaces got deleted and I lost it. Luckily, I do remember that the MD5 hash of my flag was  
> <font color=red>a7bf5f833c3e4ceff2e006ff801ec16b</font>, so maybe you can help me.  
> Author: sy1vi3  

Note:  
> 作者將 flag 利用[工具網站](https://patorjk.com/software/taag/#p=display&f=3x5&t=Type%20Something%20)轉成 ASCII art (2個字元為一組)，儲存時所有的空白字元都被移除，存檔結果如 [flag.txt](./flag.txt) 附件檔。已知 flag 的 MD5 編碼為 <font color=red>a7bf5f833c3e4ceff2e006ff801ec16b</font>。
---
## Solution
觀察：  
> - flag.txt 裡每 6 列一組，共有 42 組 ASCII art。因為每列最多 6 個字符，編碼的方式為 3x5 的 ASCII art，故每組應該可以解出 2 個字元。
> - 利用題目提供的網站測試及 flag.txt，發現第 1、2 組被編碼的字元應該分別是 "L3" 及 "AK"，另依 flag 格式要求，第 5 個及最後一個字元應該分別是 "{" 及 "}"。
> - 示範圖：<img src=./whitespace-1.jpg></img>

解題：  
> - 先建立 A-Za-z0-9_{} 的 3*5 ASCII art 對照表。  
> - 兩兩字元一組，組合 ASCII art。  
> - 找出 flag.txt 的 42 組 ASCII art 各是哪些雙字元的組合。組合結果如 [char_combine_1.txt](./char_combine_1.txt)。組合總數為：6,471,694,281,809,614,130,380,800。直接用 brute force 方法計算各組合的 MD5 太花時間。  
> - 再觀察 char_combine_1.txt 裡的組合，有大量的 "_" 與小寫字母、數字的組合，猜想 flag 可能有用 leet1337 mapping logic。經 ASCII art 的對照，可能的對應如下：  
>   1 <-> I, L  
>   4 <-> A  
>   3 <-> E  
>   5 <-> S  
>   7 <-> T  
>   0 <-> O  
> - 將 char_combine_1.txt 去除不可能的字元組合，結果如 [char_combine_2.txt](./char_combine_2.txt)。組合總數為：512,988,145,055,170,560。這個組合數還是太大。  
> - 手動重組可能的字元組合 (感覺是一句用 Leet 改寫)，最後組合出可能的部分 flag：L3AK{jus7_p4tt3rn_m4tch1ng_4t_f1rs7_bu7_th3n_y0u_n33d_4_，剩下的組合數為 794,787,840。直接用 brute force 方法計算各組合的 MD5 已可接受。  
> - 最後算出的 flag 為 L3AK{jus7_p4tt3rn_m4tch1ng_4t_f1rs7_bu7_th3n_y0u_n33d_4_h3ur1st1c_t0_n4rr0w_1t_d0wn}  
> - 原句是 just_pattern_matching_at_first_but_then_you_need_a_heuristic_to_narrow_it_down  
> - 翻譯為：一開始只是模式比對，但之後你需要啟發式方法來縮小範圍。  



---
## Reference
- ref-1: https://medium.com/@looyje/l3akctf-2025-whitespace-writeup-1e3dd4b110b8
- ref-2: https://medium.com/@random1106/l3ak-ctf-writeup-whitespace-30e88639ea27  

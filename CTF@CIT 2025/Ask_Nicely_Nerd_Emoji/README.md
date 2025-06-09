# CTF@CIT_2025

 供稿 人： kevin 
# Welcome to CTF@CIT! - 10  / Welcome
 
> Welcome to the second annual CTF@CIT!
> 
> Please remember to familarize yourself with the rules, check out our sponsors, but most importantly remember to have fun and learn something new this weekend!
> 
> The flag format for all challenges will be CIT{} unless noted otherwise
> 
> We are using dynamic scoring to automatically balance the point reward for every challenge. Each challenge will start with 1,000 points and will go down every solve. This point reduction will reduce points for everyone who has already solved the challenge too, so don’t worry if you see your points go down. This was used so the amount of solves on the challenge would determine how many points it’s worth instead of us arbitrarily choosing numbers. By the end of the competition, every challenge should be worth a fair amount of points depending on how difficult it is.
> 
> Flag: CIT{welcome2025} 
## Solution
這是一道簽到題, 題目直接給flag

```
Flag: CIT{welcome2025} 
```

# Discord - 10  / Welcome
 
> Join our Discord to stay up to date throughout the competition and be the first to hear about future events from the CIT team!
> 
> https://discord.gg/s6gXMAc95P
> 
> Flag: Hidden somewhere in Discord :)

## Solution
這是一道簽到題, discord 直接給flag
不過是Base64編碼格式呈現
所以還要做一下Base64 Decode 

![image](https://hackmd.io/_uploads/Bktk6u3kxl.png)


# Ask Nicely - 668  / Reverse
  
>  I made this program, you just have to ask really nicely for the flag!
 
題目附檔下載 :
https://drive.google.com/file/d/10ytDytvd29Updkrpvs3ZRc7YhtPOqecJ/view?usp=sharing

## Solution
使用IDA開啟 asknicely 

![image](https://hackmd.io/_uploads/rk1Ubthygx.png)

 
這題是測試能否理解反編譯後的 C++ 程式碼，弄清楚程式的執行流程，並找到程式裡藏著的特定字串。整個關鍵在於：程式會要求輸入兩次內容，但真正會用來做比較的只有第二次輸入，而且需要輸入完全正確的字串。

流程大概是這樣：
程式會先提示：「How badly do you want the flag?」。
這時候可以隨便輸入任何東西，甚至直接按 Enter，因為這個輸入到後面會被覆蓋。
接下來程式會出現提示：「Ask nicely...」。

這才是重點，這次的輸入必須是以下的完整字串，不能有任何錯誤： pretty pretty pretty pretty pretty please with sprinkles and a cherry on top

如果輸入的字串完全正確，程式就會回應：「Good job, I'm so proud of you!」，然後執行一個叫 give_flag 的函數，就看到目標 Flag。



# Nerd Emoji - 774  / Crypto
  
> Find the flag.
> Flag Format: CIT{example_flag} 

題目附檔下載 :
 https://drive.google.com/file/d/11oRAZYFNrrv7siVTfAFxLoZN0jsP2kvd/view?usp=sharing
 

## Solution
頻率分析法是一種破解加密密碼的技術，利用字母出現頻率來找出加密文本的規律。英文中，像字母 "E" 是最常見的，而 "Z" 出現得最少。透過分析加密文本中字母的頻率分布，再與英文的字母頻率對比，可以嘗試找出加密規則。

舉例來說，如果加密文本裡某個字母出現的頻率非常高，很可能它代表 "E"，因此可以推測加密方式的一部分內容。頻率分析的效果取決於加密規則是否足夠複雜，以及文本的長度是否足以提供有用的數據。若加密方式非常複雜或文本過短，破解的難度就會提高。
解題工具 Quipqiup 可以幫助進行頻率分析。

https://quipqiup.com/
本題目附的文字檔太多內容,造成onlie 工具無法操作
可以刪掉一半的文字內容, 就可以順利進行分析

![image](https://hackmd.io/_uploads/rJ9pmK2Jge.png)

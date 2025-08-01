# N0PSctf 2025
by A.Tao

## Tak Tak - 50 / OSINT, 101

> Alpha querid@s! ^^  
>
> It's finally time to dive into the fascinating world of OSINT, that magical word that excites digital detectives and gives regular folks the chills. Today, we'll be starting with the baaasic stuff: just a bit of reverse image searching to warm up!  
>
> Now, story time: Alice has stumbled into N0PStopia and found herself in a surreal place, lined edtirely with chairs.   
>
> Will you be able to figure out where this tunnel is, when it opened, and just for fun, how many chairs are in there? It seemed like it stretches into infinity.. X)  
>
> Flag format: B4BY{Place-Location_Opening-Date_chairs-number}  
>
> Example" B4BY{Lectures-Tower-N0PSTopia_June-1st-2005_505}  
>
> Author: Sto
>
> appendix file: [pic.jpg](./pic.jpg)


## Solution
- 將附件圖片上傳到ChatGPT，詢問照片中是哪個地方。得到最有可能的地方是「丹麥設計博物館（Designmuseum Danmark）」。
- 以「Designmuseum Danmark」為地點，詢問ChatGPT是什麼展覽。得到「椅子隧道」，展區共展示125張椅子。
- 詢問ChatGPT該展覽是何時開始開放參觀。得到「2024/6/7、2024/6/14、2024/6/19」三種答案。
- 將「Designmuseum Danmark」、「2024/6/7、2024/6/14、2024/6/19」及「125」組合成flag，皆不接受。
- 賽方的Discord上說名稱要用官網上的名稱「[Design Museum Damark](https://designmuseum.dk/en/)」，地名要用英文名稱「Demark」。
- 再次組合各種可能的flag，最終flag如下。
- Flag: B4BY{Designmuseum-Denmark_June-7th-2024_125}

## Reference
- [Hatena Blog]( https://yocchin.hatenablog.com/entry/2025/06/03/115500 )
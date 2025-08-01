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
```
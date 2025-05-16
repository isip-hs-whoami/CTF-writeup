# CTF@CIT - 2025
###### Contributed by @CXPhoenix

## Commit & Order: Version Control Unit - 782 / Web

> [!NOTE]
> 
> Challenge Description
> 
> "In software development, the repository is represented by two separate yet equally important branches..."
> 
> **Note**: this web challenge instance will reset every 30 minutes. If a challenge is not responsive, you might need to wait until the next half hour.

### Solution

剛看到這個題目時，看到關鍵字「repository」、「branches」，我~~未偵查先猜~~這很可能是個跟 Git 洩漏有關的挑戰。

所以我開啟了 Chrome 的 extension `dotGit` ，檢查是否有 `.git` 洩漏的情形。果然一打開， `dotGit` 就亮了💡，認證了網站確實存在可存取的 `.git` 目錄，並且**成功地下載**了完整的 Git 版本歷史紀錄。

下載後，我打開 VS Code 來檢查 commit 紀錄（對我 gui 狗），並查詢 diff 狀況。果然在 commit `changed it again` (`9b8bf13`) 找到一串奇怪的 base64 `Q0lUezVkODFmNzc0M2Y0YmMyYWJ9`。為什麼會認為是 base64....因為我已經搜尋過沒有 Flag 格式字串了...所以就往其他編碼格式找。 

拿到 Base64 編碼，立刻丟進 Cyberchef 中轉，然後就得到最終的 Flag `CIT{5d81f7743f4bc2ab}`。

---

### Referenece

* [Chrome Extension: dotGit](https://chromewebstore.google.com/detail/dotgit/pampamgoihgcedonnphgehgondkhikel?hl=zh-TW&utm_source=ext_sidebar)
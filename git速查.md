# Git 最小可用清单

> [!important] 先纠正一个认知
> **Git 不是"知识点"，是工具。** 代码和算法需要"理解"，git 只需要"用熟"。
> 你每天花 0.3h "学 git" 之所以难受，是因为它在没有真实场景时特别抽象
> （分支、合并、rebase 在没有协作需求时根本用不上）。
>
> 正确做法：**一次性学会下面 8 个命令，之后每天只是"用"，不再"学"。**

## 每天收工只要这 3 行

```bash
git add .
git commit -m "Day2: 素数判断 + gcd 两种写法"
git log --oneline -1          # 确认提交成功了
```

**就这三行。做完就算今天的 git 任务完成，不用再学新东西。**

## 真正需要会的 8 个命令

| 命令 | 什么时候用 | 频率 |
|---|---|---|
| `git status` | 不知道现在什么状态时，先看这个 | 每天 |
| `git add .` | 把改动放进暂存区 | 每天 |
| `git commit -m "说明"` | 存档 | 每天 |
| `git log --oneline` | 看看提交历史 | 每天 |
| `git diff` | 提交前看看改了什么 | 常用 |
| `git branch` / `git checkout -b 名字` | 开新分支 | 第 4 周 |
| `git push` | 推到 GitHub | 第 4 周 Day27 |
| `git restore 文件名` | 改崩了，恢复到上次提交的样子 | 救命用 |

**够了。剩下的（rebase、cherry-pick、submodule、reflog）现在一律不学**，遇到了再查。

## 救命命令（一定会用到）

```bash
# 改崩了，想放弃这次修改，回到上次提交
git restore 文件名

# 提交了但写错备注，或者忘加文件
git commit --amend -m "新的备注"

# 提交错了想撤销（保留改动）
git reset --soft HEAD~1
```

## commit 备注怎么写

```
Day2: 素数判断 + gcd 两种写法
Day5: 字典推导式练习
Day22: db.py 建表 + insert_document
```

格式：**Day几 + 做了什么**。别写 `update`、`修改`、`111`，将来你回看提交记录时会感谢自己。

## 什么时候才需要系统学

| 时间 | 学什么 |
|---|---|
| 现在 | 上面 8 个命令，够了 |
| 第 4 周 Day22 | `git checkout -b kb-dev` 开分支做项目 |
| 第 4 周 Day27 | `git remote add` + `git push` 推 GitHub |
| 寒假 / 面试前 | 补 merge、冲突解决、rebase（面试会问） |

> [!tip] 想一次性搞懂分支原理，用这个
> **Learn Git Branching**（learngitbranching.js.org，有中文，游戏化，网页版免费）
> 花一两个小时通关前几关，分支和合并的概念比看文档强十倍。
> 找一整个下午或晚上集中做，别每天挤 20 分钟。

#### 更改已提交的代码的 commit message
```commandline
修改最近的一次提交 
git commit -amend
保存后摁wq
修改历史提交
git rebase -i HEAD~N   N是需要修改代码的前一次提交
控制台编辑要修改的提交信息分支前的pick更改为r或reword
保存退出
弹出的控制台内输入要更改的提交信息后回车
或者git rebase -i 分支名

git rebase --continue
有冲突解决冲突，没有冲突就直接修改成功，再push上去
```
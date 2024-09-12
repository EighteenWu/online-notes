# git使用
#### 1、git rebase和git merage的区别?  
A：都是用于合并代码,其中git merage是保留历史提交记录,合并成一个新的分支再去提交,非线性历史;git rebase是不保留历史节点，线性历史,应用到某个分支;
#### 2、如何更改最近一次的commit信息？
````gitexclude
git commit -amend
````
#### 3、 如何更改已提交合并分支的commit信息？
```gitexclude
1、首先使用git log 查看历史记录和对用分支的哈希值;
git log
2、再使用git rebase变基到目标提交的父提交上
git rebase -i <哈希值>
3、找到对应的提交记录后，讲前面的pick改成edit;
5、运行git commit --amend更改提交信息
6、 git rebase --connitune 继续变基过程;
7、查看代码是否有冲突，手动处理冲突后，git add;然后push就行
```
#### 4、 代码回滚过吗，用的什么指令?
```gitexclude
回滚过，一般用git reset,然后里面有3个模式soft,一般用于撤销提交但保留更改,mixd
重置暂存区,但是保留工作目录中的更更更,hard就是放弃所有的，直接完全回滚到某个历史状态;
```

#### 5、**Jenkins构建流程？**

* Jenkins基本设置；管理员账户设置，系统基本设置，安装必要的插件;
* 创建Jenkins job组
* 创建pipline；
* 配置源代码管理工具，git或者svn，还有账号，代码库；
* 配置触发器，通知服务
* 编写构建脚本;
* 构建测试
* 如果有需要可以设置远程执行机
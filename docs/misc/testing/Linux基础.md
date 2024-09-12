# Linux基础
##### 问题归纳
1、如何查看系统版本信息？  
```commandline
uname -a
cat /proc/version
```
2、查看ip地址?
```commandline
ifconfig
```
3、查看磁盘剩余空间?
```commandline
df -ah
df 查看系统磁盘剩余指令, a查看所有文件系统,h以可读方式展示(主要是系统容量部分)
```
4、linux操作指令是什么样的规则?
```commandline
common[指令] options[-选项] parameter【参数】
大小写敏感  
无视多少个空格符号
一行指令，换行需要 \反斜杠跳脱
```
5、系统服务管理?
```commandline
service servicename[服务名] operation[操作，比如：restart-重启,start-启动,stop-停止,reload-重新加载配置,status-状态]
```
6、如何查看文件或者目录的大小?
```commandline
du -sh Crontab  
s显示整个目录或者文件的大小
h 可读形势
```
7、如何查看系统中开放的端口号?
```commandline
netstat -tupln
参数翻译:t显示tcp指令,u显示udp，p显示相关程序名，l显示正在监听，n不显示别名;
```
8、动态显示cpu占用?
```commandline
top指令
```
9、查询某个进程占用?
```commandline
ps -aux | grep php
显示php占用
```
10、ls和ll的区别?
```commandline
ls 是指令，显示当前目录下的文件
ll 是自定义指令，可以称为别名，实际是ls -l，以长文件格式化显示权限，所有者，大小
ls -al 显示所有，包括隐藏，link
ls -L 显示链接;
```
11、 系统小程序?
```commandline
nano test.txt  【简单的文本编辑器】
bc  【简单的计算器】
cal 【显示当前月份的日历】
date 【显示当前的日期】
```
12、文件目录权限？
```commandline
linux 系统内文件权限为所有者【owner】、Grup【群组】、other【他人】
新增目录默认权限为755，文件权限为644;
可以使用命令umask更改系统初始新增文件权限;即为所有者可读可写可执行，群组可读可执行，他人可读可执行;
更改权限为chomod 777 filename
更改文件群组为chgrp
更改文件所有者为chown
```
13、新建、复制、移动、删除文件或目录?
```commandline
touch filename 新增文件
mkdir dirname 新增目录
rmdir dirname  删除空目录
rm -rm 删除非空目录
cp root-filename target-flename 复制文件
nv root-file/dir  target-path  移动文件
```
14、查看文件？
```commandline
head -10 filename  查看文件头10行
tail -f filename  动态查看文件
less filename 按屏幕显示
cat filename  截取部分内容显示,后续一般跟着grep
```
15、杀死某个进程?
```commandline
ps -ef | grep 进程名
# e显示所有进程
# f 全格式显示进程信息，包括更多的字段
kill -9 pid  
### 或者使用
kill $(ps -ef |grep 'nginx' | grep -v grep | awk '(print $2)')
### 或者使用pkill和pgrep命令
pkill -9 nginx 命令
```

16、解压和压缩？
```commandline
tar -zcvf 压缩 z通过gzip程序压缩或者解压,c表示新的文件归档文件,v详细模式,f表示接下来的选项是文件名
tar -zxvf 解压 x表示提取文件
```


17、 linux下grep指令的使用？
命令的基本格式:
```commandline

grep [option] pattern file
```
常用的可选项:  
-A ： 除了显示符合范本样式的那一列，并显示之后的x行内容  
-B： 除了显示符合范本样式的那一列，并显示之前的x行内容  
-X： 除本行外，都显示  
-c： 统计匹配的行数   
-n:  仅显示匹配的的行号  
-v： 反向匹配  
-w： 匹配整个单词  
-e ：实现多个选项间的逻辑or 关系
假如我们有个名叫test的文件内容如下:
```commandline
aaaa
bbbbbbb
AAAaaa
BBBBASDABBDA
```
则`grep A2 aaaa test `输出的是:
```commandline
bbbbbbb
AAAaaa
```
`grep B1 AAAaaa test`输出的是:
```commandline
bbbbbbb
```
`grep -c aaa test`输出的是2行，匹配倒具体的行数；  
`grep -e aaaa -ebbbb test `匹配的是多对多的一个关系:
```commandline
aaaa
bbbbbbb
```

18、简单说说sed指令？  
`sed`指令例用脚本来处理文本文件。  
`sed [-hnV][-e<script>][-f<script文件>][文本文件]`  

参数说明：
* `-e`  以选项中指定的 script 来处理输入的文本文件，这个-e可以省略，直接写表达式。  
* `-f`<script文件>或--file=<script文件>以选项中指定的 script 文件来处理输入的文本文件。  
* `-h`或--help显示帮助。  
* `-n` 或 `--quiet` 或 `--silent` 仅显示 script 处理后的结果。
* `-V` 或 `--version` 显示版本信息。
* `-r` 开启正则匹配

动作说明：
* a：新增， a 的后面可以接字串，而这些字串会在新的一行出现(目前的下一行)～  
* c：取代， c 的后面可以接字串，这些字串可以取代 n1,n2 之间的行！  
* d：删除，因为是删除啊，所以 d 后面通常不接任何咚咚；  
* i：插入， i 的后面可以接字串，而这些字串会在新的一行出现(目前的上一行)；  
* p：打印，亦即将某个选择的数据印出。通常 p 会与参数 sed -n 一起运行～  
* s：取代，通常这个 s 的动作可以搭配正规表示法，例如 1,20s/old/new/g 。  

我们准备test文件,内容如下  
```commandline
HELLO LINUX!  
Linux is a free unix-type opterating system.  
This is a linux testfile!  
Linux test
```
增加内容使用命令`sed -i "3a\newline" testfile`则是在测试文件第3行后新增newline，最终文件
如下所示
```commandline
HELLO LINUX!  
Linux is a free unix-type opterating system.  
This is a linux testfile!  
newline
Linux test
```
插入内容使用命令`sed -i "3i\newline" testfile`则是在测试文件第三行新增newline，最终文件所示
如下
```commandline
HELLO LINUX!  
Linux is a free unix-type opterating system.
newline  
This is a linux testfile!  
Linux test
```
删除动作则是`sed -i "/Linux/d" testfile`则是在测试文删除匹配倒的所有行；最终文件如下图所示
```commandline
HELLO LINUX!  
This is a linux testfile!  
```

19、 简单说说awk指令？  
awk指令主要就是将文件逐行的读入，根据空格或者制表符，将每一行分成若干字段，依次用$1,$2,$3代表第一，第二，第三个字段等等；  
`-F` fs or --field-separator fs 指定输入文件折分隔符，fs是一个字符串或者是一个正则表达式，如-F:。  
`-v `var=value or --asign var=value 赋值一个用户定义变量。  
`-f` scripfile or --file scriptfile 从脚本文件中读取awk命令。    
如果有test文件内容如下图所示
```commandline
2 this is a test
3 Are you like awk
This's a test
10 There are orange,apple,mongo
```
打印文件的某一列
```bash
awk '{print $1，$4}' filename
```
则打印的文件内容为：
```commandline
2 a
3 like
This's 
10 orange,apple,mongo
```
指定使用的指标符
```bash
awk  -F, '{print $2}' test
```
则打印的文件内容为,仅有最后一行的第二列内容被打印出来:
```commandline
apple
```

20、linux系统如何安装某个服务？
主要看是什么发行版本，debian用的`apt`，centOS用的的`yum install`或者`dnf install`；安装完成后在etc目录下配置某个服务的，然后正常使用
`systemctl start nginx`来启动服务

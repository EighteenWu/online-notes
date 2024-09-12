# mysql基础
1、什么是数据库?  

A：根据**数据结构**来**组织**、**存储**、**管理数据**的仓库;  

2、什么是关系型数据库,主键、外键、索引分别是什么?  
A:关系数据库是由多张可以互相联结的二位行列表格组成的数据库;  
**主键（primary key）:** 一般是用于表示表内的数据的唯一标识;可以有**一个**或者**多个**;  
**外键**:一般用来表示两个关系之间的相关联系，有外键的的表称为主表的从表,外键又称为关键字;  
**索引**: 索引是一种单独的、物理的对数据库一列或者多列值进行排序的一种存储结构;可以理解为表内数据的集合和相应的表中数据也的逻辑指针清单;  

3、表的链接查询方式有哪些？有什么区别？  
A:**交叉链接、内连接、自链接、外链接** todo  

4、事务的特性?  
A:**原子性**: 事务中的全部操作在数据库中是不可以被分割的，要么全部完成，要么全部不执行;  
**一致性**: 几个并行执行的事务，其执行结果必须按某一顺序串行执行的结果一致;  
**隔离性**: 事务的执行不受其他的事务的干扰，事务执行的中间结果对其他事务必须是透明的;  
**持久性**: 对于任何已提交事务,系统必须保证事务对该数据库的改变不被丢失,即使数据库出现故障;

5、MySql数据库中怎么实现分页?
```mysql
select * from tablename limit 20 offset 10;
#limit后面+限制的条数，offset则是偏移量;
```
6、MySql基本操作?
```mysql
# 创建一个新的数据库
CREATE DATABASE database_name;

# 使用一个特定的数据库
USE database_name;

# 显示当前数据库中的所有表;
show TABLES;

# 创建一个新的表;
CREATE TABLE table_name
(
    name char(20);
age int(3);
gender char(2);
adress char(128);
);

# 插入数据到数据库中
INSERT INTO table_name(cloumn1, cloumn2, cloumn3) VALUES (value1,value2,value3);

# 查询数据;
SELECT column1, column2, column3 FROM table_name where condition;

# 更新语句
UPDATE table_name
set columns1 = value1, coloumn2 = value2,...
WHERE condition;

# 删除数据
DELETE FROM table_name
where condition;

# 删除一个表
DROP TABLE  table_name;

# 删除一个数据库
DROP DATABASE database_name;

# 修改表,修改字段;
ALTER table table_name change old_name new_name char not null;

```
7、 Mysql数据类型?
* 整数数类型有 TINYINT:占用一个字节 INT（4字节） BIGINT(大的整数,占用8个字节)SMALLINT，占用两个字节 MEDIUMINT,3个字节
* 浮点数或定点数:FLOAT（单精度浮点数）,DOUBLE（双进度浮点数）,DECIMAL（存储货币使用,定点数)；  
* 日期和事件类型:DATA(仅有日期),TIME（仅有时间),DATATIME(包含日期和时间)，TIMESTAMP（自动设置当前日期，用来存储更新时间或者创建时间），YEAR（仅有年份）  
* 字符串类型:CHAR(255,定长字符串),VARCHAR(65535,变成字符串),TEXT(文本),LONGTEXT（长文本）,ENUM(枚举类型),SET(一个字符串对象);
* 二进制类型:BINARY(存储二进制字符串),BLOB（存储二进制大对象）;
* 其他类型:JSON;

8、常见数据库问题?
```mysql
# Student-Sourse-SC-Teacher 表关系如下
# Student（sid，Sname，Sage，Ssex）学生表
# Course（cid，Cname，tid）课程表
# SC（sid，cid，score）成绩表
# Teacher（tid，Tname）教师表
# 查询课程 001 课程比 002课程成绩高的所有学生的学号？
# 问题1、使用外链接查询+where子句
SELECT sc1.sid from SC AS sc1 WHERE sc1.cid = '001' and sc1.score > 
(select score from SC AS sc2  where sc2.cid = '002');
# 2、使用自链接查询
SELECT sid from
SC sc1
join SC 
sc2 ON sc1.sid = sc2.sid
where sc1.cid = '001' and sc2.cid = '002'
AND sc1.score > sc2.score;

# 问题2、修改学号为 20131201 的语文成绩为 100‘
UPDATE SC SET score = 100 where sid = '20131201' and cid = (
    select cid FROM Course where Cname = "语文"
    );

# 问题3、 插入一条名为“李四”的教师记录
INSERT INTO Teacher(Tname) VALUES("李四");

# 问题4 删除学习叶平老师课程的sc表记录;
DELETE FROM SC 
WHERE cid = (
    SELECT cid From Teacher t1 join Course c1 ON t1.tid = c1.tid where t1.Tname = "李平"
    )
```

9、上面的题我看到你用Join,LEFT Join, Right Join，请问他们都是什么意思，有什么区别?  
A：Join 内链接,Join通常指的是Inner Join,只返回链接的两个表中匹配的条件记录。如果左表中的行与右表的行在链接条件上匹配，则返回，如果没有匹配上，则不返回;  
Left Join 左连接,通常指的是返回左表中的所有记录，右表如果没有匹配上则显示为NULL;  
Right Join 右链接，通常指的是返回右表中的所有记录和左表中匹配的记录，如果左表没有匹配就返回NULL值;
```mysql
# 图示说明
INNER JOIN (JOIN):
A:       B:
|---|    |---|
| 1 |    | 1 |
| 2 |    | 3 |
| 3 |    |   |
|---|    |---|
Result:
|---|
| 1 |
| 3 |
|---|

LEFT JOIN:
A:       B:
|---|    |---|
| 1 |    | 1 |
| 2 |    | 3 |
| 3 |    |   |
|---|    |---|
Result:
|---|---|
| 1 | 1 |
| 2 |NULL|
| 3 | 3 |
|---|---|

RIGHT JOIN:
A:       B:
|---|    |---|
| 1 |    | 1 |
| 2 |    | 3 |
| 3 |    |   |
|---|    |---|
Result:
|---|---|
| 1 | 1 |
|NULL| 3 |
| 3 | 3 |
|---|---|

```
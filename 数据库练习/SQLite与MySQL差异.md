# SQLite 与 MySQL 关键差异（Day22 交付物，先记在这里）

> [!info] 为什么练 SQLite、学 MySQL
> 你现在练手用 **SQLite**（Python 自带、零安装、第 4 周项目直接用），
> 但骆昊文档教的是 **MySQL**（面试考的也是 MySQL）。
> 两者 SQL 语法约 90% 相同，下面这些不同点记下来就不会混。

## 1. 自增主键（最常写错）

| | 写法 |
|---|---|
| SQLite | `id INTEGER PRIMARY KEY AUTOINCREMENT` |
| MySQL | `id INT NOT NULL AUTO_INCREMENT PRIMARY KEY` |

- SQLite 里 `AUTOINCREMENT` **必须**跟在 `INTEGER PRIMARY KEY` 后面，写成 `INT` 会失效
- MySQL 里 `AUTO_INCREMENT` 必须是键（PRIMARY KEY 或 UNIQUE）

## 2. 数据类型

| SQLite | MySQL |
|---|---|
| 动态类型，只有 5 种存储类：NULL / INTEGER / REAL / TEXT / BLOB | 静态类型：INT / VARCHAR(n) / DATETIME / DECIMAL 等 |
| 声明成 `VARCHAR(20)` 也能存超长字符串，**不会截断也不报错** | 超长会报错或截断（严格模式） |

> SQLite 声明的类型只是"建议"，这就是为什么你写错类型也不会立刻炸——
> 别被这个宽容骗了，到 MySQL 上会出问题。

## 3. 外键默认不生效 ⚠️

```sql
PRAGMA foreign_keys = ON;   -- SQLite 每次连接都要显式打开，默认 OFF
```

MySQL 的 InnoDB 默认就支持外键约束。**这是你 Day23 建 chunks 表关联 documents 时会踩的坑**——
不开这行，外键写了等于没写。

## 4. 日期处理

| SQLite | MySQL |
|---|---|
| 用字符串或 `DATE('now')`，没有真正的日期类型 | 有 `DATETIME` / `TIMESTAMP`，`NOW()` |
| `strftime('%Y-%m-%d', 'now')` | `DATE_FORMAT(NOW(), '%Y-%m-%d')` |

## 5. 布尔值

- SQLite：没有布尔类型，用 `0` / `1` 存
- MySQL：`TINYINT(1)` 当布尔用（本质还是数字）

## 6. 命令行

- SQLite：你机器上**没有 sqlite3 命令**，用 Python 的 `sqlite3` 模块或 PyCharm 的 Database 面板
- MySQL：`mysql -u root -p` 进入

## 什么时候真正用 MySQL

| 时间 | 做什么 |
|---|---|
| 现在 ~ 第 5 周 | SQLite 练手，只学概念和 SQL 语法 |
| 第 6 周 Day42 | docker-compose 起一个 MySQL 容器，第一次接触真 MySQL |
| 寒假 | 骆昊 44.Python接入MySQL，把项目从 SQLite 迁到 MySQL |

> [!tip]
> 面试问"你用的什么数据库"——答 **MySQL**（学的、考的都是它），
> 项目里用 SQLite 只是因为轻量，这个选择本身也能讲：
> "早期用 SQLite 降低部署成本，后续可平滑迁移 MySQL"。

"""
SQL 练习执行器 —— 每天「数据库 0.5h」就靠它练手

为什么需要它：
    Windows 默认没有 sqlite3 命令行，而你现在也不用装 MySQL。
    SQLite 是 Python 自带的（无需安装），建表/增删改查/索引/事务的 SQL 语法
    和 MySQL 90% 一样，够你练到第 6 周。

怎么用：
    1. 把当天要练的 SQL 写进下面的 SQLS 列表
    2. 运行本文件（PyCharm 右键 Run，或命令行 python run_sql.py）
    3. SELECT 的结果会直接打印出来；写错会报具体错误，改了再跑

数据存在同目录的 practice.db，关掉程序数据也还在（这就是"持久化"）。
想清空重来：把 practice.db 删掉即可。
"""

import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).with_name("practice.db")

# ===== 把当天的 SQL 写在这里，按顺序执行 =====
SQLS = [
    # --- Day1 补账：建表 + 主键自增 ---
    """
    CREATE TABLE IF NOT EXISTS student (
        id   INTEGER PRIMARY KEY AUTOINCREMENT,   -- 主键自增
        name TEXT    NOT NULL,
        age  INTEGER
    )
    """,

    "INSERT INTO student (name, age) VALUES ('张三', 20)",
    "INSERT INTO student (name, age) VALUES ('李四', 22)",

    "SELECT * FROM student",

    # 观察：id 是不是自动从 1 开始往上加？
    # 再插入一条一模一样的 '张三'，想想为什么不会报错？（主键只约束 id，不约束 name）

    # --- Day2：索引 ---
    # 先插入多一些数据，才看得出索引的作用
    # "CREATE INDEX idx_student_name ON student (name)",
    # "EXPLAIN QUERY PLAN SELECT * FROM student WHERE name = '张三'",
]

# ================================================


def main() -> None:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # 让结果可以按列名取值
    cur = conn.cursor()

    for sql in SQLS:
        sql = sql.strip()
        if not sql:
            continue
        print(f"\n>>> {sql.splitlines()[0][:70]}")
        try:
            cur.execute(sql)
            rows = cur.fetchall()
            if rows:
                for row in rows:
                    print("   ", dict(row))
            else:
                print("    执行成功（无返回行）")
        except sqlite3.Error as e:
            print(f"    ❌ 报错：{e}")

    conn.commit()
    conn.close()
    print(f"\n完成。数据文件：{DB_PATH}")


if __name__ == "__main__":
    main()

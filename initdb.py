import csv
import ipaddress
import sqlite3

# 打开CSV文件
with open('country_asn.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    rows = [row for row in reader]

# 创建SQLite数据库
conn = sqlite3.connect('country_asn.db')
cursor = conn.cursor()

# 删除旧表（如果存在）
cursor.execute("DROP TABLE IF EXISTS ip_info")

# 创建数据表
create_table_sql = """
    CREATE TABLE ip_info (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        start_ip TEXT,
        end_ip TEXT,
        country TEXT,
        country_name TEXT,
        continent TEXT,
        continent_name TEXT,
        asn TEXT,
        as_name TEXT,
        as_domain TEXT
    )
"""
cursor.execute(create_table_sql)

# 插入数据
insert_sql = """
    INSERT INTO ip_info (
        start_ip,
        end_ip,
        country,
        country_name,
        continent,
        continent_name,
        asn,
        as_name,
        as_domain
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
"""

for row in rows:
    start_ip = ipaddress.ip_address(row['start_ip'])
    end_ip = ipaddress.ip_address(row['end_ip'])
    if start_ip.version == 4:
        start_ip_hex = format(int(start_ip), '08x')  # Pad to 8 characters for IPv4
        end_ip_hex = format(int(end_ip), '08x')      # Pad to 8 characters for IPv4
    else:
        start_ip_hex = format(int(start_ip), '032x')  # Pad to 32 characters for IPv6
        end_ip_hex = format(int(end_ip), '032x')      # Pad to 32 characters for IPv6
    cursor.execute(insert_sql, (
        start_ip_hex,
        end_ip_hex,
        row['country'],
        row['country_name'],
        row['continent'],
        row['continent_name'],
        row['asn'],
        row['as_name'],
        row['as_domain']
    ))

# 提交更改
conn.commit()

# 关闭数据库连接
conn.close()

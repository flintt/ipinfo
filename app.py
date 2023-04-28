import json
import ipaddress
import sqlite3
from flask import Flask, request

app = Flask(__name__)

# 连接SQLite数据库
conn = sqlite3.connect('country_asn.db', check_same_thread=False)
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

def find_ip_info(ip_address_str):
    conn = sqlite3.connect('country_asn.db')
    cursor = conn.cursor()

    # Convert the IP address to a hexadecimal string
    ip_address = ipaddress.ip_address(ip_address_str)
    if ip_address.version == 4:
        ip_hex_str = format(int(ip_address), '08x')  # Pad to 8 characters for IPv4
        query = """
            SELECT * FROM ip_info
            WHERE LENGTH(start_ip) = 8 AND LENGTH(end_ip) = 8
            AND start_ip <= ? AND end_ip >= ?
        """
    else:
        ip_hex_str = format(int(ip_address), '032x')  # Pad to 32 characters for IPv6
        query = """
            SELECT * FROM ip_info
            WHERE LENGTH(start_ip) = 32 AND LENGTH(end_ip) = 32
            AND start_ip <= ? AND end_ip >= ?
        """

    # Execute the SQL query and fetch the matching records
    cursor.execute(query, (ip_hex_str, ip_hex_str))
    rows = cursor.fetchall()

    # If a matching record is found, return it as a dictionary
    if rows:
        row = rows[0]
        result = {
            'ip_address': ip_address_str,
            # 'ip_hex': ip_hex_str,
            # 'start': row[1],
            # 'end': row[2],
            'country': row[3],
            'country_name': row[4],
            'continent': row[5],
            'continent_name': row[6],
            'asn': row[7],
            'as_name': row[8],
            'as_domain': row[9]
        }
        return result

    # If no matching record is found, return an empty dictionary
    return {}




@app.route('/ip_info/<ip_address>')
def ip_info(ip_address):
    result = find_ip_info(ip_address)
    return json.dumps(result)

@app.route('/ip_country/<ip_address>')
def ip_country(ip_address):
    result = find_ip_info(ip_address)
    if result:
        result = {
            'ip_address': ip_address,
            'country': result['country']
        }
    return json.dumps(result)

@app.route('/ip_country_name/<ip_address>')
def ip_country_name(ip_address):
    result = find_ip_info(ip_address)
    if result:
        result = {
            'ip_address': ip_address,
            'country_name': result['country_name']
        }
    return json.dumps(result)

@app.route('/ip_continent/<ip_address>')
def ip_continent(ip_address):
    result = find_ip_info(ip_address)
    if result:
        result = {
            'ip_address': ip_address,
            'continent': result['continent']
        }
    return json.dumps(result)

@app.route('/ip_continent_name/<ip_address>')
def ip_continent_name(ip_address):
    result = find_ip_info(ip_address)
    if result:
        result = {
            'ip_address': ip_address,
            'continent_name': result['continent_name']
        }
    return json.dumps(result)

@app.route('/ip_asn_info/<ip_address>')
def ip_asn_info(ip_address):
    result = find_ip_info(ip_address)
    if result:
        result = {
            'ip_address': ip_address,
            'asn': result['asn'],
            'as_name': result['as_name'],
            'as_domain': result['as_domain']
        }
    return json.dumps(result)

@app.route('/ip_full_info/<ip_address>')
def ip_full_info(ip_address):
    result = find_ip_info(ip_address)
    return json.dumps(result)

if __name__ == '__main__':
    app.run(debug=True)

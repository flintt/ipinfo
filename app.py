import csv
import json
import ipaddress
from flask import Flask

app = Flask(__name__)

# 读取CSV文件到内存
data = []
with open('country_asn.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        row['start_ip'] = ipaddress.ip_address(row['start_ip'])
        row['end_ip'] = ipaddress.ip_address(row['end_ip'])
        data.append(row)

# 查询IP地址所属国家或地区代码
@app.route('/ip_country/<ip_address_str>')
def ip_country(ip_address_str):
    ip_address = ipaddress.ip_address(ip_address_str)
    result = {}
    for row in data:
        if row['start_ip'].version == ip_address.version and row['start_ip'] <= ip_address <= row['end_ip']:
            result['ip_address'] = str(ip_address)
            result['country'] = row['country']
            break
    return json.dumps(result)

# 查询IP地址所属国家或地区名称
@app.route('/ip_country_name/<ip_address_str>')
def ip_country_name(ip_address_str):
    ip_address = ipaddress.ip_address(ip_address_str)
    result = {}
    for row in data:
        if row['start_ip'].version == ip_address.version and row['start_ip'] <= ip_address <= row['end_ip']:
            result['ip_address'] = str(ip_address)
            result['country_name'] = row['country_name']
            break
    return json.dumps(result)

# 查询IP地址所属洲代码
@app.route('/ip_continent/<ip_address_str>')
def ip_continent(ip_address_str):
    ip_address = ipaddress.ip_address(ip_address_str)
    result = {}
    for row in data:
        if row['start_ip'].version == ip_address.version and row['start_ip'] <= ip_address <= row['end_ip']:
            result['ip_address'] = str(ip_address)
            result['continent'] = row['continent']
            break
    return json.dumps(result)

# 查询IP地址所属洲名称
@app.route('/ip_continent_name/<ip_address_str>')
def ip_continent_name(ip_address_str):
    ip_address = ipaddress.ip_address(ip_address_str)
    result = {}
    for row in data:
        if row['start_ip'].version == ip_address.version and row['start_ip'] <= ip_address <= row['end_ip']:
            result['ip_address'] = str(ip_address)
            result['continent_name'] = row['continent_name']
            break
    return json.dumps(result)

# 查询IP地址所属自治系统（AS）信息
@app.route('/ip_asn_info/<ip_address_str>')
def ip_asn_info(ip_address_str):
    ip_address = ipaddress.ip_address(ip_address_str)
    result = {}
    for row in data:
        if row['start_ip'].version == ip_address.version and row['start_ip'] <= ip_address <= row['end_ip']:
            result['ip_address'] = str(ip_address)
            result['asn'] = row['asn']
            result['as_name'] = row['as_name']
            result['as_domain'] = row['as_domain']
            break
    return json.dumps(result)

# 查询IP地址完整信息
@app.route('/ip_full_info/<ip_address_str>')
def ip_full_info(ip_address_str):
    ip_address = ipaddress.ip_address(ip_address_str)
    result = {}
    for row in data:
        if row['start_ip'].version == ip_address.version and row['start_ip'] <= ip_address <= row['end_ip']:
            result['ip_address'] = str(ip_address)
            result['country'] = row['country']
            result['country_name'] = row['country_name']
            result['continent'] = row['continent']
            result['continent_name'] = row['continent_name']
            result['asn'] = row['asn']
            result['as_name'] = row['as_name']
            result['as_domain'] = row['as_domain']
            break
    return json.dumps(result)

if __name__ == '__main__':
    app.run(debug=True)

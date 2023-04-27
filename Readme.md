

## 使用说明

### 启动服务

解压 `country_asn.7z` 得到 `country_asn.csv`

`python app.py`

### 查询

`curl http://127.0.0.1:5000/ip_full_info/8.8.8.8`

`curl http://127.0.0.1:5000/ip_country/8.8.8.8`

### 路由节点

| 查询内容                         | 路由              |                           返回示例                           |
| -------------------------------- | ----------------- | :----------------------------------------------------------: |
| 查询IP地址所属国家或地区代码     | ip_country        | {"ip_address": "8.8.8.8", "country": "US"}<br />{"ip_address": "240e:1::1", "country": "CN"} |
| 查询IP地址所属国家或地区名称     | ip_country_name   | {"ip_address": "8.8.8.8", "country_name": "United States"}<br />{"ip_address": "240e:1::1", "country_name": "China"} |
| 查询IP地址所属洲代码             | ip_continent      | {"ip_address": "8.8.8.8", "continent": "NA"}<br />{"ip_address": "240e:1::1", "continent": "AS"} |
| 查询IP地址所属洲名称             | ip_continent_name | {"ip_address": "8.8.8.8", "continent_name": "North America"}<br />{"ip_address": "240e:1::1", "continent_name": "Asia"} |
| 查询IP地址所属自治系统（AS）信息 | ip_asn_info       | {"ip_address": "8.8.8.8", "asn": "AS15169", "as_name": "Google LLC", "as_domain": "google.com"}<br />{"ip_address": "240e:1::1", "asn": "AS137691", "as_name": "Heilongjiang Province, P.R.China.", "as_domain": "chinatelecom.cn"} |
| 查询IP地址完整信息               | ip_full_info      | {"ip_address": "8.8.8.8", "country": "US", "country_name": "United States", "continent": "NA", "continent_name": "North America", "asn": "AS15169", "as_name": "Google LLC", "as_domain": "google.com"}<br />{"ip_address": "240e:1::1", "country": "CN", "country_name": "China", "continent": "AS", "continent_name": "Asia", "asn": "AS137691", "as_name": "Heilongjiang Province, P.R.China.", "as_domain": "chinatelecom.cn"} |

## 致谢

<p>IP address data powered by <a href="https://ipinfo.io">IPinfo</a></p>

https://chat.openai.com/


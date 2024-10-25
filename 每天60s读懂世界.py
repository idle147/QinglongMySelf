import requests
import json

url = 'https://60s.viki.moe/?encoding=text'
resp = requests.get(url)
content = resp.text
# 分片处理
pieces = resp.text.split('\n', 8)
content1 = '\n'.join(pieces[:8])  
content2 = '\n'.join(pieces[8:])

info1 = f"""
{content1}   
"""
info2 = f"""
{content2}   
"""

# # 发送分片推送  
# notify.send("每天60s读懂世界", info1 + "\n\n")
# notify.send("每天60s读懂世界", info2)

# 全文整段发送推送  
QLAPI.send("每天60s读懂世界", content)
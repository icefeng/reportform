#!/user/bin/env python
#coding:utf-8

import json,urllib2

url = "http://zabbix.conac.cn/zabbix/api_jsonrpc.php"
header = {"Content-Type":"application/json"}
data = json.dumps(
{
	"jsonrpc":"2.0",
	"method":"user.login",
	"params":{
		"user":"guest",
#		"password":""
		},
	"id":0
})
request = urllib2.Request(url,data)
for key in header:
	request.add_header(key,header[key])
try:
	result = urllib2.urlopen(request)
except URLError as e:
	print 'check name or pwd',e.code
else:
	response = json.loads(result.read())
	result.close()
	#print "auth ID is : ",response['result']
	authID = response['result']
	print  authID


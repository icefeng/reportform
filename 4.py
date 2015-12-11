import json,urllib2

url = "http://zabbix.conac.cn/zabbix/api_jsonrpc.php"
header = {"Content-Type":"application/json"}
data = json.dumps(
{
        "jsonrpc":"2.0",
        "method":"history.get",
        "params":{
                "output":"extend",
				"history":3,
				"itemids":"30761",
#				"limit":10
				"time_from":1449676800
				"time_till":1449763200
               },
        "auth":'1690f4857c4fcb0a880b64be07772f2d',
        "id":1
})
request = urllib2.Request(url,data)
for key in header:
        request.add_header(key,header[key])
try:
	result = urllib2.urlopen(request)
except URLError as e:
	if hasattr(e,'reason'):
                print 'fail to server'
                print 'reason:', e.reason
        elif hasattr(e,'code'):
                print 'not filfill request'
                print 'reason:', e.code
else:
        response = json.loads(result.read())
        result.close()
#       print result,response
        print "NUM of hosts:",len(response['result'])
        for host in response['result']:
		print host
               # print "host id:",host['hostid'],"host name:",host['name']

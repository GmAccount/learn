>>> 
>>> import json
>>> 
>>> 
>>> var1 = json.dumps([1,2,{"a":1,"b":2}])
>>> 
>>> var1
'[1, 2, {"a": 1, "b": 2}]'
>>> type(var1)
<class 'str'>
>>> 
>>> 
>>> var1 = json.dumps([1,2,True,{"a":1,"b":2}])
>>> type(var1)
<class 'str'>
>>> var1
'[1, 2, true, {"a": 1, "b": 2}]'
>>> 
>>> 
>>> var2=json.loads(var1)
>>> 
>>> type(var2)
<class 'list'>
>>> 
>>> 
>>> 
>>> 
>>> var2
[1, 2, True, {'a': 1, 'b': 2}]
>>> 
>>> 
>>> var1
'[1, 2, true, {"a": 1, "b": 2}]'
>>> 

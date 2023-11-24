### 1. What is printed by the Python code?
```python
x=5
y=x+3
x=x-1
z=10
x=x+z
print("x:{}, y:{}, z:{}".format(x, y, z))
```
```bash
Ans: x:14, y:8, z:10
```
### 2. What is printed by the Python code?
```python
x=10
for v in [4, 7, 9]:
    x=x+v
print(x)
```
```bash
Ans: 30
```
### 3. What is printed by the Python code?
```python
d=dict()
d["hello"] = "Python"
d["world"] = "2.7"
print("The {hello} {world} is {world} {hello}".format(**d))
```
```bash
Ans: The Python 2.7 is 2.7 Python
```
### 4. Complete the function fetch_the_word_arund_bucket
```python
raw = """
<A1>
[A2]
<A3>
[A4]
<A5>
*A6*
&A7&
"""
def fetch_the_word_arund_bucket(data):
    # **IMPLEMENT**
    data = data.replace('\n', '')
    ret_list, tmp_list = [], []
    for idx in range(len(data)):
        if data[idx] == '[':
            tmp_list.append(idx)
            
        if data[idx] == ']':
            if not len(tmp_list) > 0:
                raise Exception('There are unmatched brackets.')
                
            ret_list.append(data[tmp_list[-1]+1:idx])
            tmp_list.pop(-1)
    return ret_list
    
output = fetch_the_word_arund_bucket(raw)
for item in output:
    print(item)
    
# expect output:
# A2
# A4
```
### 5. What is printed by the Python code?
```python
def set_key_value(x, y, base={}):
    base[x] = y
    return base
    
out = {}
for v in range(0, 10):
    out = set_key_value(v, v)
    
ret = 0
for k, v in out.iteritems():
    ret = ret + v
    
print(ret)
```
```bash
Ans: 45
```
### 6. Complete the class ReadOnlyDict
```python
class ActionInvaild(Exception):
    pass
    
class ReadOnlyDict(dict):
    # **IMPLEMENT**
    def __setitem__(self, key, value):
        raise ActionInvaild()
        
    def set(self, key, value):
        super(ReadOnlyDict, self).__setitem__(key, value)
        
data = ReadOnlyDict()
data.set("Hello", "World!")
try:
    data["foo"] = "bar"
except ActionInvaild:
    print("Hello")
    
print(data["Hello"])
# except output:
# Hello
# World!
```
### 7. What is printed by the Python code?
```python
def gen(num):
    DATA_LEN = 3
    DATA = range(0, DATA_LEN) # range(0, 3)
    for n in range(0, num): # range(0, 10)
        idx = n % DATA_LEN
        yield DATA[idx]
        
for v in gen(10):
    print(v)
```
```bash
Ans:
0
1
2
0
1
2
0
1
2
0
```
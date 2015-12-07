##SAX解析xml
xml文件太大时,不能一次读到内存里,所以以前解析xml的方法,
```
import xml.etree.ElementTree as ET
def get_root(fname):
    tree = ET.parse(fname)
    return tree.getroot()
```
然后用root.find findall之类的方法不能用了.

解决办法是用SAX,simple API for XML.具体是用ET.iterparse,每次只处理一个节点.
```
def count_tags(filename):        
    tree = ET.parse(filename)
    data = {}
    for each in tree.iter():
        data[each.tag] = data.get(each.tag, 0) + 1
```
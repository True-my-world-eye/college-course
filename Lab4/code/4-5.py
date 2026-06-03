class DictInfo:
    def __init__(self):
        self.dict = {}
    def add_item(self, key, value):
        self.dict[key] = value

    def get_value(self, key):
        return self.dict.get(key, None)
    def merge_dict(self,dict2):
        self.dict.update(dict2.dict)
    def del_last_item(self):
        if not self.dict:
            return None
        key = list(self.dict.keys())[-1]
        val = self.dict.pop(key)
        return (key, val)
    
if __name__ == "__main__":
    dict1 = DictInfo()
    dict1.add_item("a", 1)
    dict1.add_item("b", 2)
    print(dict1.get_value("a"))  
    print(dict1.get_value("c"))  

    dict2 = DictInfo()
    dict2.add_item("c", 3)
    dict2.add_item("d", 4)

    dict1.merge_dict(dict2)
    print(dict1.get_value("c"))  

    last_item = dict1.del_last_item()
    print(last_item)  
    print(dict1.get_value("d"))  
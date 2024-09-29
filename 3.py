dict1 = {1: "xiaomi",
      2: "oppo",
      3: {3.1: "apple", 3.2: "microsoft", 3.3: "logitech", 3.4: "valve", 3.5: "samsung"},
      4: "sony"}
print(dict1)

type_dict = {}  

for key in dict1:
    val = dict1[key]
    if type(val) == dict:
        for sub_key in val:
            sub_val = type(val[sub_key])
            type_dict[sub_key] = type[sub_val]
    else:
        type_dict[key] = type(val)
    
print(type_dict)

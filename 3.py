dict1 = {1: "xiaomi",
      2: "oppo",
      3: {3.1: "apple", 3.2: "microsoft", 3.3: "logitech", 3.4: "valve", 3.5: "samsung"},
      4: "sony"}
print(dict1)

dict2 = {1: type(dict1[1]),
         2: type(dict1[2]),
         3: type(dict1[3]),
         4: type(dict1[4])}
print(dict2)
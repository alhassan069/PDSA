# try:
#     print(hello)
# except IndexError:
#     print("index error")
# except (NameError, KeyError):
#     print("Either NameError or KeyError")
# except: 
#     print("All other exceptions")
# else:
#     print("if try runs without any errors")

scores = {
    "Shefali": [3,22],
    "Harmanpreet": [200,3],
}

try:
    scores["b"].append(s)
except KeyError:
    scores["b"] = [s]
except IndexError:
    print("indexError")
except NameError:
    print("NameError")
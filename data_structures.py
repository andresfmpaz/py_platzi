print("here you will find data structure information inside of a dict")
data_structures = {"list": {"mutable" : True,
                            "Ordered" :True,
                            "Indexed" : True,
                            "Duplicate Items": True
                            },
                    "tuple": {"mutable": False,
                            "Ordered" :True,
                            "Indexed" : True,
                            "Duplicate Items": True
                            },
                    "set": {"mutable" : True,
                            "Ordered" : False,
                            "Indexed" : False,
                            "Duplicate Items": False
                            }
                    }
print(data_structures)
print('list: ',data_structures['list'])
print('tuple: ',data_structures['tuple'])
print('set: ',data_structures['set'])
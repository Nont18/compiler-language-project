def singleton(cls):
    instances = {}
    def getinstance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return getinstance

@singleton
class Memory:

    def __init__(self) -> None:
        self.memory:dict = dict({})
    
    def get(self, variable_name:str) -> object:
        assert variable_name in self.memory, f"{variable_name=} not exist in Memory"
        return self.memory[variable_name]["value"]
    
    def set(self, variable_name: str, value: object, data_type: str):
        if variable_name in self.memory:
            self.memory[variable_name]["value"] = value
            self.memory[variable_name]["data_type"] = data_type
        else:
            self.memory[variable_name] = {"value": value, "data_type": data_type}
        return self.memory[variable_name]

    def __repr__(self) -> str:
        string = ""
        string += f"Name\tValue\tData Type\n"
        string += "-"*30+"\n"
        for var, data in self.memory.items():
            value = data["value"]
            data_type = data["data_type"]
            string += f"{var}\t{value}\t{data_type}\n"
        string += "-"*30+"\n"
        return string

if __name__ == "__main__":
    memory = Memory()
    memory.set(variable_name='a', value=10.36, data_type=float)
    memory.set(variable_name='b', value="20", data_type=str)
    print(memory)
    print(memory.get(variable_name='a'))
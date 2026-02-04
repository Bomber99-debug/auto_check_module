def load_data(file_name:str, type_read_file:str = 'r', encoding:str = 'utf=8') -> list[str]:
    with open(file_name, type_read_file, encoding = encoding) as file:
        return list(i.strip() for i in file.readlines())

def file_write(file_name:str, *args, type_write: str = 'w', encoding: str = 'utf-8') -> str:
    with open(file_name, type_write, encoding = encoding) as file:
        for i in args:
            file.write(f"{str(i)}\n")
        return 'Дані записані в файл'

def clean_data(temperatura:list[str]) -> list[float]:
    return [float(temp.strip()) for temp in temperatura if temp.strip()]
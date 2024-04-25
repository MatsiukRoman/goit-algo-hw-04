from pathlib import Path

def get_cats_info(path):
   cats_dict = list()

   try:
        file_name = Path(path)
        with open(file_name, 'r', encoding='utf-8') as file:
            for line in file:
                cats_dict.append({"id": line.split(',')[0], "name": line.split(',')[1], "age": line.split(',')[2].rstrip()})
                
        return cats_dict
   except Exception as e:
       print(f'{e} with file')
       return [{"id": "", "name": "", "age": ""}]
    
relative_path = Path("cats_file.txt")
absolute_path = relative_path.absolute()
cats_info = get_cats_info(absolute_path)
print(cats_info)
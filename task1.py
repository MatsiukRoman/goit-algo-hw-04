from pathlib import Path

def total_salary(path):
    salary = list()
    try:
        file_name = Path(path)
        with open(file_name, 'r', encoding='utf-8') as file:
            for line in file:
                salary.append(float(line.split(',')[1]))
                
        total_salary = round(sum(salary),2)
        average_salary = round(total_salary/len(salary),2)
        return [total_salary,average_salary]

    except Exception as e:
        print(f'{e} with file')
        return [0,0]

relative_path = Path("salary_file.txt")
absolute_path = relative_path.absolute()
total, average = total_salary(absolute_path)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
# lab05
## json_csv
### Переводит json в csv json_to_csv()
Преобразует JSON-файл в CSV.  
Поддерживает список словарей [{...}, {...}], заполняет отсутствующие поля пустыми строками.  
Кодировка UTF-8.   
Порядок колонок — как в первом объекте.  
json_to_csv(json_path: str, csv_path: str) -> None:

### Переводить csv в json csv_to_json()
Преобразует CSV в JSON (список словарей).  
Заголовок обязателен, значения сохраняются как строки.  
csv_to_json(csv_path: str, json_path: str) -> None:

### [Код](json_and_csv.py)
![alt text](../../images/lab05/json_and_csv_code.png)

### JSON => CSV
#### people.json -> people_from_json.csv
![people.json](../../images/lab05/people_jsom.png)
---
![people_from_json.csv](../../images/lab05/people_from_json.png)

### products.json -> products_from_json.csv
![products.json](../../images/lab05/products.png)
---
![products_from_json.csv](../../images/lab05/products_from_json.png)



### CSV => JSON
#### people.csv -> people_from_csv.json
![people.csv](../../images/lab05/people.png)
---
![people_from_csv.json](../../images/lab05/people_from_csv.png)


#### students.csv -> students_from_csv.json
![students.csv](../../images/lab05/students.png)
---
![students_from_csv.json](../../images/lab05/people_from_csv.png)


### Краевые случаи
Неверный тип файла, пустой JSON или CSV → ValueError.  
Осутствующий файл → FileNotFoundError.  


## csv_xlsx
### Переводить csv в xlsx csv_to_xlsx()
Конвертирует CSV в XLSX.
Первая строка CSV — заголовок.
Лист называется "Sheet1".
Колонки — автоширина по длине текста (не менее 8 символов).
csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:

### [Код](csv_and_xlsx.py)
![alt text](../../images/lab05/csv_and_xlsx_code.png)

### CSV => XLSX
#### cities.csv -> cities.xlsx
![cities.csv](../../images/lab05/cities.png)
---
![cities.xlsx](../../images/lab05/cities_from_csv.png)

#### people.csv -> people.xlsx
![people.csv](../../images/lab05/people.png)
---
![people.xlsx](../../images/lab05/people_xlsx.png)


### Краевые случаи
Неверный тип файла, пустой JSON или CSV → ValueError.  
Осутствующий файл → FileNotFoundError.  
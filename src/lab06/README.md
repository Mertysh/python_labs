# lab05
## cli_text.py
### [Код](cli_text.py)
![alt text](../../images/lab06/cli_text_code.png)

### --help
![alt text](../../images/lab06/cli_text.png)

### Вывод cтрок файла cat()
--input - путь к входному файлу  
-n - если нужно нумеровать строки  
![alt text](../../images/lab06/peoplecsv.png)  
---
![alt text](../../images/lab06/cat.png)  

### Вывод топ слов stats()
--input - путь к входному файлу  
--top - количество слов для вывода (по умолчанию 5)  
![alt text](../../images/lab06/peopletxt.png)  
---
![alt text](../../images/lab06/stats.png)  


## cli_convert.py
### [Код](cli_text.py)
![alt text](../../images/lab06/cli_convert_code.png)

### --help
![alt text](../../images/lab06/cli_convert.png)

### json_to_csv
--in - путь к входному файлу  
--out - путь к выходному файлу  
#### --help 
![alt text](../../images/lab06/json_to_csv.png)

#### people.json -> people.csv
![alt text](../../images/lab06/json_to_csv1.png)
---
![alt text](../../images/lab06/json_to_csv2.png)
---
![alt text](../../images/lab06/json_to_csv3.png)


### csv_to_json
--in - путь к входному файлу  
--out - путь к выходному файлу  
#### --help 
![alt text](../../images/lab06/csv_to_json.png)

#### people.json -> people.csv
![alt text](../../images/lab06/csv_to_json1.png)
---
![alt text](../../images/lab06/csv_to_json2.png)
---
![alt text](../../images/lab06/csv_to_json3.png)


### csv_to_xlsx
--in - путь к входному файлу  
--out - путь к выходному файлу  
#### --help 
![alt text](../../images/lab06/csv_to_xlsx.png)

#### people.json -> people.csv
![alt text](../../images/lab06/csv_to_xlsx1.png)
---
![alt text](../../images/lab06/csv_to_xlsx2.png)
---
![alt text](../../images/lab06/csv_to_xlsx3.png)

### Краевые случаи
Осутствующий файл → FileNotFoundError.  
top меньше или равен 0 → error: top должен быть больше 0.  
Отсутствие подкоманды →  error: argument command: invalid choice: "" (choose from 'json_to_csv', 'csv_to_json', 'csv_to_xlsx')

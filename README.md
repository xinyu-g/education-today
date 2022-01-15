# Education Today

## Database 

### Change path and setup parameters in consts.py

```python
# data directory
DATA = 'path to data'

# mysql setup
HOST = 'localhost'
USER = 'username'
PASSWORD = 'password'
DB = 'dbname'

# Schema setup 
REDUCED_SCHEMA = {'tablename': [selected cols]}
SCHEMA = {'tablename': [all data cols]}
```

### Run preprocess.py

```python
args
--reduced: whether to create database on selected columns or on all columns, default true
```

run

```python
python preprocess.py
```



## Task 1

### Run the flask app

```shell
export FLASK_APP=edtoday
export FLASK_ENV=development
flask run
```

### Run react frontend

```shell
npm start
```

### search by authorId

Input author id and click submit.

![image-20220115001556477](C:\Users\xinyu\AppData\Roaming\Typora\typora-user-images\image-20220115001556477.png)

The output for sample author id 2146473740.

![image-20220115001839763](C:\Users\xinyu\AppData\Roaming\Typora\typora-user-images\image-20220115001839763.png)
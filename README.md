# ORM(Object-Relational-Mapper)

## SQL Alchemy
## Django ORM   

# WHAT? Converting data between incompatible type system using object-oriented programming languages

Student.object.all()

Select * from Student

# SQL
- Structured Query Language
- Language Used to 
- - SQL lets you access and manipulate databases
- Standard language for dealing with Relational
- - Databases:
    - - MYSQL
    - - PostgreSQL
    - - Oracle

# WHY? 
- Developer writed Python code instead of SQL to
    - Create,
    - Update,
    - Delete data & Schemas.

# WHY ORM?
1. Write in the language you are already using anyway
2. Easy switching from MySQL to PostgreSQL
3. ORM provides additional feature out of the box.
4. Queries can perform better - if you're not too familiar with SQL

# 2nd 
- Simple OR queries
- Simple OR query
- Q object - OR query
- View query SQL in tab
- Query performance

# 3rd
- Simple AND queries
- Simple AND query
- Q object - AND query
- View query SQL in tab
- Query performance

# 4th
- Simple UNION queries
- Simple UNION query
- View query SQL 
- Query performance

# 5th
- Simple NOT queries
- Simple NOT query
- View query SQL 
- Query performance
- exclude(<condition>)
- filter(~Q(<condition>))

# 6th
- Simple Field Select and Output
- Select individual database field
- Outputting to template

# 7th 
- Performing simple RAW queries
- Understandig RAW
- RAW query example
- raw() mathod takes a raw SQL query
- Executes query

# 8th
- Performing custom SQL directly
- Understanding the prrocess
- SQL query examples
- django.db.connection
- connection.cursor()
- cursor.execut(sql)
- cursor.fetchone() or cursor.fetchall()

# 9th 
- Introduction  to Model Inheritance
- Abstract models(Abstract Base Class(ABC))
- - Used: When you have common information needed for number of other models
- - ABC - does not get created : Fields added to other child classes(models)
- Multi-table model inheritance
- - Differences:
    - - Every model is a model all by itself 
    - - One-to-One link is created automatically
- Proxy models
- - Used:
    - - Change the behavior of the model
    - - Proxy models operate on the orignal model



#   S n i p p e t - O R M  
 
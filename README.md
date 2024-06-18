### Cookie cutter template for using your own Python modules inside Databricks notebooks

Steps to follow:
- Move the `.py` files containing the functions you want to a seperate my_lib folder.
- Create en empty file called `__init__.py` in the same my_lib directory. This way Python knows it is a package directory.
- In your notebook, add the following: 
```
import sys
sys.path.append("my_lib")
```
- Then import functions the following way
```
from <my_lib>.<my_module> import <function_name> <ClassName>
```

![image](./cool_logo.png)
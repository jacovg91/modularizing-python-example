### Cookie cutter template for using your own Python modules inside Databricks notebooks

Steps to follow:
- Move the `.py` files containing the functions into a seperate directory.
- Create an empty file called `__init__.py` in the same directory. This way Python knows it is a package directory.
- In your notebook, add the following: 
```
import sys
sys.path.append("path/to/my_folder")
```
- Then import functions the following way:
```
from <my_folder>.<my_module> import <function_name>, <ClassName>
```

![image](./cool_logo.png)
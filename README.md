# data4test
you can get useful data here for software testing

## Installation
The last stable release is available on PyPI and can be installed with pip.
make sure that Chrome has been installed and match the selenium version

    $ pip install data4test
    
## Best Practice

Firstly, create a python file: c:\folder\mytest.py

    # c:\folder\mytest.py
    from data4test import timestamp4test
    print(timestamp4test.get_this_week_head_timestamp())
    print(timestamp4test.get_this_week_end_timestamp())
    print(timestamp4test.get_this_month_head_timestamp())
    print(timestamp4test.get_this_month_end_timestamp())
    print(timestamp4test.get_chinese_this_week_head_timestamp())
    print(timestamp4test.get_chinese_this_week_end_timestamp())
    
then use your IDE to run this script or 

    $ python c:\folder\mytest.py
    
if successful, you will see many timestamps :) 


## Contact me

For information and suggestions you can contact me at 523314409@qq.com
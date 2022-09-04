"""""
Regular Expression 

"""""

import re

text = """
This alert service notifies Malkova@gmail.com
and Romi@yahoo.com and Mia_1@telegram.in
"""

list_of_mails = re.findall("[a-z0-9\.\-+_]+@[a-z0-9\.\-+",text)
print(list_of_mails)
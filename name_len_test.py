# def name_len2(username,min_len):
#     assert type(username) ==str, "name must be string mate"
#     if min_len <1:
#         raise ValueError("mate how can the length be <1?")
#     if len(username)< min_len:
#         return False
#     if not username.isalnum():
#         return False
#     return True

# print(name_len2(12,0))


import unittest
from day32_26_02_26 import name_len2

class name_len_test(unittest.TestCase):
    # def test_min_len(self):
    #     arg1='aa'
    #     arg2=12
    #     result=''
    #     self.assertEqual(name_len2(arg1,arg2),result)
    def test_short(self):
        self.assertRaises(ValueError, name_len2, '',0)
        # behind the scenes assertRaises calls function using try catch block
        
        pass 
unittest.main()
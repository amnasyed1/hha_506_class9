# import module1
# import module1 as mod1
# from module1 import *

import sys

sys.path.append('/home/amna_syed/hha_506_class9/modules')

import module1

output1= module1.addition(5, 10)
output2 = module1.subtraction(5, 10)

print('Output: ', output1) 
print('Output: ', output2)

print (f"Output 1: {output1}")
print (f'Output 2: {output2}')
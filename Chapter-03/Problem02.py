# Write a program to fill in a letter template given below with name and date. 
#letter 
'''  
       Dear <|Name|>, 
       You are selected! 
       <|Date|> 
        '''
Letters = '''
Dear <|Name|>,
You are selected!
<|Date|> 
'''
replace_name = input("Enter your name: ")
replace_date = input("Enter the date: ")
print(Letters.replace("<|Name|>", replace_name).replace("<|Date|>", replace_date))
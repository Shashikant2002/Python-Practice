name = input('Enter Your Name\n')
age = input('Enter Your Age\n')

# print(''' Hi Welcome Mr. ''' + name + ''' Maked By Shashikant''')

latter = ''' Dear <|Name|> 
Your Are The Best
<|age|>'''

latter = latter.replace("<|Name|>", name)
latter = latter.replace("<|age|>", age)

print(latter)

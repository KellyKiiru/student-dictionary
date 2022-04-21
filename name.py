#print('hello world')

#a = 4 
#b =2
#c = a/b
#print(c)

person = {
    'jina':'loise',
    'age': 23,
    'favorite_movie':'spiderman going home'
}

#name = input('whats your name')

print('hi there...')

email_address = input(f'hi, whats your email address?\n\n')

if email_address:
    
    #multi_line = f"""
    #Hi {person['name']}, are you {person['age']}?
    #Your fav movie is {person['favorite_movie']}
    #"""
    
    #print(f"""
    #Hi {person['name']}, are you {person['age']}?
    #Your fav movie is {person['favorite_movie']}
    #""")
    
    print(f"""
          Hi {person['jina']}, are you {person['age']} ?
          We realized that you really like {person['favorite_movie']}.
          Is that true?
          """)
else:
    print('get out\n\n')
    
#string1="go"
#string2="now"
#string3="great"
#print(f"""
#I will {string1} there
#I will go {string2}
#{string3}
#""")
# -	Write a program that takes in a text and a query string and checks if the query string exists in the text. For example: 

# text = “Hello World”
# query = “wor”
# result = search(text, query)
# print(result)

# The result should be equal to True

def search(text,query):
    if query in text:
      return True 
    else:
       return False
    
text ="Hello World"
query ="Wor"
result = search(text,query)
print(result)
    

# string counter
def count(text, string, v=0 ) :
  v = v + int(text.startswith(string))
  print(v)
  if len(string) < len(text):
      count(text[1 : ], string, v)
  else:
      return v

print(count('hellohellogoodbye','hello'))

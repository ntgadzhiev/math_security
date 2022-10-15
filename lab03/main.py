
alphabet = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я','А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']

def gamma(start, key):
  key*=len(start)

  end_text=""
  for i, j in enumerate(start):
    position = alphabet.index(j)
    
    position_key=alphabet.index(key[i])+1
    new_position =(position-position_key)%33
    end_text+=alphabet[new_position]
    print(new_position,end=" ")
  print(f"\n Our Result: {end_text}")

gamma("УСЦШБЛ".upper(),"ГАММА")

#П 16   Г 4   20
#Р 17   А 1   18 
#И 9    М 14  23
#К 11   М 14  25
#А 0    А 1   1
#З 8    Г 4   12

  
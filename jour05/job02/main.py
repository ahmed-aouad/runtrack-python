def draw_rectangle(width, height):
    parrallele = "|"+(width-2)*"-"+"|"
    print(parrallele)

    for i in range(height-2):
      cotés="|"+(width-2)*" "+"|"
      print(cotés)
    print(parrallele)  

draw_rectangle(10,3)    

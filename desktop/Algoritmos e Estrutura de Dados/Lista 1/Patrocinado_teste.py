def analisePilha(list, endr_pos, ney_pos, cr7_pos, mes_pos, balance_pos,puma_pos, nike_pos, adidas_pos):
    endr, ney, cr7, mes = False, False, False, False
    for item in list:
        if item == "endrick":
            endr_pos = list.index(item)
        if item == "new balance": 
            balance_pos = list.index(item)
        if item == "neymar":
            ney_pos = list.index(item)
        if item == "puma":
            puma_pos = list.index(item)
        if item == "cr7":
            cr7_pos = list.index(item)
        if item == "nike":
            nike_pos = list.index(item)
        if item == "messi":
            mes_pos = list.index(item)
        if item == "adidas":
            adidas_pos = list.index(item)
        
    if balance_pos >= endr_pos:
        endr = True
    if puma_pos >= ney_pos:
        ney = True
    if nike_pos >= cr7_pos:
        cr7 = True
    if adidas_pos >= mes_pos:
        mes = True
    
    if endr == True and ney == True and cr7 == True and mes == True:
        return True
    return False
        
endr_pos, ney_pos, cr7_pos, mes_pos, balance_pos,puma_pos, nike_pos, adidas_pos = 0,0,0,0,0,0,0,0

question = input().split("-")

if analisePilha(question,endr_pos, ney_pos, cr7_pos, mes_pos, balance_pos,puma_pos, nike_pos, adidas_pos):
    print("Correto")
else:
    print("Incorreto")

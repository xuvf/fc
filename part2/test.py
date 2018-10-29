import part2, math




# same centre

#Circle 0 0 and 5
cir1 = part2.Circle(part2.Point(0,0), 5.0)

#same Square
sq = part2.Square(part2.Point(-2,2),4)
if cir1.envelops(sq):
    print("圆里面包含正方形（正常）")
else:
    print("圆里面包含正方形（正常）错误")

sq = part2.Square(part2.Point(-math.sqrt(5.0**2/2),math.sqrt((5.0**2)/2)), math.sqrt(50)) 
if cir1.envelops(sq):
    print("圆里面包含正方形（同中心,四点相切）")
else:
    print("圆里面包含正方形（同中心,四点相切）错误")

sq = part2.Square(part2.Point(-4,4), 8)
if not cir1.envelops(sq):
    print("圆里面包含正方形（同中心,四点出界）")
else:
    print("圆里面包含正方形（同中心,四点出界）错误")

sq = part2.Square(part2.Point(-4,4), 4)
if not cir1.envelops(sq):
    print("圆里面包含正方形（同中心,左上出界）")
else:
    print("圆里面包含正方形（同中心,左上出界）错误")

sq = part2.Square(part2.Point(0,4), 4)
if not cir1.envelops(sq):
    print("圆里面包含正方形（同中心,右上出界）")
else:
    print("圆里面包含正方形（同中心,右上出界）错误")

sq = part2.Square(part2.Point(-4,0), 4)
if not cir1.envelops(sq):
    print("圆里面包含正方形（同中心,左下出界）")
else:
    print("圆里面包含正方形（同中心,左下出界）错误")

sq = part2.Square(part2.Point(0,0), 4)
if not cir1.envelops(sq):
    print("圆里面包含正方形（同中心,右下出界）")
else:
    print("圆里面包含正方形（同中心,右下出界）错误")

sq = part2.Square(part2.Point(-1,5), 2)
if not cir1.envelops(sq):
    print("圆里面包含正方形（同中心,左上右上出界）")
else:
    print("圆里面包含正方形（同中心,左上右上出界）错误")

sq = part2.Square(part2.Point(-5,1), 2)
if not cir1.envelops(sq):
    print("圆里面包含正方形（同中心,左上左下出界）")
else:
    print("圆里面包含正方形（同中心,左上左下出界）错误")
    
sq = part2.Square(part2.Point(4,1), 2)
if not cir1.envelops(sq):
    print("圆里面包含正方形（同中心,右上右下出界）")
else:
    print("圆里面包含正方形（同中心,右上右下出界）错误")

sq = part2.Square(part2.Point(-1,-4), 2)
if not cir1.envelops(sq):
    print("圆里面包含正方形（同中心,左下右下出界）")
else:
    print("圆里面包含正方形（同中心,左下右下出界）错误")

sq = part2.Square(part2.Point(-7,7), 4)
if not cir1.envelops(sq):
    print("圆里面包含正方形（同中心,左上左下右上出界）")
else:
    print("圆里面包含正方形（同中心,左上左下右上出界）错误")
    
sq = part2.Square(part2.Point(3,7), 4)
if not cir1.envelops(sq):
    print("圆里面包含正方形（同中心,左上右上右下出界）")
else:
    print("圆里面包含正方形（同中心,左上右上右下出界）错误")

sq = part2.Square(part2.Point(3,-3), 4)
if not cir1.envelops(sq):
    print("圆里面包含正方形（同中心,左下右上右下出界）")
else:
    print("圆里面包含正方形（同中心,左下右上右下出界）错误")

sq = part2.Square(part2.Point(-7,-3), 4)
if not cir1.envelops(sq):
    print("圆里面包含正方形（同中心,左上左下右下出界）")
else:
    print("圆里面包含正方形（同中心,左下左上右下出界）错误")

cir2 = part2.Circle(part2.Point(0,0), 3.0)
if cir1.envelops(cir2):
    print("圆里面包含圆（同中心）")
else:
    print("圆里面包含圆（同中心）错误")

cir2 = part2.Circle(part2.Point(0,0), 5.0)
if cir1.envelops(cir2):
    print("圆里面包含圆（同中心,相等）")
else:
    print("圆里面包含圆（同中心,相等）错误")
    
cir2 = part2.Circle(part2.Point(0,0), 6.0)
if not cir1.envelops(cir2):
    print("圆里面包含圆（同中心,出界）")
else:
    print("圆里面包含圆（同中心,出界）错误")

cir2 = part2.Circle(part2.Point(-3,0), 2.0)
if cir1.envelops(cir2):
    print("圆里面包含圆（左相切）")
else:
    print("圆里面包含圆（左相切）错误")

cir2 = part2.Circle(part2.Point(3,0), 2.0)
if cir1.envelops(cir2):
    print("圆里面包含圆（右相切）")
else:
    print("圆里面包含圆（右相切）错误")

cir2 = part2.Circle(part2.Point(0,3), 2.0)
if cir1.envelops(cir2):
    print("圆里面包含圆（上相切）")
else:
    print("圆里面包含圆（上相切）错误")

cir2 = part2.Circle(part2.Point(0,-3), 2.0)
if cir1.envelops(cir2):
    print("圆里面包含圆（下相切）")
else:
    print("圆里面包含圆（下相切）错误")

cir2 = part2.Circle(part2.Point(-3,0), 4.0)
if not cir1.envelops(cir2):
    print("圆里面包含圆（左出界）")
else:
    print("圆里面包含圆（左出界）错误")

cir2 = part2.Circle(part2.Point(3,0), 4.0)
if not cir1.envelops(cir2):
    print("圆里面包含圆（右出界）")
else:
    print("圆里面包含圆（右出界）错误")

cir2 = part2.Circle(part2.Point(0,2), 4.0)
if not cir1.envelops(cir2):
    print("圆里面包含圆（上出界）")
else:
    print("圆里面包含圆（上出界）错误")

cir2 = part2.Circle(part2.Point(0,-3), 4.0)
if not cir1.envelops(cir2):
    print("圆里面包含圆（下出界）")
else:
    print("圆里面包含圆（下出界）错误")

cir2 = part2.Circle(part2.Point(5,0), 1.0)
if not cir1.envelops(cir2):
    print("圆里面包含圆（出界[判断边]）")
else:
    print("圆里面包含圆（下出界[判断边]）错误")

sq = part2.Square(part2.Point(0,0), 5.0)

sq2 = part2.Square(part2.Point(2,-2), 2.0)
if  sq.envelops(sq2):
    print("正方形里面包含正方形（正常）")
else:
    print("正方形里面包含正方形（正常）错误")

sq2 = part2.Square(part2.Point(0,0), 5.0)
if  sq.envelops(sq2):
    print("正方形里面包含正方形（正常,相等）")
else:
    print("正方形里面包含正方形（正常,相等）错误")

sq2 = part2.Square(part2.Point(0,0), 3.0)
if  sq.envelops(sq2):
    print("正方形里面包含正方形（左上相切）")
else:
    print("正方形里面包含正方形（左上相切）错误")

sq2 = part2.Square(part2.Point(0,-2), 3.0)
if  sq.envelops(sq2):
    print("正方形里面包含正方形（左下相切）")
else:
    print("正方形里面包含正方形（左下相切）错误")

sq2 = part2.Square(part2.Point(2,0), 3.0)
if  sq.envelops(sq2):
    print("正方形里面包含正方形（右上相切）")
else:
    print("正方形里面包含正方形（右上相切）错误")

sq2 = part2.Square(part2.Point(2,-2), 3.0)
if  sq.envelops(sq2):
    print("正方形里面包含正方形（右下相切）")
else:
    print("正方形里面包含正方形（右下相切）错误")

sq2 = part2.Square(part2.Point(4,2), 2.0)
if not sq.envelops(sq2):
    print("正方形里面包含正方形（上出界）")
else:
    print("正方形里面包含正方形（上出界）错误")
    
sq2 = part2.Square(part2.Point(2,-4), 2.0)
if not sq.envelops(sq2):
    print("正方形里面包含正方形（下出界）")
else:
    print("正方形里面包含正方形（下出界）错误")

sq2 = part2.Square(part2.Point(-1,-2), 2.0)
if not sq.envelops(sq2):
    print("正方形里面包含正方形（左出界）")
else:
    print("正方形里面包含正方形（左出界）错误")

sq2 = part2.Square(part2.Point(4,-2), 2.0)
if not sq.envelops(sq2):
    print("正方形里面包含正方形（右出界）")
else:
    print("正方形里面包含正方形（右出界）错误")

sq2 = part2.Square(part2.Point(-1.5,1.5), 2.0)
if not sq.envelops(sq2):
    print("正方形里面包含正方形（左上出界三点）")
else:
    print("正方形里面包含正方形（左上出界三点）错误")
    
sq2 = part2.Square(part2.Point(-1.5,-4.5), 2.0)
if not sq.envelops(sq2):
    print("正方形里面包含正方形（左下出界三点）")
else:
    print("正方形里面包含正方形（左下出界三点）错误")

sq2 = part2.Square(part2.Point(4.5,1.5), 2.0)
if not sq.envelops(sq2):
    print("正方形里面包含正方形（右上出界三点）")
else:
    print("正方形里面包含正方形（右上出界三点）错误")

sq2 = part2.Square(part2.Point(4.5,-4.5), 2.0)
if not sq.envelops(sq2):
    print("正方形里面包含正方形（右下出界三点）")
else:
    print("正方形里面包含正方形（右下出界三点）错误")

sq = part2.Square(part2.Point(-5,5),10.0)

cir = part2.Circle(part2.Point(0,0), 3.0)
if sq.envelops(cir):
    print("正方形里面包含圆（同心,正常）")
else:
    print("正方形里面包含圆（同心,正常）错误")

cir = part2.Circle(part2.Point(0,0), 5)
if sq.envelops(cir):
    print("正方形里面包含圆（同心,相切）")
else:
    print("正方形里面包含圆（同心,相切）错误")
    
cir = part2.Circle(part2.Point(0,0), 5.5)
if not sq.envelops(cir):
    print("正方形里面包含圆（同心,出界）")
else:
    print("正方形里面包含圆（同心,出界）错误")

cir = part2.Circle(part2.Point(-3,3), 3)
if not sq.envelops(cir):
    print("正方形里面包含圆（左上出界）")
else:
    print("正方形里面包含圆（左上出界）错误")

cir = part2.Circle(part2.Point(-3,-3), 3)
if not sq.envelops(cir):
    print("正方形里面包含圆（左下出界）")
else:
    print("正方形里面包含圆（左下出界）错误")

cir = part2.Circle(part2.Point(3,3), 3)
if not sq.envelops(cir):
    print("正方形里面包含圆（右上出界）")
else:
    print("正方形里面包含圆（右上出界）错误")

cir = part2.Circle(part2.Point(3,-3), 3)
if not sq.envelops(cir):
    print("正方形里面包含圆（右下出界）")
else:
    print("正方形里面包含圆（右下出界）错误")

cir = part2.Circle(part2.Point(0,5), 5)
if not sq.envelops(cir):
    print("正方形里面包含圆（上出界2个）")
else:
    print("正方形里面包含圆（上出界2个）错误")
    
cir = part2.Circle(part2.Point(0,-5), 5)
if not sq.envelops(cir):
    print("正方形里面包含圆（下出界2个）")
else:
    print("正方形里面包含圆（下出界2个）错误")

cir = part2.Circle(part2.Point(5,0), 5)
if not sq.envelops(cir):
    print("正方形里面包含圆（右出界2个）")
else:
    print("正方形里面包含圆（右出界2个）错误")
    
cir = part2.Circle(part2.Point(-5,0), 5)
if not sq.envelops(cir):
    print("正方形里面包含圆（左出界2个）")
else:
    print("正方形里面包含圆（左出界2个）错误")

cir = part2.Circle(part2.Point(-5,5), 10)
if not sq.envelops(cir):
    print("正方形里面包含圆（左上出界3个）")
else:
    print("正方形里面包含圆（左出界2个）错误")

cir = part2.Circle(part2.Point(-5,-5), 10)
if not sq.envelops(cir):
    print("正方形里面包含圆（左下出界3个）")
else:
    print("正方形里面包含圆（左下出界3个）错误")

cir = part2.Circle(part2.Point(5,5), 10)
if not sq.envelops(cir):
    print("正方形里面包含圆（右上出界3个）")
else:
    print("正方形里面包含圆（右上出界3个）错误")

cir = part2.Circle(part2.Point(5,-5), 10)
if not sq.envelops(cir):
    print("正方形里面包含圆（右下出界3个）")
else:
    print("正方形里面包含圆（右下出界3个）错误")





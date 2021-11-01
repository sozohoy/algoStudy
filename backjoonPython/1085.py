x,y,w,h = map(int, input().split())

cod_x = w - x
cod_y = h - y
cod_0x = x - 0
cod_0y = y - 0

print(min(cod_x, cod_y, cod_0x, cod_0y))
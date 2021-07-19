products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	price = int(price)
	# p = []
	# p.append(name)
	# p.append(price)
	# p = [name, price]
	products.append([name, price])
print(products)
# print(products[0][0])

for p in products:
	print(p[0], '的價格是', p[1])

with open('product.csv', 'w', encoding='utf-8') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')



#作業
# data = [1, 3, 5, 7, 9] # 清單中
# with open('data.txt', 'w') as f:
# 	for p in data:
# 		f.write(p)
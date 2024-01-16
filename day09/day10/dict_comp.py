#dict_comp
#normalPopcorn = {
#         'name':"일반 팝콘",
#         'price': 2500,
# }


# zipper
# zipped = zip(coffee,price)
# print(list(zipped))
# coffee = ['아메리카노', '라떼', '바닐라']
# price = [2500, 3000, 3500]
# caffeine = [120,150,50]
# result = [{'이름':name, '가격':price, '카페인':caffeine} for name,price,caffeine in zip(coffee,price,caffeine)]
# print(result)


coffee = ['아메리카노', '라떼', '바닐라']
price = [2500, 3000, 3500]

a = [i:{'이름':coffee,'가격':price} for i,(coffee,price) in enumerate(zip(coffee,price))]
Popcorn = {
         'name':"일반 팝콘",
         'price': 2500,
}
# for index,item in enumerate(coffee):

for in enumerate(coffee,price)



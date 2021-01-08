# 商品列表
list_commodity_infos = [
    {"cid": 1001, "name": "屠龙刀", "price": 10000},
    {"cid": 1002, "name": "倚天剑", "price": 10000},
    {"cid": 1003, "name": "金箍棒", "price": 52100},
    {"cid": 1004, "name": "口罩", "price": 20},
    {"cid": 1005, "name": "酒精", "price": 30},
]

# 订单列表
list_orders = [
    {"cid": 1001, "count": 1},
    {"cid": 1002, "count": 3},
    {"cid": 1005, "count": 2},
]


#
# # --1.定义函数,打印所有商品信息,
# # --格式：商品编号xx,商品名称xx,商品单价xx.
# def print_all_commodity():
#     for item in list_commodity_infos:
#         print(f"商品编号{item['cid']},商品名称{item['name']},商品单价{item['price']}")
#
#
# # print_all_commodity()
#
# # --2.定义函数,打印商品单价小于2万的商品信息
# def print_price_less_than_2w():
#     for item in list_commodity_infos:
#         if item['price'] < 20000:
#             print(item)
#
#
# print_price_less_than_2w()

# --3.定义函数,打印所有订单中的商品信息,
# --格式：商品名称xx,商品单价:xx,数量xx.
def print_all_order():
    for item in list_commodity_infos:
        for item2 in list_orders:
            if item2["cid"]==item["cid"]:
                print(f"商品名称{item['name']},商品单价:{item['price']},数量{item2['count']}")
                break #跳出内层循环
                # return #跳出整个循环
#
#
# print_all_order()
# --4.定义函数,查找最贵的商品(使用自定义算法,不使用内置函数)
# def get_max_price_commodity():
#     max_price = list_commodity_infos[0]
#     for i in range(1, len(list_commodity_infos)):
#         if max_price["price"] < list_commodity_infos[i]["price"]:
#             max_price = list_commodity_infos[i]
#     print(max_price)


# get_max_price_commodity()

# --5.定义函数,根据单价对商品列表升序排列
def ascending_order_by_price():
    for i in range(len(list_commodity_infos) - 1):
        for j in range(i + 1, len(list_commodity_infos)):
            if list_commodity_infos[i]['price'] > list_commodity_infos[j]['price']:
                list_commodity_infos[i], list_commodity_infos[j] = list_commodity_infos[j], list_commodity_infos[i]
    print(list_commodity_infos)


ascending_order_by_price()

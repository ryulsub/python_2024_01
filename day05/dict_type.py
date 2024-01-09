#dict_type
# key-value

# key: 중복 안됨, 숫자 or 문자 type 가능
# value: 중복 가능, any type
# zodiac = {
#     1:'쥐',
#     2:'소',
#     3:'호랑이',
#     4:'토끼',
#     5:'용'
# }
# print(zodiac[4])

# mbti = {
#     'e':'외향적',
#     'i':'내향적',
#     's':'감각적',
#     'n':'직관적',
#     'f':'감성적',
#     't':'이성적',
#     'j':'계획적',
#     'p':'즉흥적',
# }
# # print(mbti['e'])
# personality = input("mbti 입력:")
# print(f"당신의 성향은 {mbti[personality[0]]} {mbti[personality[1]]} {mbti[personality[2]]} {mbti[personality[3]]}")

instargram = {
    "신촌맛집":['싸다김밥','신촌순댓국','서브웨이'],
    "서강대맛집":{
        "서강대학식":['한식정식','오늘의치돈','육회덮밥']
    }
}
print(instargram["신촌맛집"][2])
print(instargram["서강대맛집"]["서강대학식"][1])
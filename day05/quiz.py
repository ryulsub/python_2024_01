#1.  일본여행 계획 프로그램
#유저에게 쉼표 기준으로 할 계획을 입력받고, 할일을 나타내는 프로그램 만들기
# 입력)일본여행 계획: 초밥 먹기, 돈키호테 가기, 온천가기
# 결과) 일본여행 계획표 [초밥 먹기, 돈키호테가기.온천가기]입니다.

# plan = input("일본 여행 계획표를 입력하세요(쉼표 기준)")
# planList = plan.split(",")
# print(f"일본 여행 계획표는 {planList} 입니다!😊")


#2.뉴스기사 단어 찾기 프로그램

# article = """
# Collaboration is essential to advancing knowledge and, ultimately, entire societies.
# With the development of Web 2.0, the possibilities have risen to unprecedented levels and allowed for the collaborative creation of
# the world’s largest compendium of knowledge that ever existed – Wikipedia.
# Collaboration is not a safeguard of quality per se, however. Rather, the quality of Wikipedia articles rises with the number of
# editors per article as well as a greater diversity among them.
# Here, we address a not yet documented potential threat to those preconditions: self-selection of Wikipedia editors to articles. Specifically,
# we expected articles with a clear-cut link to a specific country (e.g., about its highest mountain, “national” article category)
# to attract a larger proportion of editors of that nationality when compared to articles without any specific link to that country
# (e.g., “gravity”, “universal” article category), whereas articles with a link to several countries
# (e.g., “United Nations”, “international” article category) should fall in between. Across several language versions, hundreds of different articles, and hundreds of thousands of editors,
# we find the expected effect within Wikipedia: The more exclusively an article topic is linked to a particular nation, the higher the proportion of editors from that country is among the contributors.
#  """
#
# word = input("찾고 싶은 단어:")
# countWord = article.count(word)
# print(f"{word}의 개수는 {countWord}개 입니다.")

#3 스타벅스 메뉴 고르기
# coffee = [4000,5000,5500]
# cake = [5000,6000,5500]
# choice_coffee = int(input("커피 메뉴[1.아메리카노: 4000 2.라떼: 5000 3.바닐라라떼:5500")) - 1
# choice_cake = int(input("케잌 메뉴[1.치즈케잌: 5000 2.딸기케잌: 6000 3.우유케잌:5500")) - 1
# print(f"커피와 케잌의 값은 {coffee[choice_coffee]+ cake[choice_cake]} 입니다.")

#4. 커피 브랜드 capitalize화 하기
# brands = input("좋아하는 커피 브랜드 3개 입력(쉼표 기준):").split(',')
# brands[0] = brands[0].capitalize()
# brands[1] = brands[1].capitalize()
# brands[2] = brands[2].capitalize()
# print(brands)

# 퀴즈1. 대소문자변화 프로그램
# * 사용자로부터 소문자로 된 문자열을 입력받은 후, 이를 모두 대문자로 변환하는 프로그램을 만드세요.
# coffee= 'icecafelatte'
# print(coffee.upper())
#
# #2. 노래 가사에서 단어 카운트
# song = """
#
# "Memories follow me left and right
# I can feel you over here, I can feel you over here
# You take up every corner of my mind (what you gon' do now?)
# Ever since the d-day y-you went away (no, I don't know how)
# How to erase your body from out my brain (what you gon' do now?)
# Maybe I should just focus on me instead (but all I think about)
# Are the nights we were tangled up in your bed
# Oh no (oh no)
# Oh no (oh no)
# You're goin' 'round in circles
# Got you stuck up in my head, yeah
# Memories follow me left and right
# I can feel you over here, I can feel you over here
# You take up every corner of my mind
# Your love stays with me day and night
# I can feel you over here, I can feel you over here
# You take up every corner of my mind (what you gon' do now?)
# Ever since the d-day y-you went away (someone tell me how)
# How much more do I gotta drink for the pain (what you gon' do now?)
# You did things to me that I just can't forget (now all I think about)
# Are the nights we were tangled up in your bed
# Oh no (oh no)
# Oh no (oh no)
# You're going 'round in circles
# Got you stuck up in my head, yeah
# Memories follow me left and right
# I can feel you over here, I can feel you over here
# You take up every corner of my mind (of my mind)
# Your love stays with me day and night
# I can feel you over here, I can feel you over here
# You take up every corner of my mind (what you gon' do now?)
# Did you know you're the one that got away?
# And even now, baby, I'm still not okay
# Did you know that my dreams, they're all the same
# Every time I close my eyes?
# Memories follow me left and right
# I can feel you over here, I can feel you over here
# You take up every corner of my mind (what you gon' do now?)
# Your love stays with me day and night
# I can feel you over here, I can feel you over here
# You take up every corner of my mind (what you gon' do now?)
# (Whoa)
# I can feel you over here, I can feel you over here
# You take up every corner of my mind (what you gon' do now?)"
# """

# print(f"가사에서 left는 {song.count('left')}개, right는 {song.count('right')}개")
# print(f"가사의 길이는 {len(song)}")

a = "mega"
b = "study"
c = a + b  # + 문자열 연결 연산자  결과:megastudy
d = a * 3  # * 문자열 반복 연산자  결과:megamegamega
e = a[0]  # [] 문자열 인덱싱     결과:m
f = b[0:3]  # [start:end] 문자열 슬라이싱(end제외) 결과:stu
g = 'g' in a  # "mega"에서 'g'가 있니? 결과: True or False




# title = "megastudy python programming"
# print(title.split()) #빈공간 기준으로 str에서 list만들어주기
# title1 = "orange,apple,banana"
# print(title1.split(','))

# user한테 이메일주소 입력받고 -> ['유저아이디,'도메인']
# ex) sls1599@hanmail.net ['sls1599', 'hanmail.net']
# user = input("이메일 입력:")
# a = user.split("@"))  #['sls1599', 'hanmail.net]
# b = a[1].split('.')      #['hanmial','net']
# a[1] = b[0]     #['sls1599', 'hanmail']
# # a[2] = b[1] a[2]가 없으므로 안됨
# a.append(b[1])
# print(a) 



# join
# word = ' 'join(['ice','cream']) # 'ice cream'
# id = input("아이디 입력:")
#domain = input("도메인 입력:")
# print ('@'.join([id,domain])

article = """ 
Acer has announced a lengthy list of new products at CES 2024 in Las Vegas,
including a 57-inch monitor with curvature designed to increase your field of vision and make you feel more immersed in a game's environment.
The king-sized Predator Z57 has a Dual UHD resolution — that's 7,680 x 2,160 pixels — a 120Hz refresh rate and a wide 32:9 aspect ratio. 
It's a MiniLED monitor that Acer says can achieve up to 1,000-nit brightness,
can produce highly accurate colors and can maximize light and dark contrast for realistic visuals and dark scenes with great picture quality.
"""

newArticle = article.replace('after','before').replace('it','😊').split()
print(newArticle)




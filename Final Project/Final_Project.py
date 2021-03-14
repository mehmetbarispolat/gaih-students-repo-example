questions = ["Türkiye'nin başkenti neresidir?",
"Japonların geleneksel güreşine ne ad verilir?",
"Deniz yolculuğunda toplu insan taşımacılığında kullanılan araçların ortak adı?",
"Kurutulmuş yaprakları demlendirilerek içilen bitki?","Ölenden geriye kalan mal veya para",
"Ağırlık ölçüsü içinde bin kilogramlık bir yük kaç ton gelir?",
"Şirketlere ait hisseler nerede alınır satılır?",
"TC kimlik numaramız kaç harften oluşur?",
"Yeni bir işe girerken, iş yerlerine verdiğimiz kısa öz geçmişin kısa adı",
"Lakin ve fakatın eş anlamlısı"]
answers = ["Ankara","Sumo","Vapur","Çay","Miras","1 ton",'Borsa','11','CV','Ama']
LEN_ARRAY = len(questions)
count = 0
for i in range(LEN_ARRAY):
    print(questions[i])
    user_answer = input("Answer --> ")
    if user_answer == answers[i]:
        count += 1

worth = count * 10
if count > 5:
    print(f'success {worth} points')
else:
    print(f'fail {worth} points')

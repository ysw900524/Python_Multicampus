#사전형 함수

customer = {
    "name"  : "김진수",
    "gender": "남자",
    "email" : "bigpycraft@gmail.com",
    "company": "빅파이크래프스",
    "address": "서울시 중구 청파로"
}

print('customer.keys()      \t= ', customer.keys())
print('customer.values()    \t= ', customer.values())
print('customer.items()     \t= ', customer.items())
print('-'*50)

for key, value in customer.items():
    print('%s\t : %s' %(key, value))


    # customer.keys()      	=  dict_keys(['name', 'gender', 'email', 'company', 'address'])
    # customer.values()    	=  dict_values(['김진수', '남자', 'bigpycraft@gmail.com', '빅파이크래프스', '서울시 중구 청파로'])
    # customer.items()     	=  dict_items([('name', '김진수'), ('gender', '남자'), ('email', 'bigpycraft@gmail.com'), ('company', '빅파이크래프스'), ('address', '서울시 중구 청파로')])
    # --------------------------------------------------
    # name	 : 김진수
    # gender	 : 남자
    # email	 : bigpycraft@gmail.com
    # company	 : 빅파이크래프스
    # address	 : 서울시 중구 청파로
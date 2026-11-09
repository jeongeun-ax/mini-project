# 쇼핑몰 타이틀 
def show_title():
    print("-"*70)
    print("1.상품목록  2.담기  3.빼기  4.장바구니  5.쿠폰  6.결제  q.종료")
    print("-"*70)

# 메뉴 선택 
def ask_menu():
    while True:
        user_answer = input("선택: ").strip()

        if user_answer in ("1", "2", "3", "4", "5", "6"):
            return int(user_answer)

        if user_answer == "q":
            print("종료합니다.")
            break
        
        print("1 ~ 6 중에서 입력하세요.")
    

# 판매 상품 목록  
products_list = [
    ("이어폰", 5000, 3),
    ("배터리", 15000, 1),
    ("텀블러", 50000, 10),
]

# 판매 상품 목록 출력 
def show_products():
    for i, product in enumerate(products_list, start=1):
        print(f"{i}. {product[0]}  {product[1]:,}원     (재고{product[2]}개)")


show_title()
menu = ask_menu()

if menu == 1:
    show_products()
    
def show_title():
     print("-"*70)
     print("1.상품목록  2.담기  3.빼기  4.장바구니  5.쿠폰  6.결제  q.종료")
     print("-"*70)
show_title()

# 상품 클래스 
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = int(price)
        self.stock = int(stock)

    # 1. 상품 목록 
    def product_list(self):
        for i, product in enumerate(products, start=1):
            print(f"{i}. {product.name}  {product.price:,}원  (재고 {product.stock}개)")

    def show(self):
        return f"{self.name}  {self.price:,}원  재고 {self.stock}개"


# 장바구니 클래스 
class Cart:
    def __init__(self):
        self.items = {}

    # 장바구니 담기 
    def add(self, product, quantity):
        if quantity > product.stock:
            print(f"재고가 부족합니다. (담을 수 있는 수량: {product.stock}개)")
            return
        
        if product in self.items:
            self.items[product] += quantity
        else:
            self.items[product] = quantity

        product.stock -= quantity

        print(f"{product.name}을/를 {quantity}개 담았습니다.")


    # 장바구니 빼기 

cart = Cart()


# 상품 목록 
product_a = Product("무선 이어폰", 1000, 10)
product_b = Product("텀블러", 15000, 1)
product_c = Product("보조배터리", 5000, 0)
product_d = Product("마우스패드", 1200, 8)
product_e = Product("USB허브", 50000, 52)

products = [product_a, product_b, product_c, product_d, product_e]

# ----------------------메뉴 묻기---------------------------- 
def ask_menu():
    while True:
        user_answer = input("선택: ").strip()

        if user_answer == "1":
            product_a.product_list()

        if user_answer == "2":
            product_num = int(input("상품 번호: "))
            quantity = int(input("수량: "))
            if 1 <= product_num <= len(products):
                product = products[product_num - 1]
                cart.add(product, quantity)
            else:
                print("잘못된 상품 번호입니다.")

        if user_answer == "4":
            print("-" * 50)
            
            print("-" * 50)

            
        if user_answer == "q":
            print("종료")
            break

ask_menu()

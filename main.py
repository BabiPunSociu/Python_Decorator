# 1, Python Decorator là gì?
# - Python decorator là cách thay đổi hành vi (behavior) của
#     một object callable mà không cần can thiệp và chỉnh sửa
#     object đó.

# - Decorator là một hàm có nhiệm vụ bao bọc một hàm khác (ta 
#      tạm gọi là hàm B), hàm B sẽ được gọi bên trong thân của
#      hàm decorator, và đương nhiên lúc này hàm decorator có 
#      thể bổ sung những đoạn code phía trên và phía dưới vị 
#      trí gọi hàm B.

# Ví dụ:
'''
# Đây là hàm decorator
def decoratorFunc(func):
    # Đây là hàm decorator gọi,
    # ta gọi là extend decorated function
    def addStar():
        print("***************************")
        func()
        print('')
        print("***************************")
    return addStar

def showNumbers():
    for i in range( 1, 11):
        print(i, end=' ')

if __name__=='__main__':
    add_star = decoratorFunc(showNumbers)
    add_star()
'''

# 2, Tạo decorator bằng dấu @:
# - sử dụng dấu @ để đánh dấu một phương thức sẽ được trang
#      trí (decorator) bằng một phương thức khác

# Ví dụ như trên:
'''
def decoratorFunc(func):
    # Đây là hàm decorator gọi,
    # ta gọi là extend decorated function
    def addStar(n):
        print("***************************")
        func(n)
        print('')
        print("***************************")
    return addStar

@decoratorFunc
def showNumbers(n):
    for i in range( 1, n+1):
        print(i, end=' ')

if __name__=='__main__':
    # Gọi đơn giản hơn
    showNumbers(10)
'''

# 3, Multi Decorator trong python: (áp dụng nhiều decorator)
# - Thứ tự áp dụng, thực hiện các trang trí là từ dưới lên
# - Ví dụ
def make_the_a(func):
    def add():
        print("\t<a>")
        func()
        print("\t</a>")
    return add

def make_the_div(func):
    def add():
        print("<div>")
        func()
        print("</div>")
    return add

# Thứ tự từ dưới lên: thẻ a -> thẻ div
@make_the_div
@make_the_a
def showMsg():
    print('\t\tBabipunsociu')

if __name__=='__main__':
    showMsg()

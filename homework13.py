#Вызовите функцию inner_function внутри функции test_function

def test_function():

    def inner_function():
        print('Я в зоне видимости функции test_function')
    inner_function()
test_function()


#Попробуйте вызывать inner_function вне функции test_function и посмотрите на результат выполнения программы

# def test_function():
#
#     def inner_function():
#         print('Я в зоне видимости функции test_function')
# inner_function()
# test_function()
#


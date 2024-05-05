from core.lexer import MyLexer
from core.parser import MyParser
from core.memory import Memory

if __name__ == '__main__':
    lexer = MyLexer()
    parser = MyParser()

    while True:
        try:
            data = input('>> ')
        except EOFError:
            break
        if data:
            memory = Memory()
            parser.parse(lexer.tokenize(data))
            print(memory)

    # data = '''10+9'''
    # result = parser.parse(lexer.tokenize(data))
    # print(result)

    # data = open('input.txt','r').read()
    # result = parser.parse(lexer.tokenize(data))
    # print(result)


    # To process a file:
    # file_path = 'input.txt'
    # with open(file_path, 'r') as file:
    #     data = file.read()
    #     memory = Memory()
    #     parser.parse(lexer.tokenize(data))
    #     print(memory)
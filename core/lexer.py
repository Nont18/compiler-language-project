from sly import Lexer
import sly

class MyLexer(Lexer):
    tokens = { NAME, NUMBER, FLOAT, BOOL, NE, GE, LE, EQ, IF, THEN, ELSE, PRINT, STRING, WHILE, DO, AND, OR }
    ignore = ' \t'
    literals = { '=', '+', '-', '*', '/', '(', ')', '.', '>', '<', ':', ';'  } #เครื่องหมายพิเศษต่างๆ (ที่ไม่ใช่ token)
    PRINT = r'print'
    WHILE = r'while'
    DO = r'do'
    IF = r'if'
    THEN = r'then'
    ELSE = r'else'
    # NAME['True'] = BOOL
    # NAME['False'] = BOOL
    # NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
    AND = r'&&'
    OR = r'OR'
    GE = r'>='
    LE = r'<='
    EQ = r'=='
    NE = r'!='

    BOOL = r'True|False'
    

    # Define NAME token regex pattern
    @_(r'[a-zA-Z_][a-zA-Z0-9_]*')
    def NAME(self, t):
        if t.value == 'True' or t.value == 'False':
            t.type = self.BOOL
        return t

    @_(r'\".*?\"')  # Regular expression for matching strings enclosed in double quotes
    def STRING(self, t):
        t.value = t.value[1:-1]  # Remove the double quotes
        return t

    @_(r'\d+\.\d+f?')
    def FLOAT(self, t):
        t.value = float(t.value)
        return t

    @_(r'\d+')
    def NUMBER(self, t):
        t.value = int(t.value)
        return t

    @_(r'\n+')
    def newline(self, t):
        self.lineno += t.value.count('\n')

    def error(self, t):
        print("Illegal character '%s'" % t.value[0])
        self.index += 1


if __name__ == '__main__':
    string_input:str = 'True && False OR True == True && False'
    lex:Lexer = MyLexer()
    token: sly.lex.Token
    for token in lex.tokenize(string_input):
        print(token)
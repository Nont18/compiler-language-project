from sly import Parser
from .lexer import MyLexer
from core.memory import Memory

class MyParser(Parser):
    tokens = MyLexer.tokens
    debugfile = 'parser.out'

    precedence = (
        # ('left', IF, THEN, ELSE),
        # ('left', WHILE, DO),
        # ('left', '>', '<', GE, LE),
        ('left', '+', '-'),
        ('left', NE, EQ),
        ('left', '*', '/'),
        # ('right', 'UMINUS'),
        ('left', OR, AND),
        ('nonassoc', '>', '<', GE, LE),
        ('right', 'UMINUS'),
        ('left', WHILE, DO),
        ('left', '(', ')'),
        ('left', IF, THEN, ELSE),
        )

    def __init__(self):
        self.names = { }
        self.memory:Memory = Memory()

    @_('NAME "=" expr')
    def statement(self, p):
        var_name = p.NAME
        value = p.expr
        self.memory.set(variable_name=var_name,value=value, data_type=type(value))
        self.names[p.NAME] = p.expr

    @_('expr')
    def statement(self, p):
        print(p.expr)

    @_('IF "(" expr ")" statement')
    def statement(self, p):
        if p.expr:
            return p.statement

    @_('expr "+" expr')
    def expr(self, p):
        return p.expr0 + p.expr1

    # @_('NAME "+" STRING')
    # def expr(self, p):
    #     if(type(p.STRING)== str):
    #         NA = self.memory.get(variable_name=p.NAME)
    #         self.memory.set(variable_name=p.NAME, value=NA + p.STRING, data_type=str)
    #         return NA + p.STRING
    #     return p.NAME + p.STRING

    @_('expr "-" expr')
    def expr(self, p):
        return p.expr0 - p.expr1

    @_('expr "*" expr')
    def expr(self, p):
        return p.expr0 * p.expr1

    @_('expr "/" expr')
    def expr(self, p):
        return p.expr0 / p.expr1

    ##########################################################################

    @_('expr AND expr')
    def expr(self, p):
        if(p.expr0 and p.expr1 == True):
            #For debug
            # print("This is p.expr0 =" + str(p.expr0))
            # print("This is p.expr1 =" + str(p.expr1))
            return True
        else:
            #For debug
            # print("This is p.expr0 =" + str(p.expr0))
            # print("This is p.expr1 =" + str(p.expr1))
            return False

    @_('expr OR expr')
    def expr(self, p):
        if(p.expr0 or p.expr1 == False):
            return p.expr0
        else:
            return not p.expr0

    ##########################################################################

    @_('expr ">" expr')
    def expr(self, p):
        if(p.expr0>p.expr1):
            return True
        else: return False

    @_('expr GE expr')
    def expr(self, p):
        if(p.expr0>=p.expr1):
            return True
        else: return False

    @_('expr "<" expr')
    def expr(self, p):
        if(p.expr0<p.expr1):
            return True
        else: return False

    @_('expr LE expr')
    def expr(self, p):
        if(p.expr0<=p.expr1):
            return True
        else: return False

    @_('expr EQ expr')
    def expr(self, p):
        if(p.expr0==p.expr1):
            return True
        else: return False

    @_('expr NE expr')
    def expr(self, p):
        if(p.expr0 != p.expr1):
            return True
        else:
            return False

    #####################################################################

    @_('IF expr ">" expr THEN NAME "=" expr')
    def expr(self,p):
        if p.expr0 > p.expr1:
            var_name = p.NAME
            value = p.expr2
            self.memory.set(variable_name=var_name,value=value, data_type=type(value))
            self.names[p.NAME] = p.expr2
        else:
            None

    @_('IF expr ">" expr THEN PRINT "(" STRING ")"')
    def expr(self,p):
        if p.expr0 > p.expr1:
            return p.STRING
        else:
            None

    @_('IF expr GE expr THEN NAME "=" expr')
    def expr(self,p):
        if p.expr0 >= p.expr1:
            var_name = p.NAME
            value = p.expr2
            self.memory.set(variable_name=var_name,value=value, data_type=type(value))
            self.names[p.NAME] = p.expr2
        else:
            None

    @_('IF expr "<" expr THEN NAME "=" expr')
    def expr(self,p):
        if p.expr0 < p.expr1:
            var_name = p.NAME
            value = p.expr2
            self.memory.set(variable_name=var_name,value=value, data_type=type(value))
            self.names[p.NAME] = p.expr2
        else:
            None

    @_('IF expr "<" expr THEN PRINT "(" STRING ")"')
    def expr(self,p):
        if p.expr0 > p.expr1:
            return p.STRING
        else:
            None

    @_('IF expr LE expr THEN NAME "=" expr')
    def expr(self,p):
        if p.expr0 <= p.expr1:
            var_name = p.NAME
            value = p.expr2
            self.memory.set(variable_name=var_name,value=value, data_type=type(value))
            self.names[p.NAME] = p.expr2
        else:
            None

    @_('IF expr EQ expr THEN NAME "=" expr')
    def expr(self,p):
        if p.expr0 == p.expr1:
            var_name = p.NAME
            value = p.expr2
            self.memory.set(variable_name=var_name,value=value, data_type=type(value))
            self.names[p.NAME] = p.expr2
        else:
            None

    @_('IF expr EQ expr THEN PRINT "(" STRING ")"')
    def expr(self,p):
        if p.expr0 == p.expr1:
            return p.STRING
        else:
            None

    @_('IF expr EQ expr THEN PRINT "(" NUMBER ")"')
    def expr(self,p):
        if p.expr0 == p.expr1:
            return p.NUMBER
        else:
            None

    @_('IF expr ">" expr THEN NAME "=" expr ELSE NAME "=" expr')
    def expr(self, p):
        if p.expr0 > p.expr1:
            var_name = p.NAME0
            value = p.expr2
            self.memory.set(variable_name=var_name,value=value, data_type=type(value))
            self.names[p.NAME0] = p.expr2
        else:
            var_name = p.NAME1
            value = p.expr3
            self.memory.set(variable_name=var_name,value=value, data_type=type(value))
            self.names[p.NAME1] = p.expr3

    @_('IF expr ">" expr THEN PRINT "(" STRING ")" ELSE PRINT "(" STRING ")"')
    def expr(self,p):
        if p.expr0 > p.expr1:
            return p.STRING0
        else:
            return p.STRING1

    @_('IF expr GE expr THEN NAME "=" expr ELSE NAME "=" expr')
    def expr(self, p):
        if p.expr0 >= p.expr1:
            var_name = p.NAME0
            value = p.expr2
            self.memory.set(variable_name=var_name,value=value, data_type=type(value))
            self.names[p.NAME0] = p.expr2
        else:
            var_name = p.NAME1
            value = p.expr3
            self.memory.set(variable_name=var_name,value=value, data_type=type(value))
            self.names[p.NAME1] = p.expr3

    @_('IF expr "<" expr THEN NAME "=" expr ELSE NAME "=" expr')
    def expr(self, p):
        if p.expr0 < p.expr1:
            var_name = p.NAME0
            value = p.expr2
            self.memory.set(variable_name=var_name,value=value, data_type=type(value))
            self.names[p.NAME0] = p.expr2
        else:
            var_name = p.NAME1
            value = p.expr3
            self.memory.set(variable_name=var_name,value=value, data_type=type(value))
            self.names[p.NAME1] = p.expr3

    @_('IF expr "<" expr THEN PRINT "(" STRING ")" ELSE PRINT "(" STRING ")"')
    def expr(self,p):
        if p.expr0 < p.expr1:
            return p.STRING0
        else:
            return p.STRING1

    @_('IF expr LE expr THEN NAME "=" expr ELSE NAME "=" expr')
    def expr(self, p):
        if p.expr0 <= p.expr1:
            var_name = p.NAME0
            value = p.expr2
            self.memory.set(variable_name=var_name,value=value, data_type=type(value))
            self.names[p.NAME0] = p.expr2
        else:
            var_name = p.NAME1
            value = p.expr3
            self.memory.set(variable_name=var_name,value=value, data_type=type(value))
            self.names[p.NAME1] = p.expr3

    @_('IF expr EQ expr THEN NAME "=" expr ELSE NAME "=" expr')
    def expr(self, p):
        if p.expr0 == p.expr1:
            var_name = p.NAME0
            value = p.expr2
            self.memory.set(variable_name=var_name,value=value, data_type=type(value))
            self.names[p.NAME0] = p.expr2
        else:
            var_name = p.NAME1
            value = p.expr3
            self.memory.set(variable_name=var_name,value=value, data_type=type(value))
            self.names[p.NAME1] = p.expr3

    @_('IF expr EQ expr THEN PRINT "(" STRING ")" ELSE PRINT "(" STRING ")"')
    def expr(self,p):
        if p.expr0 == p.expr1:
            return p.STRING0
        else:
            return p.STRING1

    ####################################################################

    @_('"-" expr %prec UMINUS')
    def expr(self, p):
        return -p.expr

    @_('"(" expr ")"')
    def expr(self, p):
        return p.expr

    @_('NUMBER')
    def expr(self, p):
        return p.NUMBER

    @_('FLOAT')
    def expr(self, p):
        return p.FLOAT

    @_('BOOL')
    def expr(self, p):
        return p.BOOL

    @_('STRING')
    def expr(self,p):
        return p.STRING

    @_('PRINT "(" expr ")"')
    def expr(self, p):
        print(p.expr)

    @_('PRINT "(" expr ")"')
    def statement(self, p):
        print(p.expr)

    ###############################################################

    # @_('WHILE "(" expr ")" DO expr')
    # def expr(self, p):
    #     result = None
    #     #print("Dung")
    #     # string = p.expr1[6:str(p.expr1)]
    #     while p.expr0:
    #         # print("This is p.expr0 = " + str(p.expr0))
    #         # print("This is p.expr1 = " + str(p.expr1))
    #         result = p.expr1
    #         print(result)
    #     return result

    # @_('WHILE "(" expr ")" DO expr')
    # def expr(self, p):
    #     while p.expr0:
    #         return p.expr1
    #     return p.expr1

    @_('WHILE "(" expr ")" DO PRINT "(" expr ")"')
    def expr(self, p):
        while p.expr0:
            print(p.expr1)
        # return p.expr1

    @_('WHILE "(" expr ")" DO PRINT "(" NUMBER ")"')
    def expr(self, p):
        while p.expr0:
            print(p.NUMBER)


    @_('WHILE "(" expr ")" DO expr NAME "=" expr "-" expr')
    def expr(self, p):
        value = p.expr2 - p.expr3
        while value>0:
            print(value)
            var_name = p.NAME
            self.memory.set(variable_name=var_name, value=value, data_type=type(value))
            self.names[p.NAME] = value
            value=value-p.expr3

    @_('WHILE "(" expr ")" DO NAME "=" expr "*" expr NAME "=" expr "-" expr PRINT "(" NAME ")"')
    def expr(self, p):
        N0 = p.expr1 * p.expr2
        N1 = p.expr3 - p.expr4
        while N1>0:
            N0 = N0 * N1
            N1 = N1-1
            self.memory.set(variable_name=p.NAME0, value=N0, data_type=type(N0))
            self.memory.set(variable_name=p.NAME1, value=N1, data_type=type(N1))
            self.names[p.NAME0] = N0
            self.names[p.NAME1] = N1
        print(N0)

    
    

    @_('NAME')
    def expr(self, p):
        try:
            return self.names[p.NAME]
        except LookupError:
            print("Undefined name '%s'" % p.NAME)
            return 0

   

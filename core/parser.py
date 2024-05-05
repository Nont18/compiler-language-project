from sly import Parser
from .lexer import MyLexer
from core.memory import Memory

class MyParser(Parser):
    tokens = MyLexer.tokens
    debugfile = 'parser.out'

    precedence = (
        ('left', '+', '-'),
        ('left', NE, EQ),
        ('left', '*', '/'),
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
            return True
        else:
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
        if p.expr0 > p.expr1:
            return p.STRING
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


    @_('WHILE "(" expr ")" DO PRINT "(" expr ")"')
    def expr(self, p):
        while p.expr0:
            print(p.expr1)
        # return p.expr1

    

    @_('NAME')
    def expr(self, p):
        try:
            return self.names[p.NAME]
        except LookupError:
            print("Undefined name '%s'" % p.NAME)
            return 0

   

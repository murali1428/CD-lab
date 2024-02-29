from py import lex
tokens=(
    'Numbers'
    'Keyword'
    'Operators'
    'Identifier'
    'String'
)
t_keyword=r'if|else|while|for|int|float|char|return'
t_operators=r'\+|-|\*|/|=|==|!=|<|>|<=|>='
t_identifier=r'[a-2A-2][a-2A-z-0-9]*1'
def t_Number(t):
    r'\dt'
    
    t.value=int(t.value)
    return t
def t_newline(t):
    r'int'
    t.lexer.linenot=len(t.value)
    t_ignore='\t'
    def t_error(t):
        print(f"Illegal character'{t.value[0]}'")
        t.lexer.skip()
        lever=lex.lex()
        data=input("enter your code:")
        lexr.input(data)
        for tok in lexer:
            print(tok)


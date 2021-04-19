import re

def load_file():
    arq = open('fileSample.go', 'r')
    text = arq.readline()

    buffer = []
    cont = 1

        # The buffer size can be changed by changing cont
    while text != "":
        buffer.append(text)
        text = arq.readline()
        cont += 1

        if cont == 10 or text == '':
            # Return a full buffer
            buf = ''.join(buffer)
            cont = 1
            yield buf

            # Reset the buffer
            buffer = []

    arq.close()



arr = []
def tokenize(code):
    rules = [
        ('PACKAGE', r'package'),    # package
        ('MAIN', r'main'),          # main
        ('IMPORT', r'import'),      # import
        ('FMT', r'fmt'),            # fmt
        ('FUNCTION', r'func'),      # func
        ('NIL', r'nil'),
        ('DEFAULT', r'default'),
        ('SELECT', r'select'),
        ('CASE', r'case'),
        ('GO', r'go'),
        ('STRUCT', r'struct'),
        ('SWITCH', r'switch'),
        ('CONST', r'const'),
        ('FOR', r'for'),
        ('VAR', r'var'),
        ('TRUE', r'true'),
        ('FALSE', r'false'),
        ('ACCESSOR', r'\.'), # still to edit
        ('FUNCTIONID',	r'[a-zA-Z_][a-zA-Z0-9_]*(?=([ \t]+)?\()'), # Function Identifier
        ('PREDEFINED_TYPES', r'((int)|(float)|(char)|(string)|(bool))'), # predefined datatypes
        ('IDENTIFIERS', r'[a-zA-Z_@][a-zA-Z_0-9]*'),     # IDENTIFIERS
        ('FLOAT_LIT', r'([0-9]+\.([0-9]+)?((e|E)(\+|\-)?[0-9]+)?)|([0-9]+(e|E)(\+|\-)?[0-9]+)|(\.[0-9]+((e|E)(\+|\-)?[0-9]+)?)'),
        ('STRING_LIT', r'(\"[^(\")]*\")|\`((\\x[0-9A-Fa-f]{2})|(\\u[0-9A-Fa-f]{4})|(\\U[0-9A-Fa-f]{8})|(\\[0-7]{3})|(\\(a|b|f|n|r|t|v|\\|\'|\"))|([^(\`)]))*\`'),
        ('COMMENT', r'(/\*([^*]|\n|(\*+([^*/]|\n])))*\*+/)|(//.*)'), # for comments
        ('BREAK', r'break'),
        ('CONTINUE', r'continue'),
        ('RETURN', r'return'),
        ('IF', r'if'),              # if
        ('ELSE', r'else'),          # else
        ('WHILE', r'while'),        # while
        ('PRINT', r'print'),        # print
        ('PRINTLN', r'Println'),    # print-line
        ('PRINTF', r'Printf'),      # print-format
        ('LBRACKET', r'\('),        # (
        ('RBRACKET', r'\)'),        # )
        ('LBRACE', r'\{'),          # {
        ('RBRACE', r'\}'),          # }
        ('COMMA', r','),            # ,
        ('PCOMMA', r';'),           # ;
        ('EQ', r'=='),              # ==
        ('ASSIGN', r':='),          # ==
        ('NE', r'!='),              # !=
        ('LE', r'<='),              # <=
        ('GE', r'>='),              # >=
        ('OR', r'\|\|'),            # ||
        ('AND', r'&&'),             # &&
        ('ATTR', r'\='),            # =
        ('LT', r'<'),               # <
        ('GT', r'>'),               # >
        ('PLUS', r'\+'),            # +
        ('MINUS', r'-'),            # -
        ('MULT', r'\*'),            # *
        ('DIV', r'\/'),             # /
        ('INTEGER_CONST', r'\d(\d)*'), # INT
        ('NEWLINE', r'\n'),         # NEW LINE
        ('SKIP', r'[ \t]+'),        # SPACE and TABS
        ('MISMATCH', r'.'),         # ANOTHER CHARACTER
    ]
    # Token row
    lin_num = 1
    tokens_join = '|'.join('(?P<%s>%s)' % x for x in rules)
    lin_start = 0

    # Lists of output for the program
    token = []
    lexeme = []
    row = []
    column = []
    

    # It analyzes the code to find the lexemes and their respective Tokens
    for m in re.finditer(tokens_join, code):
        token_type = m.lastgroup
        token_lexeme = m.group(token_type)

        if token_type == 'NEWLINE':
            lin_start = m.end()
            lin_num += 1
        elif token_type == 'SKIP':
            continue
        elif token_type == 'MISMATCH':
            raise RuntimeError('%r unexpected on line %d' % (token_lexeme, self.lin_num))
        else:
            col = m.start() - lin_start
            column.append(col)
            token.append(token_type)
            lexeme.append(token_lexeme)
            row.append(lin_num)

            # To print information about a Token
            resp = 'Token = {0}, Lexeme = \'{1}\', Row = {2}, Column = {3}'.format(token_type, token_lexeme, lin_num, col)
            
            # Display in terminal
            print(resp)
            arr.append(resp)

    # Write to file
    with open('tokenInfo.txt', mode='w') as f:
        for i in arr:
            f.write(i)
            f.write('\n')

    return token, lexeme, row, column


if __name__ == '__main__':
    
    # Lists for every list returned list from the function tokenize
    token = []
    lexeme = []
    row = []
    column = []

    # Tokenize and reload of the buffer
    for i in load_file():
        t, lex, lin, col = tokenize(i)
        token += t
        lexeme += lex
        row += lin
        column += col

    # Display recognizable token in terminal
    print('\nRecognize Tokens: ', token)

    # Write recognizable tokens to file
    with open('recognizableToken.txt', mode='w') as f:
        f.write("\nRecognize Tokens: ")
        f.writelines("%s\n" % line for line in token)

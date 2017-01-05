__author__ = 'Pranav'
import sys
import re

# Reserved words
tokens =(
    # Literals (identifier, integer constant, float constant, string constant, char const)
    'i'
)
 
# Newlines
def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

# Identifiers and reserved words
t_ID =r'[A-Za-z_][\w_]*'

# Integer literal
t_ICONST = r'\d+([uU]|[lL]|[uU][lL]|[lL][uU])?'

# Floating literal
t_FCONST = r'((\d+)(\.\d+)(e(\+|-)?(\d+))?|(\d+)e(\+|-)?(\d+))([lL]|[fF])?'

    
#Tokenize the input string
def tokenize(line):
    line=re.subn(t_FCONST,'i',line)[0]
    line=re.subn(t_ICONST,'i',line)[0]
    line=re.subn(t_ID,'i',line)[0]
    return line
    

# Matches > 6 char alphanumeric only password with at least: 1 number, 1 lowercase, 1 uppercase.
regex_compiled = '^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])[a-zA-Z\d]{6,}$'

# These compile and VERBOSE are useful for documenting what your regex does, then compiling it for use later.
from re import compile, VERBOSE
regex = compile("""
^              # begin word
(?=.*?[a-z])   # at least one lowercase letter
(?=.*?[A-Z])   # at least one uppercase letter
(?=.*?[0-9])   # at least one number
[A-Za-z\d]     # only alphanumeric
{6,}           # at least 6 characters long
$              # end word
""", VERBOSE)

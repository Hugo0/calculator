##############################################
# Any good programmer uses tests
# to be sure that his software works!
# We are good programmers, 
# so lets do that too!
##############################################

from calculator import add

assert add(1, 2) == 3
assert add(4, 7) == 11
assert add (23, 3) == 26
print('-- all tests worked! --')

# whew okay, that was a lot of tests. Nothing broke
# so it seems like its working. 
# :)
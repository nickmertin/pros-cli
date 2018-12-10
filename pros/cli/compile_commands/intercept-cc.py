import sys
from libscanbuild.intercept import intercept_compiler_wrapper

if __name__ == '__main__':
    sys.exit(intercept_compiler_wrapper())

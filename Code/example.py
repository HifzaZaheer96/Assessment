#!/usr/bin/env python3
def endsPy(input):
    for i in range(len(input)):
        if input[i-1] == "y" or input[i-1] == "Y" and input[i-2] == "p"  or input[i-2] =="P":
	        return True
        else:
            return False

# ---------------------------------------------------------------------
# pex_2_helper
# Author: Maj Adrian de Freitas
# Course: CS110Z, Spring 2020
# Description: Provides helper functions to assist with PEX 2
# _NOTE:  Not all functions may be needed
# ---------------------------------------------------------------------
import hashlib

###########################################################
# get_password_hash
# Input:  A string (e.g., "hello"); any whitespace on either side will be removed
# Returns:  A string containing the hash value (all lowercase)
# Description:  Calculates (and returns) the hash value of a string
def get_password_hash(string_to_hash):
    b = string_to_hash.strip().encode('utf-8')
    hash_function = hashlib.md5(b)
    return str(hash_function.hexdigest())




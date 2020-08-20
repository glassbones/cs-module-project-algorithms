'''
Input: an integer
Returns: an integer
'''
# 0, 0, 1, 1, 2, 4, 7, 13, 24, 44, 81, 149, 274, 504, 927, 1705, 3136, 5768, 10609, 19513
def eating_cookies(n):
    trib=[1,1,2]
    if( n <= 2 ): return trib[n]
    for x in range(n-2): trib.append( trib[-1] + trib[-2] + trib[-3] )
    return trib[-1]

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")

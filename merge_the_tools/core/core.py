
#split the string into substrings
#remove duplicates in sub strings
def merge_the_tools(string, k):
    res = []
    len_res=0
    for i in string:
        len_res=len_res+1
        if i not in res:
            res.append(i)
        if len_res == k:
            print (''.join(res))
            res=[]
            len_res=0
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
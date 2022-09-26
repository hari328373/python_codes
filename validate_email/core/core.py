
#checking the email is valid or not
#using regular expression methods
import re
def fun(s):
    pattern="^[a-zA-Z0-9\-\_]+@[A-Za-z0-9]+[\.][a-zA-Z]{1,3}$"
    return re.search(pattern,s)!=None # return the match object
def filter_mail(emails):
    return list(filter(fun, emails)) #filter the emails from input accpording to condition (pattern)

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(('lara@hackerrank.com','brian-23@hackerrank.com','britts_54@hackerrank.com'))
filtered_emails.sort() # sort the emails
print(filtered_emails)
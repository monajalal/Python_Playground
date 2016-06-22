'''
The new "Avengers" movie has just been released! There are a lot of people at the cinema
box office standing in a huge line. Each of them has a single 100, 50 or 25 dollars bill.
A "Avengers" ticket costs 25 dollars. Vasya is currently working as a clerk. He wants to
sell a ticket to every single person in this line. Can Vasya sell a ticket to each person
and give the change if he initially has no money and sells the tickets strictly in the
order people follow in the line? Return YES, if Vasya can sell a ticket to each person
and give the change. Otherwise return NO.
Examples:
### Python ###
tickets([25, 25, 50]) # => YES
tickets([25, 100])
         # => NO. Vasya will not have enough money to give change to 100 dollars
'''

def tickets(people):
    sum = 0
    for p in people:
        if p < 25:
            return 'NO'
        if p == 25:
            sum += p
        elif p > 25:
            if (sum - p) <0 :
                return 'NO'
  #          else:
  #              sum += p
    return 'YES'

print(tickets([25, 25, 50])) #YES
print(tickets([25, 100])) #NO
print(tickets([25, 25, 50, 50, 50])) #YES
print(tickets([25, 25, 25, 25, 50, 100, 50])) #YES

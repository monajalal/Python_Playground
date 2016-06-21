'''
We give you an Array of friend's list.

Write a method called greetingForAllFriends, with this signature:

greeting_for_all_friends(friends)
This method takes an array of friends name and return a greeting messages Array.

Message sample: for the friend "Bilal" we get "Hello, Bilal!"

Rules:

If the argument is null, the method should return null/nil/None according to the
given language (null for JS, None for Python and so on). If the argument is an
empty array, the method should return null/nil/None, as stated above. If the
argument is a valide array of strings, the method should return a hello message
 for every array entry

test.expect(greeting_for_all_friends(None) is None, "Must return None for None as input")
test.expect(greeting_for_all_friends([]) is None, "Must return None for empty list as input")
test.expect(greeting_for_all_friends(["Bilal"]) is not None, "Must not return None for an input")
test.assert_equals(greeting_for_all_friends(["Bilal"]), ["Hello, Bilal!"])


'''

def greeting_for_all_friends(friends):
    greeting_list = []
    if len(friends) == 0:
        return None
    if friends is None:
        return None
    else:
        for friend in friends:
            greeting_list.append("Hello, {}!".format(friend))
    return greeting_list
print(greeting_for_all_friends([]))


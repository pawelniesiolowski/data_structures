# Active Directory

This is a common recursive problem. To provide an efficient look up for user in groups
I search user for each group and then recursively - users in groups in group...
If user is found the function returns True immediately, but I have to check if returned value is True
before I stop function execution - recursive calling could return False if it doesn't found user
after checking all groups in groups.

Time complexity is O(n) where "n" is number of users and groups.
Space complexity is O(m) where "m" is depth of recursion.


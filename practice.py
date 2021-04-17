for left in range(7):
    for right in range(left, 7):
        print("[" + str(left) + "|" + str(right) + "]", end=" ")
    print()

# list of elements to calculate median
n_num = [1, 12, 3, 4, 15, 6, 7, 8, 19]
n = len(n_num)
n_num.sort()

if n % 2 == 0:
    median1 = n_num[n]
    median2 = n_num[n]
    median = (median1 + median2) / 2
else:
    median = n_num[n // 2]
print("Median is: " + str(median))


def groups_per_user(group_dictionary):
    user_groups = {}
    for group, users in group_dictionary.items():
        for user in users:
            if user not in user_groups:
                user_groups[user] = []
            user_groups[user].append(group)
    return user_groups


print(groups_per_user({"local": ["admin", "userA"],
                       "public": ["admin", "userB"],
                       "administrator": ["admin"]}))


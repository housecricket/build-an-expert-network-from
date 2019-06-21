from collections import Counter
from collections import defaultdict
from data import *

# Initialize the dict with an empty list for each expert id:
friendships = {expert["id"]: [] for expert in experts}

# And loop over the friendship pairs to populate it:
for i, j in friendship_pairs:
    friendships[i].append(j)  # Add j as a friend of expert i
    friendships[j].append(i)  # Add i as a friend of expert j


def number_of_friends(expert):
    expert_id = expert["id"]
    friend_ids = friendships[expert_id]
    return len(friend_ids)

# 24
total_connections = sum(number_of_friends(expert) for expert in experts)
# length of the users list
num_experts = len(experts)           
# 24 / 10 == 2.4                
avg_connections = total_connections / num_experts   

# Create a list (user_id, number_of_friends).
num_friends_by_id = [(expert["id"], number_of_friends(expert))
                     for expert in experts]

# Sort the list
num_friends_by_id.sort(                                
       key=lambda id_and_friends: id_and_friends[1],   # by num_friends
       reverse=True)                                   # largest to smallest

# Each pair is (expert_id, num_friends):
# [(1, 3), (2, 3), (3, 3), (5, 3), (8, 3),
#  (0, 2), (4, 2), (6, 2), (7, 2), (9, 1)]

# foaf is short for "friend of a friend"
def foaf_ids_bad(expert):
    return [foaf_id
            for friend_id in friendships[expert["id"]]
            for foaf_id in friendships[friend_id]]

def friends_of_friends(expert):
    expert_id = expert["id"]
    return Counter(
        foaf_id
        # For each of my friends,
        for friend_id in friendships[expert_id]     
        # find their friends
        for foaf_id in friendships[friend_id]   
        # who aren't me  
        if foaf_id != expert_id       
         # and aren't my friends.              
        and foaf_id not in friendships[expert_id]  
    )

# print(friends_of_friends(experts[1]))               
# Counter({0: 2, 5: 1})

#Find the ids of all users who like the target interest.
def data_scientists_who_like(target_interest):
    return [expert_id
            for expert_id, expert_interest in interests
            if expert_interest == target_interest]

   

# Keys are interests, values are lists of expert_id with that interest
expert_ids_by_interest = defaultdict(list)

for expert_id, interest in interests:
    expert_ids_by_interest[interest].append(expert_id)

# Keys are expert_ids, values are lists of interests for that expert_id.
interests_by_expert_id = defaultdict(list)

for expert_id, interest in interests:
    interests_by_expert_id[expert_id].append(interest)

def most_common_interests_with(expert):
    return Counter(
        interested_expert_id
        for interest in interests_by_expert_id[expert["id"]]
        for interested_expert_id in expert_ids_by_interest[interest]
        if interested_expert_id != expert["id"]
    )

# print(most_common_interests_with(experts[1]))

# Keys are years, values are lists of the salaries for each tenure.
income_by_tenure = defaultdict(list)

for income, tenure in incomes_and_tenures:
    income_by_tenure[tenure].append(income)

# Keys are years, each value is average salary for that tenure.
average_income_by_tenure = {
    tenure: sum(incomes) / len(incomes)
    for tenure, incomes in income_by_tenure.items()
}

# print(average_income_by_tenure)

def tenure_bucket(tenure):
    if tenure < 2:
        return "less than two"
    elif tenure < 5:
        return "between two and five"
    else:
        return "more than five"

# Keys are tenure buckets, values are lists of incomes for that bucket.
income_by_tenure_bucket = defaultdict(list)

for income, tenure in incomes_and_tenures:
    bucket = tenure_bucket(tenure)
    income_by_tenure_bucket[bucket].append(income)


# Keys are tenure buckets, values are average income for that bucket.
average_income_by_bucket = {
  tenure_bucket: sum(incomes) / len(incomes)
  for tenure_bucket, incomes in income_by_tenure_bucket.items()
}

print(average_income_by_bucket)
from collections import Counter
from collections import defaultdict

experts = [
    {"id": 0, "name": "Bill Gates"},
    {"id": 1, "name": "Mark Zuckerberg"},
    {"id": 2, "name": "Steve Jobs"},
    {"id": 3, "name": "Jeff Bezos"},
    {"id": 4, "name": "Ha Dong Nguyen"},
    {"id": 5, "name": "Trung Anh Dang"},
    {"id": 6, "name": "Sundar Pichai"},
    {"id": 7, "name": "Larry Page"},
    {"id": 8, "name": "Sergey Brin"},
    {"id": 9, "name": "Tim Cook"}
]

interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
    (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
    (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
    (3, "statistics"), (3, "regression"), (3, "probability"),
    (4, "machine learning"), (4, "regression"), (4, "decision trees"),
    (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
    (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
    (6, "probability"), (6, "mathematics"), (6, "theory"),
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
    (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
    (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
    (9, "Java"), (9, "MapReduce"), (9, "Big Data")
]

friendship_pairs = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
                    (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

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

# print(friends_of_friends(experts[1]))               # Counter({0: 2, 5: 1})

#Find the ids of all users who like the target interest.
def data_scientists_who_like(target_interest):
    return [expert_id
            for expert_id, expert_interest in interests
            if expert_interest == target_interest]

   

# Keys are interests, values are lists of user_ids with that interest
expert_ids_by_interest = defaultdict(list)

for expert_id, interest in interests:
    expert_ids_by_interest[interest].append(expert_id)

# Keys are user_ids, values are lists of interests for that expert_id.
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

print(most_common_interests_with(experts[1]))
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
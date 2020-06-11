import random
from util import Queue


def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        q = Queue()
        q.enqueue(starting_vertex)
        visited = set()
        routes = {}
        best_route = []
        while q.size() > 0:
            v = q.dequeue()
            
            if v not in visited:
                if v == destination_vertex:
                    # return routes
                    cur = destination_vertex
                    while cur != starting_vertex:
                        for v in visited:
                            if cur in routes[v]:
                                best_route.insert(0, v)
                                cur = v
                    best_route.append(destination_vertex)
                    return best_route
                visited.add(v)
                neighbors = set()
                for next_vert in self.get_neighbors(v):
                    q.enqueue(next_vert)
                    neighbors.add(next_vert)
                routes[v] = neighbors

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(num_users):
            self.add_user(i)

        # Create friendships
        friendship_cache = set()
        for user in self.users:
            for friend in self.users:
                if friend is not user:
                    if (user, friend) not in friendship_cache and (friend, user) not in friendship_cache:
                        # self.add_friendship(user, friend)
                        # friendship_cache[(user, friend)] = True
                        friendship_cache.add((user, friend))
        all_possible_friendships = list(friendship_cache)

        random.shuffle(all_possible_friendships)

        filtered_friendships = []

        for i in range(len(all_possible_friendships)//((num_users-2)//avg_friendships)):
            filtered_friendships.append(all_possible_friendships[i])

        print('friendship_cache: ', filtered_friendships)
        
        for friendship in filtered_friendships:
            self.add_friendship(friendship[0], friendship[1])
        # for friendship in all_possible_friendships:
        #     self.add_friendship(friendship[0], friendship[1])
                    

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        q = Queue()
        q.enqueue([user_id])
        routes = {}
        
        while q.size() > 0:
            cur_path = q.dequeue()
            cur_friend = cur_path[-1]

            if cur_friend not in visited:
                visited[cur_friend] = cur_path
                # Enqueue all 1 more entended friends lists
                neighbors = self.friendships[cur_friend]
                path_copy = cur_path
                for neighbor in neighbors:
                    path_copy.append(neighbor)
                    q.enqueue(path_copy)



        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    num_of_users = 10
    sg.populate_graph(num_of_users, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print('connections :', connections)

    # check average connections
    friends = 0
    for i in range(num_of_users):
        if i in sg.friendships:
            friends += (len(sg.friendships[i]))
    print('Average connections :', friends/num_of_users)

    print(sg.friendships[1])
    
    print('Get all social paths :', sg.get_all_social_paths(1))
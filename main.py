
class User:

    def __int__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0


user_1 = User('001', 'Kings')

user_2 = User('002', 'Chinaza')

print(user_1.id)
#print(user_2)

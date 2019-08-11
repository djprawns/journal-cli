# import sys

# # for arg in sys.argv:
# #     print(arg)

# def login_signup_options():
# 	print("1) Login")
# 	print("2) Sign up")
# 	option = input("(1/2) : ")
# 	return option

# print("######## Welcome to journal-cli! ########")
# print("Type the options number to proceed: -")
# login_signup_options()
# # print(option)

# if option is 1:
# 	#login
# elif option is 2:
# 	#signup
# else:
# 	print("Please enter the correct option")


class SignUp:

	def __init__(self):
		self.username = None
		self.password = None

	def get_username(self):
		print("please enter the username: ")
		username = input("username: ")
		if self.check_if_username_exists(username):
			print("this username already exists, please choose another one: - ")
			self.get_username()
		else:
			

	def check_if_username_exists(self, username):




class Flow:

	commands = ['user', 'log', 'login']

	def __init__(self):
		option = self.login_signup_options()
		while 


	def login_signup_options(self):
		print("1) Login")
		print("2) Sign up")
		option = input("(1/2) : ")
		return option




while True:
	name = input("please enter your name: ")
	if name.isalpha():
		break
	else:
		print("Invalid name")
print(f"Hello {name}")
print("How is the weather today?")

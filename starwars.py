import requests
base_url="https://swapi.co/api/"
people_url=base_url+"people/"

class Base():
	def api_info():
		return requests.get(base_url).json()

class People():
	def get(id=None):
		if id==None:
			print("You need to pass id of character to get output.")
			print("To get list of all characters, use getall() method.")
			return
		return requests.get(people_url+str(id)).json()



if __name__ == "__main__":
	response = People.get(1)
	print(response)


import requests


def get_single_data(get):
    url = f"https://catfact.ninja/{get}"
    data = requests.get(url)
    response = data.json()
    print(response)


def get_multidata(get, data_type):
    url = f"https://catfact.ninja/{get}"
    data = requests.get(url)
    response = data.json()
    dict_data = response["data"]
    for dict_sub_data in dict_data:
        print("*" + dict_sub_data[f"{data_type}"] + "\n")


option = int(
    input(
        "Enter what thing you want to know about cats.\n 1.Fact \n 2.Facts \n 3.Breeds"
    )
)

if option == 1:
    get_single_data("fact")


elif option == 2:
    get_multidata("facts", "fact")

else:
    get_multidata("breeds", "breed")

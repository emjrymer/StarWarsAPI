import requests

film_url = "http://swapi.co/api/films/"
people_url = "http://swapi.co/api/people/"
vehicles_url = "http://swapi.co/api/vehicles/"


def get_data_list(main_filter, sub_filter, url):
    for item in get_json_response(main_filter, url):
        print(get_json_response(sub_filter, item))


def filter_by_person():
    person = "http://swapi.co/api/people/"
    choice = input("Enter number for more details:   ")
    url = person + choice + '/'
    response = requests.get(url)
    json_response = response.json()
    print("name: " + json_response['name'])
    print("gender: " + json_response['gender'])
    print("mass: " + json_response['mass'])
    print("height: " + json_response['height'])
    print("hair color: " + json_response['hair_color'])
    print("skin color: " + json_response['skin_color'])
    print("eye color: " + json_response['eye_color'])
    print("birth year: " + json_response['birth_year'])
    print("movies:  ")
    get_data_list('films', 'title', url)
    print("species: ")
    get_data_list('species', 'name', url)
    print("vehicles: ")
    get_data_list('vehicles', 'name', url)
    print("starships: ")
    get_data_list('starships', 'name', url)


def filter_by_vehicle():
    vehicle = "http://swapi.co/api/vehicles/"
    choice = input("Enter number for more details:   ")
    url = vehicle + choice + '/'
    response = requests.get(url)
    json_response = response.json()
    print("name: " + json_response['name'])
    print("model: " + json_response['model'])
    print("manufacturer: " + json_response['manufacturer'])
    print("cost in credits: " + json_response['cost_in_credits'])
    print("length: " + json_response['length'])
    print("max atmosphering speed: " + json_response['max_atmosphering_speed'])
    print("crew: " + json_response['crew'])
    print("passengers: " + json_response['passengers'])
    print("cargo capacity: " + json_response['cargo_capacity'])
    print("consumables: " + json_response['consumables'])
    print("vehicle class: " + json_response['vehicle_class'])


def filter_by_film():
    film = "http://swapi.co/api/films/"
    choice = input("Enter number for more details:   ")
    url = film + choice + '/'
    response = requests.get(url)
    json_response = response.json()
    print("title: " + json_response['title'])
    print("episode id: " + str(json_response['episode_id']))
    print("director: " + json_response['director'])
    print("producer: " + json_response['producer'])
    print("release date: " + json_response['release_date'])
    print("Top three characters:  ")


#  need to come back and filter down to top three
    get_data_list('characters', 'name', url)


def get_json_response(key, url):
    response = requests.get(url)
    json_response = response.json()
    return json_response[key]


def choosen_results(url, filter, url_end):
    for item in get_json_response("results", url):
        num = item['url'][url_end:-1]
        title = item[filter]
        print("{} -- {}".format(num, title))

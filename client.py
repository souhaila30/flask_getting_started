import requests

def get_name():
    """makes a get request and returns the name"""
    r  = requests.get("http://vcm-3586.vm.duke.edu:5000/name")
    name = r.json()
    print(name)
    return name

def get_hello_name():
    """ makes a get request and returns the  message """
    r = requests.get("http://vcm-3586.vm.duke.edu:5000/hello/souhaila")
    message = r.json()
    print(message)
    return message

def get_distance():
    """makes a post request to the virtual machine and returns the distance"""
    input = {
        "a": [1,1],
        "b": [2,2]
         } 
    r = requests.post("http://vcm-3586.vm.duke.edu:5000/distance", json=input)
    distance = r.json()
    print(distance)
    return distance

def main():
    name = get_name()
    message = get_hello_name()
    distance = get_distance()
    return name, message, distance

if __name__ == "__main__":
    main()

def main():
   ##Tracebacks
   open("mars.jpg")
    
   ##Try y Except de los bloques
   # try:
   #     open('config.txt')
   # except FileNotFoundError:
   #     print("Couldn't find the config.txt file!")
   # except IsADirectoryError:
   #     print("Found config.txt but it is a directory, couldn't read it")
   # except (BlockingIOError, TimeoutError):
   #     print("Filesystem under heavy load, can't complete reading configuration file")
   
   #try:
   #    open("mars.jpg")
   #except FileNotFoundError as err:
   #    print("got a problem trying to read the file:" err)

   #try:
   #    open("config.txt")
   #except OSError as err:
   #    if err.errno == 2:
   #        print("Couldn't find the config.txt file!")
   #    elif err.errno == 13:
   #        print("Found config.txt but couldn't read it")

##Generación de excepciones

def water_left(astronauts, water_left, days_left):
    for argument in [astronauts, water_left, days_left]:
        try:
            argument / 10
        except TypeError:
            raise TypeError(f"All arguments must be of type int, but received: '{argument}'")
    daily_usage = astronauts * 11
    total_usage = daily_usage * days_left
    total_water_left = water_left - total_usage
    if total_water_left < 0:
        raise RuntimeError(f"There is not enough water for {astronauts} astronauts after {days_left} days!")
    return f"Total water left after {days_left} days is: {total_water_left} liters"

if __name__ == '__main__':
    #main()
    #print(water_left(5,100,2))
    #try:
    #    print(water_left(5,100,2))
    #except RuntimeError as err:
        #alert_navigation_system(err)
    water_left("3", "200", None)
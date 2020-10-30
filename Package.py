# Carlos Perez
# Student ID: 000819792

# Package class with each package attribute
class Package:

    def __init__(self, package_id, address, city, zipcode, state, deadline, weight, status):
        self.package_id = package_id
        self.address = address
        self.deadline = deadline
        self.city = city
        self.zipcode = zipcode
        self.state = state
        self.weight = weight
        self.status = status
        self.package_departure_time = 0
        self.delivery_time = 0
        self.time = 0
        self.status_update = None

    # Informs the package has not been loaded onto the truck
    def not_loaded(self):
        return print('Package', self.package_id, 'to', self.address, 'has not been loaded')
    # Informs package has been loaded onto the truck

    def loaded(self):
        return print('Package', self.package_id,'to', self.address,'has been loaded')
    # Informs the package is out for delivery

    def en_route(self):
        return print('Package', self.package_id, ' en route to', self.address)
    # Prints the package information when delivered


    # Converts time into total minutes for easier manipulation. Raises exception when minutes go passed 60
    # and when hours go passed 23.
    # 0(1)
    def to_minutes(self, time):
        t = time.split(':')
        if int(t[1]) > 59 or int(t[0]) > 23 or int(t[0]) < 8:
            raise Exception(time,'is not valid. Please enter a valid time')
        minutes = (int(t[0]) * 60) + int(t[1])
        return minutes


    # Sets the package when delivered by printing the time
    # 0(1)
    def set_delivered(self):
        hr = int(self.delivery_time / 60)
        min = int(self.delivery_time % 60)
        self.time = str(hr) + ":" + str(min).zfill(2)
        self.status_update = 'DELIVERED @ ' + self.time


    #set the time it has been delivered and for later retrieval
    # 0(1)
    def set_timestamp(self, distance):
        self.delivery_time = round(3.33 * distance) + self.package_departure_time


    # Function that determines the status of each package based on time.
    # 0(1)
    def lookup(self, min):
        minutes = self.to_minutes(min)
        # if not minutes <= 780:
        #     raise Exception('Please re-enter time again')

        if (minutes < 480):
            self.not_loaded()

        elif (minutes >= 480 and minutes < self.package_departure_time):
            self.loaded()

        elif minutes >= self.package_departure_time and minutes < self.delivery_time:
            self.en_route()

        elif minutes >= self.delivery_time:
            print('PACKAGE:',self.package_id, self.address, self.deadline, self.city, self.zipcode, self.state, self.weight,
                  self.status,
                  '--->', self.status_update)









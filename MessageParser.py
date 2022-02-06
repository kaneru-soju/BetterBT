from datetime import datetime


def parse_message(text_message):
    message = text_message.split(",")
    for i in range(0, len(message)):
        message[i] = message[i].lstrip()
    bus_route = message[0]
    location = message[1]
    stop_code = message[2]
    requested_time = message[3]
    if len(requested_time) == 4:
        requested_time = "0" + requested_time

    print(f"Bus Route is: {bus_route}, Location: {location}, Stop Code: {stop_code}, Requested Time: {requested_time}, "
          f"Current Time: {datetime.now().strftime('%X')}")

    query_time = int(requested_time[3:5]) - 10
    underflow = False

    if query_time < 0:
        underflow = True
        query_time = query_time + 60

    if underflow:
        query_time = str(int(requested_time[0:2]) - 1) + ":" + str(query_time)

    else:
        query_time = requested_time[0:2] + ":" + str(query_time)

    if len(query_time) == 4:
        query_time = "0" + query_time + ":00"

    return bus_route, location, stop_code, query_time


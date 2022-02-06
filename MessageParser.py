from datetime import datetime


def parse_message(text_message):
    message = text_message.split(",")
    for i in range(0, len(message)):
        message[i] = message[i].lstrip()

    bus_route, location, stop_code, requested_time = None, None, None, None

    length = len(message)
    if length == 2:
        # 1114, 21:33
        if len(message[0]) == 4:
            stop_code = message[0]
        # Torgersen Hall, 21:33
        elif len(message[0]) > 4:
            location = message[0]
        requested_time = message[1]
    elif length == 3:
        if len(message[0]) == 3:
            bus_route = message[0]
            # TOM, 1114, 21:33
            if len(message[1]) == 4:
                stop_code = message[1]
            # TOM, Torgersen Hall, 21:33
            elif len(message[1]) > 4:
                location = message[1]
            requested_time = message[2]
        # Torgersen Hall, 1114, 21:33
        elif len(message[0]) > 3:
            location = message[0]
            stop_code = message[1]
            requested_time = message[2]
    # TOM, Torgersen Hall, 1114, 21:33
    else:
        bus_route, location, stop_code, requested_time = message[0], message[1], message[2], message[3]

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


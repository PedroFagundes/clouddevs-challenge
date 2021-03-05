def humanize_time(time_in_seconds):
    '''
    Function that humanizes a given time amount in seconds
    e.g. Given 90 as an input, it outputs "1 minute 30 seconds"
    '''

    time_names = ["second", "minute", "hour", "day", "week", "month"]
    time_boundaries = [1, 60, 3600, 3600*24, 3600*24*7, 3660*24*30]
    time_pieces = []
    humanized_time = []

    for boundary in time_boundaries[::-1]:
        time_piece = int(time_in_seconds / boundary)
        time_pieces.append(int(time_in_seconds / boundary))
        time_in_seconds -= time_pieces[-1] * boundary

    for i, name in enumerate(time_names[::-1]):
        if time_pieces[i] > 0:
            humanized_time.append(
                f'{time_pieces[i]} {name}{"s" if time_pieces[i] > 1 else ""}')

    return " ".join(humanized_time)

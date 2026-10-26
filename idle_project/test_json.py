def find_all_substrings(string, substring):
    indices = []
    i = 0
    while i < len(string):
        j = string.find(substring, i)
        if j == -1:
            break
        indices.append(j)
        i = j + len(substring)
    return indices


def reformat(data_core):
    data = str(data_core)
    data = data.replace("'", '"')
    commas = find_all_substrings(data, ",")
    square = [0, 0]
    squiggly = [0, 0]
    new_data = [data]
    sessions = find_all_substrings(data, ' "Sessions"')
    charts_cardio = find_all_substrings(data, ' "Charts"')
    catalogues = find_all_substrings(data, ' "Catalogue"')
    gym_rat = 0
    session = sessions[gym_rat]
    chart_cardio = charts_cardio[gym_rat]
    catalogue = catalogues[gym_rat]
    charts_goals_count = 0
    first_indent_count = 0
    k = 1
    for index, character in enumerate(data):
        if first_indent_count == 5:
            gym_rat += 1
            session = sessions[gym_rat]
            chart_cardio = charts_cardio[gym_rat]
            catalogue = catalogues[gym_rat]
            first_indent_count = 0
        if character == "[":
            square[0] += 1
        elif character == "]":
            square[1] += 1
        elif character == "{":
            squiggly[0] += 1
        elif character == "}":
            squiggly[1] += 1
        if index in commas:
            # print(f"data is {new_data[len(new_data) - 1]}")
            # print(f"square is {square} and squiggly is {squiggly} and k is {k} when index is {index} and session is {session} and charts_cardio is {chart_cardio} and catalogue is {catalogue}")
            if square[0] == square[1] + 1 and squiggly[0] == squiggly[1] + 1:
                temp = [",".join(new_data[len(new_data) - 1].split(",")[:k]),
                        ",".join(new_data[len(new_data) - 1].split(",")[k:])]
                new_data[len(new_data) - 1] = temp[0]
                new_data.append(temp[1])
                new_data.insert(len(new_data) - 1, ",\n         ")
                k = 1
                charts_goals_count = 0
                # print(new_data)
                # print("scenario 1")
            elif square[0] == square[1] + 1 and squiggly[0] == squiggly[1] + 2:
                temp = [",".join(new_data[len(new_data) - 1].split(",")[:k]),
                        ",".join(new_data[len(new_data) - 1].split(",")[k:])]
                new_data[len(new_data) - 1] = temp[0]
                new_data.append(temp[1])
                new_data.insert(len(new_data) - 1, ",\n          ")
                k = 1
                charts_goals_count = 0
                first_indent_count += 1
                # print(new_data)
                # print("scenario 2")
            elif square[0] == square[1] + 2 and session < index < chart_cardio and index < catalogue:
                temp = [",".join(new_data[len(new_data) - 1].split(",")[:k]),
                        ",".join(new_data[len(new_data) - 1].split(",")[k:])]
                new_data[len(new_data) - 1] = temp[0]
                new_data.append(temp[1])
                if squiggly[0] == squiggly[1] + 3:
                    new_data.insert(len(new_data) - 1, ",\n                        ")
                elif squiggly[0] == squiggly[1] + 2:
                    new_data.insert(len(new_data) - 1, ",\n                       ")
                else:
                    new_data.insert(len(new_data) - 1, ",\n                                      ")
                k = 1
                # print(new_data)
                # print("scenario 3")
            elif square[0] == square[1] + 3 and squiggly[0] == squiggly[
                1] + 3 and index > session and chart_cardio < index < catalogue:
                temp = [",".join(new_data[len(new_data) - 1].split(",")[:k]),
                        ",".join(new_data[len(new_data) - 1].split(",")[k:])]
                new_data[len(new_data) - 1] = temp[0]
                new_data.append(temp[1])
                new_data.insert(len(new_data) - 1, ",\n                                              " + " " * len(
                    data_core["Logs"][gym_rat]["Charts"][charts_goals_count]["Goal"]))
                k = 1
                charts_goals_count += 1
                # print(new_data)
                # print("scenario 4")
            elif square[0] == square[1] + 2 and squiggly[0] == squiggly[
                1] + 2 and index > session and chart_cardio < index < catalogue:
                temp = [",".join(new_data[len(new_data) - 1].split(",")[:k]),
                        ",".join(new_data[len(new_data) - 1].split(",")[k:])]
                new_data[len(new_data) - 1] = temp[0]
                new_data.append(temp[1])
                new_data.insert(len(new_data) - 1, ",\n                     ")
                k = 1
                # print(new_data)
                # print("scenario 5")
            elif square[0] == square[1] + 2 and squiggly[0] == squiggly[
                1] + 2 and index > session and index > chart_cardio and index > catalogue:
                temp = [",".join(new_data[len(new_data) - 1].split(",")[:k]),
                        ",".join(new_data[len(new_data) - 1].split(",")[k:])]
                new_data[len(new_data) - 1] = temp[0]
                new_data.append(temp[1])
                new_data.insert(len(new_data) - 1, ",\n                        ")
                k = 1
                # print(new_data)
                # print("scenario 6")
            else:
                k += 1
                # print("scenario 7")
            # print("\n")

    new_data[len(new_data) - 1] = new_data[len(new_data) - 1][:-2] + "\n          " + new_data[len(new_data) - 1][
                                                                                      -2:-1] + "\n" + new_data[
                                                                                                          len(new_data) - 1][
                                                                                                      -1:]
    result = "".join(new_data)
    return result

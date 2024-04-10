
inner_counter = 0
external_counter = 0

while external_counter < 6:
    while inner_counter < 6:
        print(external_counter, inner_counter)
        inner_counter += 1
        if inner_counter >= 3:
            break

    external_counter += 1
    inner_counter = 0


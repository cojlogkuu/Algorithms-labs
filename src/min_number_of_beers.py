def made_list_of_preferences(preferences_str):
    pref_list = []
    for employees_beers in preferences_str.split():
        beers_pref_set = set()
        for i in range(len(employees_beers)):
            if employees_beers[i] == 'Y':
                beers_pref_set.add(i)
        pref_list.append(beers_pref_set)
    return pref_list


def remove_extra_beer(preferences_list, used_beers):
    for beer in used_beers:
        updated_used_beers = used_beers.copy()
        updated_used_beers.remove(beer)
        if all(bool(employee_pref.intersection(updated_used_beers)) for employee_pref in preferences_list):
            return updated_used_beers
    return used_beers


def get_min_number_of_beers(n, b, preferences):
    preferences_list = made_list_of_preferences(preferences)
    start_preferences_list = preferences_list.copy()
    used_beers = set()
    used_beers.update(min(preferences_list, key=len))
    preferences_list.remove(used_beers)

    for employee_pref in preferences_list:
        if not employee_pref.intersection(used_beers):
            used_beers.add(employee_pref.copy().pop())
    return len(remove_extra_beer(start_preferences_list, used_beers))

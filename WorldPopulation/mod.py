def get_popu(country_dict):
    population_dict = {
        '2022':float(country_dict['2022 Population']),
        '2020':float(country_dict['2020 Population']),
        '2015':float(country_dict['2015 Population']),
        '2010':float(country_dict['2010 Population']),
        '2000':float(country_dict['2000 Population']),
        '1990':float(country_dict['1990 Population']),
        '1980':float(country_dict['1980 Population']),
        '1970':float(country_dict['1970 Population'])
    }
    labels = population_dict.keys()
    values = population_dict.values()
    return labels, values

def popu_by_country(data, country):
    result = list(filter(lambda item: item['Country'] == country, data))
    return result


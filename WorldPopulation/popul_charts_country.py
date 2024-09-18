import mod
import read_csv
import charts


def run():
    data = read_csv.read_csv('world_population.csv')
    country = input('Type Country => ')
    result = mod.popu_by_country(data, country)

    if len(result)>0:
        country = result[0]
        labels, values = mod.get_popu(country)
        charts.generate_bar_chart(country['Country'], labels, values)
        print(country['Continent'])
    else:
        print('Country not found')


if __name__ == '__main__':
    run()
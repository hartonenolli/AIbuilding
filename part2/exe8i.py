def main():
    countries = ['Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden']
    populations = [5615000, 5439000, 324000, 5080000, 9609000]
    fishers = [1891, 2652, 3800, 11611, 1757]

    total_fishers = sum(fishers)
    total_population = sum(populations)

    # write your solution here
    list_of_proportions = [fisher/total_fishers*100 for fisher in fishers]
    

    for country, list_of_proportions in zip(countries, list_of_proportions):
        print("%s %.2f%%" % (country, list_of_proportions)) # modify this to print correct results

main()

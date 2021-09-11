data_weather = {}
data_weather_list = []
with open ('data_structure/nyc_weather.csv','r') as f:
    for line in f:
        tokens = line.split(',')
        temp = (tokens[1][:-1])
        if temp == 'temperature(F)':
            pass
        else:
            data_weather[tokens[0]] = float(temp)
            data_weather_list.append(float(temp))

    print(data_weather)
    sum = 0
    n = 1
    max_temp = max (data_weather_list)
    for k,v in data_weather.items():
       print(v)
       if v==max_temp:
           max_temp_jan = k
       sum = v + sum
       n += 1
    print(f'avg = {sum/(n-1)}') 
    #print(sum,n-1)   
    print(max_temp_jan, max_temp)

    print(data_weather['Jan 1'])

    
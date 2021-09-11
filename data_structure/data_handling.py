data_weather = {}
data_weather_list = []
with open ('data_structure/nyc_weather.csv','r') as f:
    for line in f:
        tokens = line.split(',')
        temp = (tokens[1])
        if temp == 'temperature(F)\n':
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
token_all = []
with open ('data_structure/poem.txt','r') as f:
    for line in f:
        tokens = line.split()
        token_all+=tokens
    #print(token_all)
    dict_cnt = {}
    for element in token_all:
        if element not in dict_cnt:
            dict_cnt[element] = 1
        else:
            dict_cnt[element] = dict_cnt[element] + 1
    print(dict_cnt)
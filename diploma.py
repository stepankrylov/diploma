def token():
    from urllib.parse import urlencode
    APP_ID = 7056106
    AUTH_URL = 'https://oauth.vk.com/authorize'
    AUTH_DATA = {'client_id': APP_ID, 'display': 'page', 'scope': 'friends', 'response_type': 'token'}
    print('?'.join((AUTH_URL, urlencode(AUTH_DATA))))

def mutual_friend():
    import requests
    TOKEN = '73eaea320bdc0d3299faa475c196cfea1c4df9da4c6d291633f9fe8f83c08c4de2a3abf89fbc3ed8a44e1'
    params = {
        'access_token': TOKEN,
        'order': 'hints',
        'v': '5.52'
    }

    friends_get_params = params.copy()
    friends_get_params['user_id'] = 171691064
    #friends_get_params['user_id'] = input('Введите id пользователя: ')

    response = requests.get('https://api.vk.com/method/users.get', params=friends_get_params)
    print('Пользователь: ', response.json()['response'][0]['first_name'],  response.json()['response'][0]['last_name'])

    response = requests.get('https://api.vk.com/method/friends.get', params=friends_get_params)
    user_friends = response.json()['response']['items']
    #print('Друзья пользователя: ', user_friends)

    response = requests.get('https://api.vk.com/method/groups.get', params=friends_get_params)
    user_group_set = response.json()['response']['items']
    print('Группы пользователя: ', user_group_set)

    import time
    pause = 0.34
    for x in user_group_set:
        friends_get_params['group_id'] = x
        friends_get_params['extended'] = 1
        friends_get_params['fields'] = "members_count"
        response = requests.get('https://api.vk.com/method/groups.getById', params=friends_get_params)
        print('Группа: ', response.json())
        #print(friends_get_params)
        #print('Группа: ', response.json()['response'][0]['name'], response.json()['response'][0]['id'])
        time.sleep(pause)

    # import time
    # pause = 0.34
    # group_list = []
    # for i in user_friends:
    #     friends_get_params['user_id'] = i
    #     response = requests.get('https://api.vk.com/method/users.get', params=friends_get_params)
    #     print('Пользователь: ', response.json()['response'][0].get('first_name'), response.json()['response'][0].get('last_name'), response.json()['response'][0].get('deactivated'))
    #     try:
    #         response = requests.get('https://api.vk.com/method/groups.get', params=friends_get_params)
    #         #print('Группы: ', response.json()['response']['items'])
    #         group_list += response.json()['response']['items']
    #     except KeyError:
    #         pass
    #     time.sleep(pause)
    # group_set = set(group_list)
    # #print('Группы друзей пользователя: ', group_set)

    # diff_group = user_group_set.difference(group_set)
    # for x in diff_group:
    #     friends_get_params['group_id'] = x
    #     response = requests.get('https://api.vk.com/method/groups.getByld', params=friends_get_params)
    #     print('Группа: ', response.json())

    

def command():
    command = input('Внимание! Для работы кода необходим TOKEN.\nЕсли вы внесли TOKEN в код нажмите "y",\nиначе нажмите "n",\nполучте TOKEN,\nвнесите его в код \nи, заново запустив программу, нажмите "y"\nВаша команда: ')
    if command == 'n':
        token()
    elif command == 'y':
        mutual_friend()
    else:
        print('Ошибка ввода. Введенной вами команды не существует. Запустите программу заново.')

if __name__ == "__main__":
    command()
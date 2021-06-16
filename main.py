import apps
pick_app = ['calculator','phone','messages','facebook','youtube','whatsapp']


if __name__ == '__main__':
    while True:
        print('Choose a app then')
        for index, item in enumerate(pick_app):
            print(f'{index+1}.{item}')
        user_awnser = input(f'Pick a number')
        if user_awnser == '1':
            apps.calculator()
        elif user_awnser == '2':
            apps.phone()
        elif user_awnser == '3':
            apps.messages()
        elif user_awnser == '4':
            apps.facebook()
        elif user_awnser == '5':
            apps.youtube()
        elif user_awnser == '6':
            apps.whatsapp()
        apps.display_total_time()

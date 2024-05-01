import requests

url = "https://discord.com/api/v10/applications/1232761917626388722/commands"

json =  {
        'name': 'title',
        'type': 1,
        'description': 'Gives the title',
        "options":  [
                {
                        "name": "title",
                        "description": "The title to give.",
                        "type": 3,
                        "required": True,
                        'choices': [
                                {
                                        'name': "duke",
                                        'value': "duke"
                                },
                                {
                                        'name': "architect",
                                        'value': "architect"
                                },
                                {
                                        'name': "justice",
                                        'value': "justice"
                                },
                                {
                                        'name': "scientist",
                                        'value': "scientist"
                                }
                        ]
                },
                {
                        'name': 'kingdom',
                        "description": "hk for home kingdom, lk for lost kingdom",
                        'type': 3,
                        'required': True,
                        'choices': [
                                {
                                        'name': "Home Kingdom",
                                        'value': "hk"
                                },
                                {
                                        'name': "Lost Kingdom",
                                        'value': "lk"
                                }

                        ]
                },
                {
                        'name': 'x-coordinate',
                        'description': 'The x coordinate of the location.',
                        'type': 4,
                        'required': True
                },
                {
                        'name': 'y-coordinate',
                        'description': 'The y coordinate of the location.',
                        'type': 4,
                        'required': True
                }
        ]
}


headers = {
    "Authorization": "Bot MTIzMjc2MTkxNzYyNjM4ODcyMg.G7BEBt.k4fjN3--Ho04RI7h-SRHVhplnego3tpb6OFFTk"
}

r = requests.delete(url, headers=headers, json=json)

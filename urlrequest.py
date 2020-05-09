import requests as req

response = req.get('https://github.com/apps/devnet-app/blah')
print(response.status_code)
if response.status_code == 200:
    print('Success!')
elif response.status_code == 404:
    print('Not Found.')
    
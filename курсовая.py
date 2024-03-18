import os
import requests
import json
import configparser

class VKAPI:
    def __init__(self, token):
        self.token = token

    def get_photos(self, user_id):
        url = f'https://api.vk.com/method/photos.get?owner_id={user_id}&album_id=profile&rev=1&extended=1&v=5.131&access_token={self.token}'
        response = requests.get(url)
        photos = response.json()['response']['items']
        return photos

class YandexAPI:
    def __init__(self, token):
        self.token = token

    def save_photo(self, file_url, file_name):
        headers = {'Authorization': f'OAuth {self.token}'}
        params = {'path': f'/vk_photos/{file_name}', 'url': file_url}
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        response = requests.post(url, headers=headers, params=params)
        return response

def main():
    config = configparser.ConfigParser()
    config.read('config.ini')
    
    vk_token = config.get('Tokens', 'VK')
    yandex_token = config.get('Tokens', 'Yandex')
    
    user_id = input("Введите id пользователя VK: ")
    
    vk_api = VKAPI(vk_token)
    yandex_api = YandexAPI(yandex_token)
    
    photos = vk_api.get_photos(user_id)
    
    if not os.path.exists('vk_photos'):
        os.makedirs('vk_photos')
    
    photos_info = []
    
    for i, photo in enumerate(photos[:5]):
        file_url = photo['sizes'][-1]['url']
        likes = photo.get('likes', {}).get('count', 0)
        date = photo['date']
        file_name = f'{likes}_{date}.jpg'
        
        if likes == 0:
            file_name = f'no_likes_{date}.jpg'
        
        response = yandex_api.save_photo(file_url, file_name)
        
        photos_info.append({
            "file_name": file_name,
            "size": photo['sizes'][-1]['type']
        })
        
        print(f"Фото {i + 1} загружено на Яндекс.Диск")
    
    with open('photos_info.json', 'w') as f:
        json.dump(photos_info, f, indent=4)

if __name__ == "__main__":
    main()
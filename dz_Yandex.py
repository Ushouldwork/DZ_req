import requests
import os
class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = {"Authorization": "OAuth " + self.token}
        params = {'path': file_path}
        response = requests.get(url, params=params, headers=headers).json()
        url = response.get("href", "")
        with open(file_path, 'rb') as f:
            response = requests.put(url, files={"file": f}, headers=headers, params=params)
            return(response.status_code)



if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    
    path_to_file = 
    token = 
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
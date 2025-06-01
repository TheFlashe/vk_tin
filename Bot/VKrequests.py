import vk_api
from config import VK_group_token, VK_service_token


class Gets:

    def __init__(self, VK_service_token):
        self.vk = vk_api.VkApi(token=VK_service_token).get_api()


    def check_token(self) -> bool:
        """Проверка валидности токена"""
        try:
            user_info = self.vk.users.get(user_id=1)
            if user_info[0]['last_name'] == 'Durov':
                return True
        except vk_api.exceptions.ApiError as e:
            return False

    def get_3top_photos(self, user_id) -> list:
        """Выдает ссылки на топ три фото пользователя по количеству лайков"""
        photos = []
        # response = self.vk.photos.getUserPhotos(user_id=user_id, extended=True)
        try:
            response = self.vk.photos.get(owner_id=user_id, album_id='profile', extended=True)
        except Exception as e:
            return False

        if response['count']:
            for item in response['items']:
                likes = item['likes']['count']
                href = item['orig_photo']['url']
                photos.append((likes, href))
        photos.sort(key=lambda x: x[0], reverse=True)
        return photos[0:3]



if __name__ == '__main__':
    user_id = 252861379
    user_id1 = 231350322
    gets = Gets(VK_service_token)
    if gets.check_token():
        gets.get_3top_photos(user_id)
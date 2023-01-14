from api import PetFriends
from settings import valid_email, valid_password
import os

from requests_toolbelt.multipart.encoder import MultipartEncoder

pf = PetFriends()


def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result

def test_get_api_key_for_invalid_user(email=valid_email+'ffhfghdhdg', password=valid_password+'ryjtjrtn'):
    status, result = pf.get_api_key(email, password)
    assert status == 403
    assert 'key' not in result

def test_get_all_pets_with_valid_key(filter=''):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    assert  len(result['pets']) > 0

def test_get_all_pets_with_invalid_key(filter=''):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets_wrong(auth_key, filter)
    assert status == 403


def test_add_new_pet_valid_data(name="Alf", animal_type="пришелец", age="20", pet_photo='images/ttt.jpg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name

def test_add_new_pet_with_invalid_photo(name='Барбоскин', animal_type='двортерьер',
                                    age='4', pet_photo='images/ttt.txt'):
   pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
   _, auth_key = pf.get_api_key(valid_email, valid_password)
   status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
   assert status == 200

def test_add_new_pet_with_invalid_data(name='Барбоскин', animal_type='двортерьер',
                                    age='-10', pet_photo='images/ttt.jpg'):
   pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
   _, auth_key = pf.get_api_key(valid_email, valid_password)
   status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
   assert status == 200

def test_delete_pet_invalid_id(pet_id = "fff"):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.delete_pet(auth_key, pet_id)
    assert status == 200

def test_delete_pet_valid_id(pet_id = "4c61f337-d53e-48de-bc8b-f3dcaf18216d"):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.delete_pet(auth_key, pet_id)
    assert status == 200

def test_update_no_exist_pet_id(pet_id = "4c61f337-d53e-48de-bc8b-f3dcaf18216d", name='Яша', animal_type='двортерьер',
                                    age='10'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.update_pet_info(auth_key, pet_id, name, animal_type, age)
    assert status == 400

def test_update_valid_pet_id(pet_id = "0f1f47e8-f8ca-4503-a2bd-a9cb07d04aff", name='Яша', animal_type='марсианин',
                                    age='10'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.update_pet_info(auth_key, pet_id, name, animal_type, age)
    assert status == 200















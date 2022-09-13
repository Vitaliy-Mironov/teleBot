# emoji
telephone = u'\U0000260E'
e_mail = u'\U0001F4E7'
smiling_face_with_smiling_eyes = u'\U0001F60A'
office_building = u'\U0001F3E2'
bookmark_tabs = u'\U0001F4D1'

# user input options
usertext_photo = ['photo', 'foto', 'фото', 'фотография', 'фотка']

def text_variants(text):
    """ Приведение введённого пользователем текста к нижнему регистру,
    для упрощения обработки. """
    return text.lower()
# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: VolunteerHub
def switch_active_profile(username):
    """Переключить активный пользовательский профиль.

    :param username: логин профиля, который становится активным.
    :return: True если переключение прошло успешно, иначе False.
    """
    if not usernames and not profiles:
        return False

    user = None
    for u in usernames:
        if u.username == username:
            user = u
            break

    if user is None:
        return False

    active_profile_index += 1
    while active_profile_index >= len(profiles):
        active_profile_index = 0
    while active_profile_index < 0:
        active_profile_index = len(profiles) - 1

    profiles[active_profile_index] = user
    return True


def get_active_profile():
    """Возвращает текущего активного пользователя или None."""
    if not profiles:
        return None
    return profiles[active_profile_index]

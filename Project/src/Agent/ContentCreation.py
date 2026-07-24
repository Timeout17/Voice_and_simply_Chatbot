
from Project.src.Enums.Role import UserEnum


class ContentCreatonClass():
    @staticmethod
    def create_message(history: list[str], message: str):
        return  [
                {
                "role": UserEnum.SYSTEM.value,
                    "content": """
                    Te egy segítőkész hangsegéd vagy.
                    A felhasználói üzenet beszédátírásból származik.
                    Közvetlenül válaszolj a felhasználó tényleges kérésére.
                    Ne foglalkozz azzal, hogy hallod-e a hangot.
                    Ne magyarázd el a korlátaidat, hacsak nem kérdeznek rá.
                    És ami nagyon fontos, MAGYAR VAGY
"""
                }
                ] + history +[
                {
                    "role": UserEnum.USER.value,
                    "content": message
                }
            ]     

from Project.src.Enums.Role import UserEnum


class ContentCreatonClass():
    @staticmethod
    def create_message(history: list[str], message: str):
        return  [
                {
                "role": UserEnum.SYSTEM.value,
                    "content": "Magyarul beszélsz. Kedves és segítő kész vagy"
                }
                ] + history +[
                {
                    "role": UserEnum.USER.value,
                    "content": message
                }
            ]     
from sqlite3 import Connection
from src.models.sqlite.interfaces.user_repository import UserRepositoryInterface

class UserRepository(UserRepositoryInterface):
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn

    def registry_user(self, username: str, password: str) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            'INSERT INTO users (username, password) VALUES (?, ?)', (username, password)
        )

        self.__conn.commit()

    def get_user_by_id(self, user_id: int) -> tuple[int, str, str]:
        cursor = self.__conn.cursor()

        cursor.execute(
            """ 
            SELECT id, username, password
            FROM users
            WHERE id = ?
            """, (user_id,)

        )

        user = cursor.fetchone()
        return user
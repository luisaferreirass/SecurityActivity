from sqlite3 import Connection
from src.models.sqlite.interfaces.orders_repository import OrdersRepositoryInterface

class OrdersRepository(OrdersRepositoryInterface):
    def __init__(self, conn: Connection):
        self.__conn = conn

    def registry_order(self, user_id: int, description: str, date: str) -> None:
        cursor = self.__conn.cursor()

        cursor.execute(
            """
            INSERT INTO orders (user_id, description, date) VALUES (?, ?, ?)
            """, (user_id, description, date)
            )
        
        self.__conn.commit()


    def list_orders(self, user_id: int) -> list[tuple]:
        cursor = self.__conn.cursor()

        cursor.execute(
            """
            SELECT description, date
            FROM orders
            WHERE user_id = ?
            """, (user_id,)
        )

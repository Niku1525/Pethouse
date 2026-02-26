import psycopg2
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.user_model import User
from fastapi.encoders import jsonable_encoder


class UserController:

    def create_user(self, user: User):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                """
                INSERT INTO users (name, last_name, email, password)
                VALUES (%s, %s, %s, %s)
                RETURNING id
                """,
                (user.name, user.last_name, user.email, user.password)
            )

            new_id = cursor.fetchone()[0]
            conn.commit()

            return {
                "id": new_id,
                "name": user.name,
                "last_name": user.last_name,
                "email": user.email,
                "password": user.password
            }

        except psycopg2.Error as err:
            conn.rollback()
            print(err)
            raise HTTPException(status_code=500, detail="Error creating user")

        finally:
            conn.close()


    def get_user(self, user_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                "SELECT id, name, last_name, email, password FROM users WHERE id = %s",
                (user_id,)
            )

            result = cursor.fetchone()

            if not result:
                raise HTTPException(status_code=404, detail="User not found")

            return {
                "id": result[0],
                "name": result[1],
                "last_name": result[2],
                "email": result[3],
                "password": result[4]
            }

        except psycopg2.Error as err:
            print(err)
            raise HTTPException(status_code=500, detail="Database error")

        finally:
            conn.close()


    def get_users(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                "SELECT id, name, last_name, email, password FROM users"
            )

            result = cursor.fetchall()

            if not result:
                raise HTTPException(status_code=404, detail="No users found")

            users = []
            for row in result:
                users.append({
                    "id": row[0],
                    "name": row[1],
                    "last_name": row[2],
                    "email": row[3],
                    "password": row[4]
                })

            return users

        except psycopg2.Error as err:
            print(err)
            raise HTTPException(status_code=500, detail="Database error")

        finally:
            conn.close()


    def update_user(self, user_id: int, user: User):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                """
                UPDATE users
                SET name = %s,
                    last_name = %s,
                    email = %s,
                    password = %s
                WHERE id = %s
                """,
                (user.name, user.last_name, user.email, user.password, user_id)
            )

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="User not found")

            conn.commit()

            return {"message": "User updated successfully"}

        except psycopg2.Error as err:
            conn.rollback()
            print(err)
            raise HTTPException(status_code=500, detail="Error updating user")

        finally:
            conn.close()


    def delete_user(self, user_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                "DELETE FROM users WHERE id = %s",
                (user_id,)
            )

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="User not found")

            conn.commit()

            return {"message": "User deleted successfully"}

        except psycopg2.Error as err:
            conn.rollback()
            print(err)
            raise HTTPException(status_code=500, detail="Error deleting user")

        finally:
            conn.close()
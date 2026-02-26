from config.db_config import get_db_connection
from models.pet_model import Pet

class PetController:

    def create_pet(self, pet: Pet):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                """
                INSERT INTO pets (user_id, name, species, age, gender, description, image_url, status)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                RETURNING id
                """,
                (
                    pet.user_id,
                    pet.name,
                    pet.species,
                    pet.age,
                    pet.gender,
                    pet.description,
                    pet.image_url,
                    pet.status
                )
            )

            new_id = cursor.fetchone()[0]
            conn.commit()

            return {"message": "Pet created", "pet_id": new_id}

        except Exception as e:
            return {"error": str(e)}

        finally:
            cursor.close()
            conn.close()


    def get_pets(self):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM pets")
        pets = cursor.fetchall()

        cursor.close()
        conn.close()

        return pets


    def get_pet(self, pet_id: int):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM pets WHERE id = %s", (pet_id,))
        pet = cursor.fetchone()

        cursor.close()
        conn.close()

        return pet


    def delete_pet(self, pet_id: int):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM pets WHERE id = %s", (pet_id,))
        conn.commit()

        cursor.close()
        conn.close()

        return {"message": "Pet deleted"}
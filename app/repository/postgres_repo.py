
from app.repository.task_repository import TaskRepository
from app.models.task_model import Task
import psycopg
from dotenv import load_dotenv
import os

load_dotenv()



class PostgresRepository(TaskRepository):

    def connection(self):
           return psycopg.connect(host=os.getenv("DB_HOST"),
                               dbname=os.getenv("DB_NAME"),
                               user=os.getenv("DB_USER"),
                               password=os.getenv("DB_PASSWORD"),
                               ) 
   
    def add(self, title):
        task = Task(id=0, title=title, status="TODO")
        try:
            with self.connection() as conn:
                with conn.cursor() as cur:
                        cur.execute(
                            """
                            INSERT INTO tasks(title)
                            VALUES (%s)
                            """,
                            (task.title,)
                        )
                conn.commit()
        except Exception as e:
               print(f"Error: {e}")
        
    def list(self, status):
        
        query = """
                    SELECT id, title, status FROM tasks
                """
        param = []
        if status is not None:
            query += """ WHERE status=%s """
            param = [status.value]
        
        try:
            with self.connection() as conn:
                with conn.cursor() as cur:
                        cur.execute(
                            query,param
                        )
                        return cur.fetchall()
        except Exception as e:
               print(f"Error: {e}")

    def mark(self, id,status):
        try:
            with self.connection() as conn:
                with conn.cursor() as cur:
                        cur.execute(
                            """
                                UPDATE tasks 
                                SET status =%s
                                WHERE id=%s
                            """,
                            (status.value, id)
                        )
                        conn.commit()
        except Exception as e:
               print(f"Error: {e}")

    def update(self, id, title):
        try:
            with self.connection() as conn:
                with conn.cursor() as cur:
                        cur.execute(
                            """
                                UPDATE tasks 
                                SET title = %s
                                WHERE id=%s
                            """,
                            (title,id)
                        )
                        conn.commit()
        except Exception as e:
               print(f"Error: {e}")

    def delete(self, id):
        try:
        
            with self.connection() as conn:
                with conn.cursor() as curr:
                        curr.execute(
                                """
                                DELETE FROM tasks WHERE id=%s
                                """,
                                (id,)
                        )
        except Exception as e:
               print(f"Error: {e}")
    
    
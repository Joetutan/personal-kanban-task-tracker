
from app.models.task_model import Task
from app.models.task_model import TaskStatus
import psycopg
from dotenv import load_dotenv
import os

load_dotenv()



class TasksRepository:

    def connection(self):
           return psycopg.connect(host=os.getenv("DB_HOST"),
                               dbname=os.getenv("DB_NAME"),
                               user=os.getenv("DB_USER"),
                               password=os.getenv("DB_PASSWORD"),
                               ) 
   
    def add(self, task: Task):
        try:
            with self.connection() as conn:
                with conn.cursor() as cur:
                        cur.execute(
                            """
                            INSERT INTO tasks(title)
                            VALUES (%s)
                            RETURNING id
                            """,
                            (task.title,)
                        )
                        task.id = cur.fetchone()[0]
                conn.commit()
                return task
        except Exception as e:
               print(f"Error: {e}")
        
    def list(self, status: TaskStatus | None) -> list[Task]:

        query = """
                    SELECT id, title, status FROM tasks
                """
        param = []
        if status is not None:
            query += """ WHERE status=%s """
            param = [status]
        
        try:
            with self.connection() as conn:
                with conn.cursor() as cur:
                        cur.execute(
                            query,param
                        )
                        return cur.fetchall()
        except Exception as e:
               print(f"Error: {e}")

    def mark(self, task:Task) -> Task:
        try:
            with self.connection() as conn:
                with conn.cursor() as cur:
                        cur.execute(
                            """
                                UPDATE tasks 
                                SET status =%s
                                WHERE id=%s
                                RETURNING id, title, status
                            """,
                            (task.status, task.id)
                        )
                        task.id, task.title, task.status = cur.fetchone()
                        conn.commit()
                        return task
        except Exception as e:
               return f"Error: {e}"

    def update(self, task:Task) -> Task:
        try:
            with self.connection() as conn:
                with conn.cursor() as cur:
                        cur.execute(
                            """
                                UPDATE tasks 
                                SET title = %s
                                WHERE id=%s
                                RETURNING id, title, status
                            """,
                            (task.title,task.id)
                        )
                        task.id, task.title, task.status = cur.fetchone()
                        conn.commit()
                        return task
        except Exception as e:
               print(f"Error: {e}")

    def delete(self, id:int) -> str:
        
        try:
            with self.connection() as conn:
                with conn.cursor() as curr:
                        curr.execute(
                                """
                                DELETE FROM tasks WHERE id=%s
                                """,
                                (id,)
                        )
                        return "Task deleted successfully"
        except Exception as e:
               return f"Error: {e}"
    
    def delete_tasks(self, status: TaskStatus) -> str:
         
        try:
            with self.connection() as conn:
                with conn.cursor() as curr:
                        curr.execute(
                                """
                                DELETE FROM tasks WHERE status=%s
                                """,
                                (status,)
                        )
                        return "Tasks deleted successfully"
        except Exception as e:
               return f"Error: {e}"
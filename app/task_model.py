from app.db import connect

def get_tasks(): 

    sql = 'SELECT * from tasks'

    conn = connect()
    cur = conn.cursor()

    cur.execute(sql)
    results = cur.fetchall()
    data = []

    for row in results:
        data.append({'id': row[0], 'name' : row[1], 'description' : row[2], 'done': row[3]})

    cur.close()
    conn.close()
    return data

def get_task(task_id): 

    sql = 'SELECT * from tasks WHERE id=%s'

    conn = connect()
    cur = conn.cursor()

    cur.execute(sql, (task_id,))
    results = cur.fetchone()

    if results is None:
        return None

    data = {'id': results[0], 'name': results[1], 'description': results[2], 'done': results[3]}

    cur.close()
    conn.close()

    return data
     
def add_task(name, description, done):

    sql = """
        INSERT INTO tasks (name, description, done) VALUES(%s, %s, %s)
        RETURNING id, name, description, done
    """

    conn = connect()
    cur = conn.cursor()

    cur.execute(sql, (name, description, done))
    result = cur.fetchone()

    if result is None:
        return None
    
    conn.commit()
    
    data = {'id': result[0], 'name': result[1], 'description': result[2], 'done': result[3]}

    cur.close()
    conn.close()

    return data

def update_task(task_id, name, description, done):
    
    sql = """
        UPDATE tasks
        SET name=%s, description=%s, done=%s 
        WHERE id=%s
    """

    conn = connect()
    cur = conn.cursor()

    cur.execute(sql, (name, description, done, task_id))
    
    conn.commit()
    cur.close()
    conn.close()

def delete_task(task_id):

    sql = """
        DELETE FROM tasks WHERE id=%s
    """

    conn = connect()
    cur = conn.cursor()

    cur.execute(sql, (task_id,))

    conn.commit()
    cur.close()
    conn.close()

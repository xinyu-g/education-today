from flask import Blueprint, jsonify, request
from flask import Flask, send_from_directory, jsonify, request
from . import db
# from flask_sqlalchemy import SQLAlchemy 




# mysql = MySQL()
# # MySQL configurations


main = Blueprint('main', __name__)

conn = db.connect()

@app.route("/task1", methods=['GET','POST'])
def task1():
    cur = conn.cursor()
    sql = """SELECT pr.PaperReferenceId, COUNT(T.PaperId)
                FROM (SELECT AuthorId, PaperId
                FROM authors as a JOIN paperauthoraffiliations as pa USING (AuthorId)
                WHERE a.AuthorId = {}) as T NATURAL JOIN paperreferences as pr
                GROUP BY pr.PaperReferenceId
                ORDER BY COUNT(T.PaperId) DESC"""
    author_id = 2146473740
    cur.execute(sql.format(author_id))
    tasks = []
    for id, cnt in cur.fetchall():
        tasks.append({
            'PaperId': id,
            'citedBy': author_id,
            'numOfTimeReferenced': cnt
        })

    return jsonify(tasks)


@app.route("/task2", methods=['GET','POST'])
def task2():
    cur = conn.cursor()
    return 'Done'
    

# api.add_resource(ApiHandler, '/flask/hello')


if __name__ == '__main__':
 
    app.run(debug = True)


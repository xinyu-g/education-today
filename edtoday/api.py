from flask import Blueprint, jsonify, request
from flask import Flask, send_from_directory, jsonify, request
from . import db
# from flask_sqlalchemy import SQLAlchemy 


# mysql = MySQL()
# # MySQL configurations


main = Blueprint('main', __name__)




@main.route("/task1", methods=['GET','POST'])
def task1():

    conn = db.connect()
    cur = conn.cursor()
    sql = """SELECT pr.PaperReferenceId, COUNT(T.PaperId)
                FROM (SELECT AuthorId, PaperId
                FROM authors as a JOIN paperauthoraffiliations as pa USING (AuthorId)
                WHERE a.AuthorId = {}) as T NATURAL JOIN paperreferences as pr
                GROUP BY pr.PaperReferenceId
                ORDER BY COUNT(T.PaperId) DESC"""
    # input = request.get_json()
    # author_id = input['authorId']
    author_id = request.get_json()
    cur.execute(sql.format(int(author_id)))
    tasks = []
    for id, cnt in cur.fetchall():
        tasks.append({
            'paperId': id,
            'citedBy': author_id,
            'numOfTimeReferenced': cnt
        })

    cur.close()
    return jsonify({'tasks': tasks})


@main.route("/task2", methods=['GET','POST'])
def task2():
    conn = db.connect()
    cur = conn.cursor()
    return 'Done'
    

# api.add_resource(ApiHandler, '/flask/hello')


if __name__ == '__main__':
 
    app.run(debug = True)


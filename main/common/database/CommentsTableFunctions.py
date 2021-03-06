import sqlite3
from sqlite3 import Error
#from . import *
from datetime import datetime

from common.database import PostsTableFunctions
from common.database import FriendsTableFunctions
from common.database import LikesTableFunctions
from common.database import  UsersTableFunctions
#from common.database import CommentsTableFunctions
from common.database import  TableCreationFunctions

# Insert Functions:

def insert_new_comment(values):
    """ inserts a new comment into the database
    :param values: 1.: post_id, 2.: author_user_name, 3.: comm_content,
    return: None
    """
    try:
        time = int(datetime.now().timestamp())
        author_id = UsersTableFunctions.get_user_id(values[1])
        conn = TableCreationFunctions.create_connection()
        c = conn.cursor()
        c.execute("""
            INSERT INTO comments (comm_post_id, comm_author_id, date_time, comm_content) 
            VALUES (?, ?, ?, ?);""", (values[0], author_id, time, values[2]))
        conn.commit()
        conn.close()
    except Error as e:
        print(e)
        conn.rollback()


# Delete Functions:

def delete_comment(values):
    """ deletes a given comment
    :param :param values: post_id, author_user_name, date_time, comm_content
    :return: None
    """
    try:
        comment_id = get_comment_id(values)
        conn = TableCreationFunctions.create_connection()
        cur = conn.cursor()
        cur.execute(f"DELETE FROM comments WHERE comment_id=?;", (comment_id, ))
        conn.commit()
        conn.close()
    except Error as e:
        print(e)
        conn.rollback()


def delete_all_comments_of_post(post_id):
    """ deletes all comments of a given post
    :param post_id
    :return: None
    """
    try:
        conn = TableCreationFunctions.create_connection()
        cur = conn.cursor()
        cur.execute(f"DELETE FROM comments WHERE comm_post_id=?;", (post_id,))
        conn.commit()
        conn.close()
    except Error as e:
        print(e)
        conn.rollback()


def delete_all_comments_of_user(user_name):
    """ deletes all comments of a given user
    :param user_name: username of the user who's comments shall be deleted
    :return: None
    """
    try:
        user_id = UsersTableFunctions.get_user_id(user_name)
        conn = TableCreationFunctions.create_connection()
        cur = conn.cursor()
        cur.execute(f"DELETE FROM comments WHERE comm_author_id=?;", (user_id,))
        conn.commit()
        conn.close()
    except Error as e:
        print(e)
        conn.rollback()


def delete_all_comments_of_posts_from_user(post_id_tuple):
    """ deletes all comments on a given user's posts
    :param post_id_tuple: Tuple of post_ids from a User that shall be deleted
    :return: None
    """
    try:
        conn = TableCreationFunctions.create_connection()
        cur = conn.cursor()
        if post_id_tuple is not None:
            for post_id in post_id_tuple:
                cur.execute(f"DELETE FROM comments WHERE comm_post_id=?;", (post_id, ))
        conn.commit()
        conn.close()
    except Error as e:
        print(e)
        conn.rollback()


# Select Functions:

def get_all_comments_of_post(post_id):
    """ returns all comments of a given post
    :param post_id: post_id
    :return: all comments of a given post (Integers in Tuple)
    """
    try:
        conn = TableCreationFunctions.create_connection()
        cur = conn.cursor()
        cur.execute(f"""
                        SELECT comment_id FROM comments
                        WHERE comm_post_id = ?;""", (post_id,))
        row = cur.fetchall()
        conn.commit()
        conn.close()
        if row:
            comments_tuple = ()
            for comment in row:
                comments_tuple = comments_tuple + comment
            return comments_tuple
        else:
            return None
    except Error as e:
        print(e)
        conn.rollback()


def get_comment_id(values):
    """ returns the comment_id of a given comment
    :param values: post_id, author_user_name, date_time, comm_content
    :return: comment_id (Integer)
    """
    try:
        author_id = UsersTableFunctions.get_user_id(values[1])
        conn = TableCreationFunctions.create_connection()
        cur = conn.cursor()
        cur.execute(f"""
                        SELECT comment_id FROM comments 
                        WHERE comm_post_id = ? AND comm_author_id = ?
                        AND date_time = ? AND comm_content = ?;""", (values[0], author_id, values[2], values[3]))
        row = cur.fetchone()
        conn.commit()
        conn.close()
        if row:
            return row[0]
        else:
            return None
    except Error as e:
        print(e)
        conn.rollback()


def get_comment_post_id(comment_id):
    """ returns the comm_post_id of a given comment
    :param comment_id:
    :return: comm_post_id (Integer) // ID of the post
    """
    try:
        conn = TableCreationFunctions.create_connection()
        cur = conn.cursor()
        cur.execute(f"""
                        SELECT comm_post_id FROM comments 
                        WHERE comment_id = ?;""", comment_id)
        row = cur.fetchone()
        conn.commit()
        conn.close()
        if row:
            return row[0]
        else:
            return None
    except Error as e:
        print(e)
        conn.rollback()


def get_comment_author_id(comment_id):
    """ returns the comm_post_id of a given comment
    :param comment_id:
    :return: comm_author_id (Integer) // ID of the comment's author
    """
    try:
        conn = TableCreationFunctions.create_connection()
        cur = conn.cursor()
        cur.execute(f"""
                        SELECT comm_author_id FROM comments 
                        WHERE comment_id = ?;""", comment_id)
        row = cur.fetchone()
        conn.commit()
        conn.close()
        if row:
            return row[0]
        else:
            return None
    except Error as e:
        print(e)
        conn.rollback()


def get_comment_date_time(comment_id):
    """ returns the comm_post_id of a given comment
    :param comment_id:
    :return: date_time: unix timestamp
    """
    try:
        conn = TableCreationFunctions.create_connection()
        cur = conn.cursor()
        cur.execute(f"""
                        SELECT date_time FROM comments 
                        WHERE comment_id = ?;""", comment_id)
        row = cur.fetchone()
        conn.commit()
        conn.close()
        if row:
            return row[0]
        else:
            return None
    except Error as e:
        print(e)
        conn.rollback()


def get_comment_content(comment_id):
    """ returns the comm_post_id of a given comment
    :param comment_id:
    :return: comm_content: text content of the comment
    """
    try:
        conn = TableCreationFunctions.create_connection()
        cur = conn.cursor()
        cur.execute(f"""
                        SELECT comm_content FROM comments 
                        WHERE comment_id = ?;""", comment_id)
        row = cur.fetchone()
        conn.commit()
        conn.close()
        if row:
            return row[0]
        else:
            return None
    except Error as e:
        print(e)
        conn.rollback()
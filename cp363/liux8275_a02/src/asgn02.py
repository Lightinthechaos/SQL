'''
Created on 2019 M02 19

@author: liux8275
'''

def publications(conn, title=None, pub_type_id=None):
    """
    -------------------------------------------------------
    Queries the pub table.
    Use: rows = publications(conn)
    Use: rows = publications(conn, title=v1)
    Use: rows = publications(conn, pub_type_id=v2)
    Use: rows = publications(conn, title=v1, pub_type_id=v2)
    -------------------------------------------------------
    Parameters:
        conn - a database connection (Connect)
        title - a partial title (str)
        pub_type_id - a publication type (str)
    Returns:
        rows - a list with a member's last name, a member's first
                name, the title of a publication, and the full publication
                type (i.e. 'article' rather than 'a';
        the entire table if title and pub_type_id are None,
        else rows matching the partial title and pub_type_id 
        if given 
                sorted by last name, first name, title (list of ?)
    -------------------------------------------------------
    """
    if title is None and pub_type_id is None:
        sql = """SELECT member.last_name , member.first_name, pub.p_title, pub_type.pt_desc 
                 FROM pub 
                 INNER JOIN member ON pub.member_id = member.member_id
                 INNER JOIN pub_type ON pub.pub_type_id = pub_type.pub_type_id
                 ORDER BY last_name, first_name, p_title""" 
        conn.cursor.execute(sql)
        rows = conn.cursor.fetchall()
    elif title is None:
        sql = """SELECT member.last_name , member.first_name, pub.p_title, pub_type.pt_desc 
                 FROM pub 
                 INNER JOIN member ON pub.member_id = member.member_id
                 INNER JOIN pub_type ON pub.pub_type_id = pub_type.pub_type_id
                 WHERE pub.pub_type_id = %s
                 ORDER BY last_name, first_name, p_title"""
        param = [pub_type_id]
        conn.cursor.execute(sql,param)
        rows = conn.cursor.fetchall()
    elif pub_type_id is None:
        sql = """SELECT member.last_name , member.first_name, pub.p_title, pub_type.pt_desc 
                 FROM pub 
                 INNER JOIN member ON pub.member_id = member.member_id
                 INNER JOIN pub_type ON pub.pub_type_id = pub_type.pub_type_id
                 WHERE pub.p_title LIKE %s
                 ORDER BY last_name, first_name, p_title"""
        param = ['%' + title + '%']
        conn.cursor.execute(sql,param)
        rows = conn.cursor.fetchall()
    else:
        sql = """SELECT member.last_name , member.first_name, pub.p_title, pub_type.pt_desc 
                 FROM pub 
                 INNER JOIN member ON pub.member_id = member.member_id
                 INNER JOIN pub_type ON pub.pub_type_id = pub_type.pub_type_id
                 WHERE pub.pub_type_id = %s AND pub.p_title LIKE %s
                 ORDER BY last_name, first_name, p_title"""
        param = [pub_type_id, '%' + title + '%']
        conn.cursor.execute(sql,param)
        rows = conn.cursor.fetchall()
    return rows


def pub_counts(conn, member_id, pub_type_id=None):
    """
    -------------------------------------------------------
    Queries the pub table.
    Use: rows = pub_counts(conn, member_id=v1)
    Use: rows = pub_counts(conn, member_id=v1, pub_type_id=v2)
    -------------------------------------------------------
    Parameters:
        conn - a database connection (Connect)
        member_id - a member ID number (int)
        pub_type_id - a publication type (str)
    Returns:
        rows - a list with a member's last name, a member's first
        name, and the number of publications of type pub_type
        if given, if not, the number of all their publications (list of ?)
    -------------------------------------------------------
    """
    if pub_type_id is None:
        sql = """SELECT member.last_name, member.first_name, COUNT(pub.pub_type_id) AS number_publications
                 FROM pub
                 INNER JOIN member ON pub.member_id = member.member_id
                 GROUP BY pub.member_id"""
        conn.cursor.execute(sql)
        rows = conn.cursor.fetchall()
    else:
        sql = """SELECT member.last_name, member.first_name, COUNT(pub.pub_type_id) AS number_publications
                 FROM pub
                 INNER JOIN member ON pub.member_id = member.member_id
                 WHERE pub.pub_type_id = %s
                 GROUP BY pub.member_id
                 """
        param = [pub_type_id]
        conn.cursor.execute(sql, param)
        rows = conn.cursor.fetchall()
        
    return rows

def member_expertise_count(conn, member_id=None):
    """
    -------------------------------------------------------
    Use: rows = member_expertise_count(conn)
    Use: rows = member_expertise_count(conn, member_id=v1)
    -------------------------------------------------------
    Parameters:
        conn - a database connection (Connect)
        member_id - a member ID number (int)
    Returns:
        rows - a list with a member's last name, a member's first
        name, and the count of the number of expertises they
            hold (i.e. keywords)
        all records member_id is None, sorted by last name, first name
        (list of ?)
    -------------------------------------------------------
    """
    if member_id is None:
        sql = """SELECT member.last_name, member.first_name, COUNT(member_keyword.keyword_id) AS number_expertises
                 FROM member_keyword
                 INNER JOIN member ON member_keyword.member_id = member.member_id
                 GROUP BY member_keyword.member_id
                 ORDER BY member.last_name, member.first_name"""
        conn.cursor.execute(sql)
        rows = conn.cursor.fetchall()
    else:
        sql = """SELECT member.last_name, member.first_name, COUNT(member_keyword.keyword_id) AS number_expertises
                 FROM member_keyword
                 INNER JOIN member ON member_keyword.member_id = member.member_id
                 WHERE member_keyword.member_id = %s
                 GROUP BY member_keyword.member_id
                 ORDER BY member.last_name, member.first_name"""
        param = [member_id]
        conn.cursor.execute(sql, param)
        rows = conn.cursor.fetchall()
    return rows
        
def all_expertise(conn, member_id=None):
    """
    -------------------------------------------------------
    Use: rows = all_expertise(conn)
    Use: rows = all_expertise(conn, member_id=v1)
    -------------------------------------------------------
    Parameters:
        conn - a database connection (Connect)
        member_id - a member ID number (int)
    Returns:
        rows - a list with a member's last name, a member's first
        name, a keyword description, and a supplementary keyword description
        all records if member_id is None, 
        sorted by last_name, first_name, keyword description, supplementary 
                keyword description
    -------------------------------------------------------
    """
    if member_id is None:
        sql = """SELECT member.last_name, member.first_name, keyword.k_desc, supp_key.sk_desc
                 FROM member
                 INNER JOIN member_supp_key ON member_supp_key.member_id = member.member_id
                 INNER JOIN supp_key ON supp_key.supp_key_id = member_supp_key.supp_key_id
                 INNER JOIN keyword ON keyword.keyword_id = keyword.keyword_id
                 ORDER BY member.last_name, member.first_name, keyword.k_desc, supp_key.sk_desc"""
        conn.cursor.execute(sql)
        rows = conn.cursor.fetchall()
        
    else:
        sql = """SELECT member.last_name, member.first_name, keyword.k_desc, supp_key.sk_desc
                 FROM member
                 INNER JOIN member_supp_key ON member_supp_key.member_id = member.member_id
                 INNER JOIN supp_key ON supp_key.supp_key_id = member_supp_key.supp_key_id
                 INNER JOIN keyword ON keyword.keyword_id = keyword.keyword_id
                 WHERE member_supp_key.member_id = %s
                 ORDER BY member.last_name, member.first_name, keyword.k_desc, supp_key.sk_desc"""
        param = [member_id]
        conn.cursor.execute(sql,param)
        rows = conn.cursor.fetchall()
    
    return rows     
        
        
        
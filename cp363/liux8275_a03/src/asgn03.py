'''
Created on 2019 M03 8

@author: liux8275
'''

def pub_counts_all(conn, member_id=None):
    """
    -------------------------------------------------------
    Queries the pub and member tables.
    Use: rows = pub_counts(conn)
    Use: rows = pub_counts(conn, member_id=v1)
    -------------------------------------------------------
    Parameters:
        conn - a database connection (Connect)
        member_id - a member ID number (int)
    Returns:
        rows - a list with a member's last name, a member's first
        name, and the number of publications of each type. Name these
        three fields "articles", "papers", and "books". List the results
        as appropriate in order by member last name and first name.
        If member_id is None, list all members. (list of ?)
    -------------------------------------------------------
    """
    if member_id is None:
        sql = """SELECT member.last_name, member.first_name, 
        (SELECT COUNT(pub_type_id) FROM pub WHERE pub_type_id = 'a' AND member_id = member.member_id) as articles,
        (SELECT COUNT(pub_type_id) FROM pub WHERE pub_type_id = 'p' AND member_id = member.member_id) as papers,
        (SELECT COUNT(pub_type_id) FROM pub WHERE pub_type_id = 'b' AND member_id = member.member_id) as books
        FROM member 
        JOIN pub ON member.member_id = pub.member_id 
        GROUP BY member.member_id 
        ORDER BY last_name, first_name"""
        conn.cursor.execute(sql)
        rows = conn.cursor.fetchall()
    else:
        sql = """SELECT member.last_name, member.first_name, 
                (SELECT COUNT(*) FROM pub WHERE pub_type_id = 'a' and member_id = member.member_id) as articles, 
                (SELECT COUNT(*) FROM pub WHERE pub_type_id = 'p' and member_id = member.member_id) as papers, 
                (SELECT COUNT(*) FROM pub WHERE pub_type_id = 'b' and member_id = member.member_id) as books
                FROM pub JOIN member
                ON member.member_id = pub.member_id
                WHERE member.member_id = %s
                GROUP BY member.member_id
                ORDER BY last_name, first_name"""
        param = [member_id]
        conn.cursor.execute(sql,param)
        rows = conn.cursor.fetchall()
    return rows

def expertise_count(conn, member_id=None):
    """
    -------------------------------------------------------
    Use: rows = expertise_count(conn)
    Use: rows = expertise_count(conn, member_id=v1)
    -------------------------------------------------------
    Parameters:
        conn - a database connection (Connect)
        member_id - a member ID number (int)
    Returns:
        rows - a list with a member's last name, a member's first
        name, and the number of keywords and supplementary keywords
        for the member. Name these fields "keywords" and "supp_keys".
        List the results as appropriate in order by member last 
        name and first name. If member_id is None, list all members.
        (list of ?)
    -------------------------------------------------------
    """
    if member_id is None:
        sql = """SELECT member.last_name, member.first_name,
                (SELECT COUNT(keyword_id) FROM member_keyword WHERE member_id = member.member_id) AS keywords,
                (SELECT COUNT(supp_key_id) FROM member_supp_key WHERE member_id = member.member_id) AS supp_keys
                FROM member 
                JOIN member_supp_key ON member.member_id = member_supp_key.member_id
                JOIN member_keyword ON member.member_id = member_keyword.member_id
                GROUP BY member.member_id
                ORDER BY last_name, first_name"""
        conn.cursor.execute(sql)
        rows = conn.cursor.fetchall()
    else:
        sql = """SELECT member.last_name, member.first_name,
                (SELECT COUNT(keyword_id) FROM member_keyword WHERE member_id = member.member_id) AS keywords,
                (SELECT COUNT(supp_key_id) FROM member_supp_key WHERE member_id = member.member_id) AS supp_keys
                FROM member 
                JOIN member_supp_key ON member.member_id = member_supp_key.member_id
                JOIN member_keyword ON member.member_id = member_keyword.member_id
                WHERE member.member_id = %s
                GROUP BY member.member_id
                ORDER BY last_name, first_name"""
        param = [member_id]
        conn.cursor.execute(sql,param)
        rows = conn.cursor.fetchall()
    
    return rows
        
def keyword_count(conn, keyword_id=None):
    """
    -------------------------------------------------------
    Use: rows = keyword_count(conn)
    Use: rows = keyword_count(conn, keyword_id=v1)
    -------------------------------------------------------
    Parameters:
        conn - a database connection (Connect)
        keyword_id - a keyword ID number (int)
    Returns:
        rows - a list with a keyword's description and the number of
        supplementary keywords that belong to it. Name the second field
        "supp_key_count".
        List the results as appropriate in order by keyword description. 
        If keyword_id is None, list all keywords. (list of ?)
    -------------------------------------------------------
    """
    if keyword_id is None:
        sql = """SELECT keyword.k_desc, 
                (SELECT COUNT(supp_key_id) FROM supp_key WHERE keyword_id = keyword.keyword_id) as supp_keys_count
                FROM keyword JOIN supp_key ON keyword.keyword_id = supp_key.keyword_id
                GROUP BY keyword.keyword_id
                ORDER BY keyword.k_desc"""
        conn.cursor.execute(sql)
        rows = conn.cursor.fetchall()
    else:
        sql = """SELECT keyword.k_desc, 
                (SELECT COUNT(supp_key_id) FROM supp_key WHERE keyword_id = keyword.keyword_id) as supp_keys_count
                FROM keyword JOIN supp_key ON keyword.keyword_id = supp_key.keyword_id
                WHERE keyword.keyword_id = %s
                GROUP BY keyword.keyword_id
                ORDER BY keyword.k_desc"""
        param = [keyword_id]
        conn.cursor.execute(sql, param)
        rows = conn.cursor.fetchall()
    
    return rows
                
def keyword_member_count(conn, keyword_id=None):
    """
    -------------------------------------------------------
    Use: rows = keyword_member_count(conn)
    Use: rows = keyword_member_count(conn, keyword_id=v1)
    -------------------------------------------------------
    Parameters:
        conn - a database connection (Connect)
        keyword_id - a keyword ID number (int)
    Returns:
        rows - a list with a keyword's description and the number of
        members that have it. Name the second field
        "member_count".
        List the results as appropriate in order by keyword description. 
        If keyword_id is None, list all keywords. (list of ?)
    -------------------------------------------------------
    """
    if keyword_id is None:
        sql = """SELECT keyword.k_desc, 
                (SELECT COUNT(member_id) FROM member_keyword WHERE keyword_id = keyword.keyword_id) as member_count
                FROM keyword JOIN member_keyword ON keyword.keyword_id = member_keyword.keyword_id
                GROUP BY keyword.keyword_id
                ORDER BY keyword.k_desc"""
        conn.cursor.execute(sql)
        rows = conn.cursor.fetchall()
    else:
        sql = """SELECT keyword.k_desc, 
                (SELECT COUNT(member_id) FROM member_keyword WHERE keyword_id = keyword.keyword_id) as member_count
                FROM keyword JOIN member_keyword ON keyword.keyword_id = member_keyword.keyword_id
                WHERE keyword.keyword_id = %s
                GROUP BY keyword.keyword_id
                ORDER BY keyword.k_desc"""
        param = [keyword_id]
        conn.cursor.execute(sql, param)
        rows = conn.cursor.fetchall()
    
    return rows

def supp_key_member_count(conn, supp_key_id=None):
    """
    -------------------------------------------------------
    Use: rows = supp_key_member_count(conn)
    Use: rows = supp_key_member_count(conn, supp_key_id=v1)
    -------------------------------------------------------
    Parameters:
        conn - a database connection (Connect)
        supp_key_id - a supp_key ID number (int)
    Returns:
        rows - a list with a keyword's description, a supplementary
        keyword description, and the number of members that have it. 
        Name the last field "member_count".
        List the results as appropriate in order by keyword description
        and then supplementary keyword description.
        If supp_key_id is None, list all keywords and supplementary
        keywords. (list of ?)
    -------------------------------------------------------
    """
    if supp_key_id is None:
        sql = """SELECT k_desc, sk_desc,
                (SELECT COUNT(member_id) FROM member_supp_key WHERE supp_key_id = supp_key.supp_key_id) as member_count
                FROM member_supp_key JOIN supp_key ON member_supp_key.supp_key_id = supp_key.supp_key_id
                JOIN keyword ON supp_key.keyword_id = keyword.keyword_id
                GROUP BY supp_key.supp_key_id
                ORDER BY keyword.k_desc, supp_key.sk_desc"""
        conn.cursor.execute(sql)
        rows = conn.cursor.fetchall()
    else:
        sql = """SELECT k_desc, sk_desc,
                (SELECT COUNT(member_id) FROM member_supp_key WHERE supp_key_id = supp_key.supp_key_id) as member_count
                FROM member_supp_key JOIN supp_key ON member_supp_key.supp_key_id = supp_key.supp_key_id
                JOIN keyword ON supp_key.keyword_id = keyword.keyword_id
                WHERE supp_key.supp_key_id = %s
                GROUP BY supp_key.supp_key_id
                ORDER BY keyword.k_desc, supp_key.sk_desc"""
        param = [supp_key_id]
        conn.cursor.execute(sql, param)
        rows = conn.cursor.fetchall()
    
    return rows
   
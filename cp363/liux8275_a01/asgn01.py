from Connect import Connect


def keyword_table(conn, keyword_id=None):
    """
    -------------------------------------------------------
    Queries the keyword table.
    Use: rows = keyword_table(conn)
    Use: rows = keyword_table(conn, keyword_id=v)
    -------------------------------------------------------
    Parameters:
        conn - a database connection (Connect)
        keyword_id - a keyword ID number (int)
    Returns:
        rows - a list with the contents of the keyword table;
        the entire table if keyword_id is None, else the row 
        matching keyword_id (list of ?)
    -------------------------------------------------------
    """
    # Connect to the DCRIS database with an option file
    
    if keyword_id is None:
        sql = "SELECT * FROM keyword"
        conn.cursor.execute(sql)
        rows = conn.cursor.fetchall()
        
    else:
        sql = "SELECT * FROM keyword WHERE keyword_id = %s"
        params = [keyword_id]
        conn.cursor.execute(sql,params)
        rows = conn.cursor.fetchall()
    
    
    return rows
   
def pub_table(conn, member_id=None, pub_type_id=None):
    """
    -------------------------------------------------------
    Queries the pub table.
    Use: rows = pub_table(conn)
    Use: rows = pub_table(conn, member_id=v1)
    Use: rows = pub_table(conn, pub_type_id=v2)
    Use: rows = pub_table(conn, member_id=v1, pub_type_id=v2)
    -------------------------------------------------------
    Parameters:
        conn - a database connection (Connect)
        member_id - a member ID number (int)
        pub_type_id - a publication type (str)
    Returns:
        rows - a list with the contents of the pub table;
        the entire table if member_id and pub_type_id are None,
        else rows matching member_id and pub_type_id 
        if given (list of ?)
    -------------------------------------------------------
    """
   
    if member_id is None and pub_type_id is None:
        sql = "SELECT * FROM pub"
        conn.cursor.execute(sql)
        rows = conn.cursor.fetchall()
    elif member_id is None:
        sql = "SELECT * FROM pub WHERE pub_type_id = %s"
        params = [pub_type_id]
        conn.cursor.execute(sql,params)
        rows = conn.cursor.fetchall()
    elif pub_type_id is None:
        sql = "SELECT * FROM pub WHERE member_id = %s"
        params = [member_id]
        conn.cursor.execute(sql,params)
        rows = conn.cursor.fetchall()
    else:
        sql = "SELECT * FROM pub WHERE pub_type_id = %s AND member_id = %s"
        params = [pub_type_id, member_id]
        conn.cursor.execute(sql, params)
        rows = conn.cursor.fetchall()
  
    return rows

def member_expertise(conn, member_id=None, keyword_id=None):
    """
    -------------------------------------------------------
    Queries the v_member_keyword view.
    Use: rows = member_expertise(conn)
    Use: rows = member_expertise(conn, member_id=v1)
    Use: rows = member_expertise(conn, keyword_id=v2)
    Use: rows = member_expertise(conn, member_id=v1, keyword_id=v2)
    -------------------------------------------------------
    Parameters:
        conn - a database connection (Connect)
        member_id - a member ID number (int)
        keyword_id - a keyword ID number (int)
    Returns:
        rows - a list with the last name, first name, and keyword
            description of the v_member_keyword view:
        the entire view if member_id and keyword_id are None, 
            sorted by last name, first name, keyword description
        rows matching member_id if keyword_id is None:
            sorted by last name, first name, keyword description
        rows matching keyword_id if member_id is None:
            sorted by keyword description, last name, first name
        otherwise rows unsorted
        if given (list of ?)
    -------------------------------------------------------
    """
  
    if member_id is None and keyword_id is None:
        sql = "SELECT last_name, first_name, k_desc FROM v_member_keyword ORDER BY last_name, first_name, k_desc"
        conn.cursor.execute(sql)
        rows = conn.cursor.fetchall()
    elif keyword_id is None:
        sql = "SELECT last_name, first_name, k_desc FROM v_member_keyword WHERE member_id = %s ORDER BY last_name, first_name, k_desc"
        params = [member_id]
        conn.cursor.execute(sql, params)
        rows = conn.cursor.fetchall()
    elif member_id is None:
        sql = "SELECT last_name, first_name, k_desc FROM v_member_keyword WHERE keyword_id = %s ORDER BY k_desc, last_name, first_name"
        params = [keyword_id]
        conn.cursor.execute(sql, params)
        rows = conn.cursor.fetchall()
    else:
        sql = "SELECT last_name, first_name, k_desc FROM v_member_keyword WHERE keyword_id = %s and member_id = %s"
        params = [keyword_id, member_id]
        conn.cursor.execute(sql, params)
        rows = conn.cursor.fetchall()
 
    return rows

def expertise(conn, keyword=None, supp_key=None):
    """
    -------------------------------------------------------
    Queries the v_keyword_supp_key view.
    Use: rows = expertise(conn)
    Use: rows = expertise(conn, keyword=v1)
    Use: rows = expertise(conn, supp_key=v2)
    Use: rows = expertise(conn, keyword=v1, supp_key=v2)
    -------------------------------------------------------
    Parameters:
        conn - a database connection (Connect)
        keyword - a partial keyword description (str)
        supp_key - a partial supplementary description (str)
    Returns:
        rows - a list with the keyword and supplementary keyword descriptions
            of the v_keyword_supp_key view:
        the entire view if keyword and supp_key are None, 
            sorted by keyword description, supplementary keyword description
        rows containing keyword if supp_key is None:
            sorted by keyword description, supplementary keyword description
        rows matching supp_key if keyword is None:
            sorted by supplementary keyword description, keyword description 
        otherwise rows
            sorted by keyword description, supplementary keyword description
    -------------------------------------------------------
    """

    if keyword is None and supp_key is None:
        sql = "SELECT k_desc, sk_desc FROM v_keyword_supp_key ORDER BY k_desc, sk_desc"  
        conn.cursor.execute(sql)
        rows = conn.cursor.fetchall()
    elif supp_key is None:
        sql = "SELECT k_desc, sk_desc FROM v_keyword_supp_key WHERE k_desc LIKE %s ORDER BY k_desc, sk_desc"
        param = ['%' + keyword + '%']
        conn.cursor.execute(sql, param)
        rows = conn.cursor.fetchall()
    elif keyword is None:
        sql = "SELECT k_desc, sk_desc FROM v_keyword_supp_key WHERE sk_desc LIKE %s ORDER BY sk_desc, k_desc"
        param = ['%' + supp_key + '%']
        conn.cursor.execute(sql, param)
        rows = conn.cursor.fetchall()
    else:
        sql = "SELECT k_desc, sk_desc FROM v_keyword_supp_key WHERE k_desc LIKE %s and sk_desc LIKE %s ORDER BY k_desc, sk_desc"
        param = ['%' + keyword + '%', '%' + supp_key + '%']
        conn.cursor.execute(sql, param)
        rows = conn.cursor.fetchall()

    return rows
    
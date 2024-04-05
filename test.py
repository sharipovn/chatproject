import psycopg2
from psycopg2.extras import execute_values

records = [('021169002636', '2024-03-02 02:00:00', 0, 0, None, None, None, None, 0,
None, None, 0, None, None, 0, None, None, None, None, None, None, None, None, None),
('021169002636', '2024-03-02 02:00:00', 0, 0, None, None, None, None, 0,
None, None, 0, None, None, 0, None, None, None, None, None, None, None, None, None)
]

insert_query = """
    INSERT INTO all_reestr.sam_lp_18218
    (m_no, up_date, use_aplus_kwh, use_aminus_kwh, use_rplus_kvarh, use_rminus_kvarh,
    pow_splus_kva, pow_sminus_kva, max_v_l1, max_v_l2, max_v_l3, min_v_l1, min_v_l2, min_v_l3,
    pf, avg_a_l1, avg_a_l2, avg_a_l3, pf_l1, pf_l2, pf_l3, avg_v_l1, avg_v_l2, avg_v_l3)
    VALUES %s
    ON CONFLICT (m_no, up_date) DO NOTHING"""




def pg_sql_insert(sql_insert_statement, data_tuple):
    cursor = None
    conn = None
    try:
        conn = psycopg2.connect(host='192.168.14.74', user='test', password='test', database='reestr')
        cursor = conn.cursor()
        execute_values(cursor,sql_insert_statement, data_tuple,template=None,page_size=1000)
        conn.commit()
    except Exception as error:
        print("Chota insert yemadi PostGreSQL: ", error)
    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()

pg_sql_insert(insert_query, records)
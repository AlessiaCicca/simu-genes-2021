from database.DB_connect import DBConnect


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getNodi():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select g.GeneID as gene
from genes g 
where g.Essential ='Essential'
"""

        cursor.execute(query)

        for row in cursor:
            result.append(row["gene"])

        cursor.close()
        conn.close()
        return result
    @staticmethod
    def getConnessioni():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct i.GeneID1 as v1, i.GeneID2 as v2, g1.Chromosome c1, g2.Chromosome c2, i.Expression_Corr as peso 
from interactions i, genes g1,genes g2
where i.GeneID1 =g1.geneID and i.GeneID2 =g2.GeneID """

        cursor.execute(query)

        for row in cursor:
            result.append((row["v1"],row["v2"], row["c1"], row["c2"], row["peso"]))

        cursor.close()
        conn.close()
        return result

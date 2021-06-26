from core.pyba_logic import PybaLogic


class CityLogic(PybaLogic):
    def __init__(self):
        super().__init__()

    # get
    def getCityById(self, id):
        database = self.createDatabaseObj()
        sql = f"SELECT * FROM world.city where ID={id};"
        result = database.executeQuery(sql)
        if len(result) != 0:
            return result[0]
        else:
            return {}

    # post
    def getCityByCountryCode(self, countryCode):
        database = self.createDatabaseObj()
        sql = f"SELECT * FROM world.city where CountryCode='{countryCode}';"
        result = database.executeQuery(sql)
        if len(result) != 0:
            return result
        else:
            return []

    # put
    def insertCity(self, city):
        database = self.createDatabaseObj()
        sql = (
            f"INSERT INTO `world`.`city`"
            + f"(`ID`,`Name`,`CountryCode`,`District`,`Population`) "
            + f"VALUES(0,'{city['Name']}','{city['CountryCode']}','{city['District']}',{city['Population']});"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    # patch
    def updateCity(self, id, city):
        database = self.createDatabaseObj()
        sql = (
            f"UPDATE `world`.`city` "
            + f"SET `Name` = '{city['Name']}',`CountryCode` = '{city['CountryCode']}',"
            + f"`District` = '{city['District']}',`Population` = {city['Population']} "
            + f"WHERE `ID` = {id};"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    # delete
    def deleteCity(self, id):
        database = self.createDatabaseObj()
        sql = f"DELETE FROM `world`.`city` WHERE ID={id};"
        rows = database.executeNonQueryRows(sql)
        return rows

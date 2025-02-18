import sqlite3,os

conn = sqlite3.connect('lookup.sqlite')

cursor = conn.cursor()

class DatabaseHandler:

    def __init__(self):
       
        self.table_list = [
            
            """CREATE TABLE length_conversion (
            unit TEXT PRIMARY KEY,  
            millimeter REAL,
            centimeter REAL,
            meter REAL,
            kilometer REAL,
            inch REAL,
            foot REAL,
            yard REAL,
            mile REAL)""",

            """CREATE TABLE temperature_conversion (
            unit TEXT PRIMARY KEY,             
            celsius REAL, 
            fahrenheit REAL, 
            kelvin REAL)""",

            """CREATE TABLE weight_conversion (
            unit TEXT PRIMARY KEY,  
            milligram REAL, 
            gram REAL, 
            kilogram REAL, 
            ounce REAL, 
            pound REAL)"""


        ]



    def __open(self):

        cwd = os.getcwd()

        print("the database path",cwd+"/database/lookup.db")
        #for regular code
        self.connection = sqlite3.connect(cwd+"/unitconverter/database/lookup.db")


        #for test code
        # self.connection = sqlite3.connect(cwd+"/lookup.db")
        
        self.cursor =  self.connection.cursor()                                           

    def __close(self):
        if self.connection != None:
            self.connection.close()
    
    def drop_table(self):

        self.__open()

        querry ="""DROP TABLE IF EXISTS unit_conversion"""

        self.cursor.execute(querry)

        self.connection.commit()

        self.__close()


    def create_table(self):

        self.__open()

        for item in self.table_list:

            self.cursor.execute(item)


        self.__close()


    def fill_up_rows(self):

        self.__open()

        querry =""" INSERT INTO temperature_conversion (unit, celsius, fahrenheit, kelvin) VALUES
                    ('celsius', 1, 1.8, 1),
                    ('fahrenheit', 0.5556, 1, 0.5556),
                    ('kelvin', 1, 1.8, 1) """

        try:
            self.cursor.execute(querry)
            self.connection.commit()  # Use commit() for queries that modify data (INSERT, UPDATE, DELETE)
            
        except Exception as e:
            print("fillup rows Exception",e)

        finally:
            self.__close()
    
    def get_conversion(self,from_unit,to_unit,table_name):

        self.__open()
        
        print("The thing",from_unit,to_unit,table_name)
        querry =  f"SELECT {to_unit} FROM {table_name} WHERE unit = ?" 
        
        try:
            result = self.cursor.execute(querry,(from_unit,))
        
            return result.fetchone()[0]
        
        except Exception as e:
            print("get conversion Exception",e)

        finally:
            self.__close

if __name__ == "__main__":

    db = DatabaseHandler()

    # db.create_table()
    # print(db.get_conversion('millimeter','meter','length_conversion'))
    # db.drop_table()
    db.fill_up_rows()
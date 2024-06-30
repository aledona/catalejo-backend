from app.database import get_db

class Country:
    def __init__(self,id=None,name=None):
        self.id=id
        self.name= name 

    def serialize(self):
        return {
            'id':self.id,
            'name':self.name,
        }
    
    @staticmethod
    def get_all():
        db = get_db()
        cursor = db.cursor()
        query = "SELECT * FROM countries"
        cursor.execute(query)
        rows = cursor.fetchall()
        countries = [Country(id=row[0], name=row[1]) for row in rows]
        cursor.close()
        return countries

class User:
    def __init__(self,id=None,firstname=None,lastname=None,genre=None,email=None,passsword=None,birthday=None,country=None, lastlogin=None):
        self.id=id
        self.firstname= firstname
        self.lastname= lastname
        self.genre= genre
        self.email= email
        self.passsword= passsword
        self.birthday= birthday
        self.country= country
        self.lastlogin= lastlogin

    def serialize(self):
        return {
            'id':self.id,
            'firstname':self.firstname,
            'lastname':self.lastname,
            'genre':self.genre,
            'email':self.email,
            'passsword':self.passsword,
            'birthdate':self.birthdate.strftime('%Y-%m-%d'),
            'country':self.country,
            'lastlogin':self.lastlogin.strftime('%Y-%m-%d'),
        }
    
    def saveLastLogin(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("""
            UPDATE users SET lastlogin = %s
            WHERE id = %s
        """, (self.lastlogin, self.id))
      
        db.commit()
        cursor.close()

    @staticmethod
    def get_by_id(id):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM users WHERE id = %s", (id,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return User(id=row[0], firstname=row[1], lastname=row[2], genre=row[3], email=row[4],
                        passsword=row[5], birthdate=row[6], country=row[7], lastlogin=row[8])
        return None


    def CreateUser(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("""
            INSERT INTO users (firstname, lastname, genre, email, 
                       password, birthdate, country, lastlogin ) 
                       VALUES (%s, %s, %s, %s,%s, %s, %s, %s)
        """, (self.firstname, self.lastname, self.genre, self.email,
              self.passsword, self.birthdate, self.country, self.lastlogin))
        #voy a obtener el último id generado
        self.id = cursor.lastrowid
      
        db.commit()
        cursor.close()
    
    def delete(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM users WHERE id = %s", (self.id,))
        db.commit()
        cursor.close()

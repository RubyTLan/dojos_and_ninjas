from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

class Dojo:
    def __init__(self,data):
        self.id=data['id']
        self.name=data['name']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']

    @classmethod
    def save(cls, data ):

        query = "INSERT INTO dojos ( name) VALUES ( %(name)s  );"

        return connectToMySQL('dojos_and_ninjas').query_db( query, data )

    @classmethod
    def get_all_dojos(cls):
        query="select * from dojos_and_ninjas.dojos;"
        results= connectToMySQL('dojos_and_ninjas').query_db( query )
        dojos=[]
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos

    @classmethod
    def get_one_with_ninjas(cls,data):
        query="select * from dojos left join ninjas on dojos.id=ninjas.dojo_id where dojos.id= %(id)s;"
        results= connectToMySQL('dojos_and_ninjas').query_db( query,data )
        print(results)
        if results:
            dojo_instance=cls(results[0])
            ninjas_list=[]
            for row in results:
                if row['ninjas.id']==None:
                    return dojo_instance
                ninja_data={
                    'id':row['ninjas.id'],
                    'first_name':row['first_name'],
                    'last_name':row['last_name'],
                    'age':row['age'],
                    'created_at':row['ninjas.created_at'],
                    'updated_at':row['ninjas.updated_at'],
                    'dojo_id':row['dojo_id']
                }
                ninja_instance=ninja.Ninja(ninja_data)
                ninjas_list.append(ninja_instance)
            dojo_instance.ninjas=ninjas_list #随时可以创建attribute
            return dojo_instance
        return False

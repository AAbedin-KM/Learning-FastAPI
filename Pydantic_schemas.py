#Pydantic schemas are classes that define the structure and validaiton rules for data 
#it gives structure by declaring variables and then restricting the data type that variable contain
#a pydantic schema can only be made after importing BaseModel from pydantic and then inheriting from the BaseModel
#then you make your class and then you make ur variables eg:
class FavouriteCharacter(BaseModel): #inherits from BaseModel 
    character : str #variable is defined and then the datatype is defined
    reason : str #this is then repeated for all lines where there is a variable
    how_much_out_of_ten : int
    eaten : Optional[bool]
#you can set a variable in a schema to be optionally filled in by setting a value for it in the schema itself
#specifically on /docs u can enter the values for those variables and they can be referred to in the function the schema is being used in 
#the schema has to be a parameter first by doing [variable] : [schema]
#eg:
def demonstration(request : FavouriteCharater):
  #you can specificaly mention the different variables in the class by doing [schema].[variable]
  #eg:
  return request , request.reason
  
#in summary:
#schemas dictate the structure of a query in FastAPI and store values of variables which can be used in various different ways

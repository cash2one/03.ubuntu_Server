from common.config import *
from database.datamodule import *


# creat table
database_object.create_table(testdb,safe=True)

#insert
for i in range(10):
	print "*"*100
	testdb.insert(name=i).execute()

	print "-"*100
# #creat 
# for i in range(10):
# 	t = testdb.creat(name=i)
# 	t.save()

#update
q = (testdb.update(name="aa")
	.where(testdb.name>50))
q.execute()

print testdb.select().where(testdb.name=="1").count()

#sql 
q = testdb.raw('select id, name from testdb')
for item in q:
    print item.id, item.name

from database.datamodule import *
create_table()
db = db_Movie()
db.insert("tb_test",name="aaa")
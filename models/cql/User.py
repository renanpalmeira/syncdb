# -*- coding: utf8 -*-

import uuid
from datetime import datetime
from cqlengine import columns
from cqlengine import Model

class User(Model):
	user_id      	= columns.UUID(primary_key=True, default=uuid.uuid4)
	name    	 	= columns.Text(index=True)
	email    	 	= columns.Text()	
	age    	 		= columns.Integer()
	create_date     = columns.DateTime(default=datetime.now())
	update_date		= columns.DateTime(default=datetime.now())
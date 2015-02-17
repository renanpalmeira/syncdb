# -*- coding: utf8 -*-

import uuid
from datetime import datetime
from cqlengine import columns
from cqlengine import Model

class Product(Model):
	product_id     	= columns.UUID(primary_key=True, default=uuid.uuid4)
	name    	 	= columns.Text(index=True)
	description  	= columns.Text()	
	price    	 	= columns.Integer()
	create_date     = columns.DateTime(default=datetime.now())
	update_date		= columns.DateTime(default=datetime.now())
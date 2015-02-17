# -*- coding: utf8 -*-

import uuid
from datetime import datetime
from elasticsearch_dsl import DocType, String, Date, Integer

class Product(DocType):
	
	name 			 = String()
	description		 = String()
	price 			 = Integer()
	create_date 	 = Date()
	update_date 	 = Date()

	_dict_model_keys =	['id','name','description','price','create_date','update_date']
	
	def save(self, **kwargs):
		if self.id is None:
			self.id = uuid.uuid4()
		self.update_date = datetime.now()
		self.create_date = datetime.now()
		return super(Product, self).save(**kwargs)

	def __len__(self):
		return len(self._dict_model_keys)
	@classmethod
	def keys(self):
		return self._dict_model_keys
	class Meta:
	    index = 'simbiose_challenge'
	
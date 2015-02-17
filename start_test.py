# -*- coding: utf8 -*-

import connections
from models import Cassandra, ElasticSearch

if __name__=='__main__':
	cql=Cassandra()
	es=ElasticSearch()

	"""
		Exemplos de insert & update.
	"""
	#es.update('user', ID, columns={"name":"Simbiose"})
	#cql.update('user', ID, columns={"name":"Simbiose"})
	es.insert('user', **{"name":"simbioseES","email":"test1@test1.com","age":42})
	cql.insert('user', **{"name":"simbioseCQL","email":"test2@test2.com","age":42})
	
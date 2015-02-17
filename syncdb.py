#!/usr/bin/env python
# -*- coding: utf8 -*-

import datetime
from dateutil import parser
from models import Cassandra, ElasticSearch

"""
	Class SyncDB:
		Ela que da o nome ao desafio, e sua função é fazer sincronização dos bancos suportados.
		Por default até o momento, os bancos suportados são Cassandra & ElasticSearch.
"""
class SyncDB(object):
	"""
	db_class=dict()
	Onde é "armazenado", todas as instâncias dos bancos suportados.

	base='cql' 
	Default(padrão) para a comparação, 
	É apenas um ponto de partida, porque todos os db's que são colocos são sincronizados.
	"""
	db_class=dict()
	base='cql'

	"""
		Adicionar todas instância em db_class.
	"""
	def __init__(self, **kwargs):
		for key, value in kwargs.iteritems():
			if hasattr(value, 'db_type'):
				self.db_class[key]=value
	
	"""
		Função _sync_update:
			Essa função, é vital para o funcionamento da sincronização, ela que confere se existem 
			updates no Cassandra ou ElasticSearch, e atualiza o banco desatualizado, 
			com base no campo update_date que esta presente nas tabelas/index/dados/tipos do bancos.
	"""
	def _sync_update(self, table, db, base=None):
		if base is None:
			base=self.base
		if hasattr(db, 'insert') and hasattr(db, 'get') and hasattr(self.db_class[base], 'insert') and hasattr(self.db_class[base], 'get'):
			db=db
			base=self.db_class[base]
			columns_models=base.model_keys(table)
			db_query=db.get(table)
			base_query=base.get(table)
			for key, value in base_query.iteritems():
				if key in db_query.keys():
					"""
					Seleciona todos os registros do banco de dados, 
					os campos inseridos pelo usuário e os de log.
					"""
					db_all=db_query[key]
					base_all=base_query[key]

					# Busca todos os registros colocados pelo usuario do banco de dados
					columns_models_not_logs=dict(columns_models)
					del columns_models_not_logs['create_date'], columns_models_not_logs['update_date'], columns_models_not_logs[table+"_id"]
					
					base_values = dict()
					db_values = dict()
					

					base_values, result_exec = (
						base_values, 
						[base_values.update({column:base_all[column]}) for column in columns_models_not_logs.keys()]
					)

					db_values, result_exec = (
						db_values, 
						[db_values.update({column:db_all[column]}) for column in columns_models_not_logs.keys()]
					)
					
					# Verifica os valores se são diferentes, parar possibilitar o update
					if db_values.values()!=base_values.values():
						if not type(db_all['update_date']) is datetime.datetime:
							db_all['update_date'] = parser.parse(db_all['update_date'])
						if not type(base_all['update_date']) is datetime.datetime:
							base_all['update_date'] = parser.parse(base_all['update_date'])
						
						max_base_update=max([base_all['update_date'], db_all['update_date']])
						
						if max_base_update in base_all.values():
							db.update(table, key, columns=base_values)
							return True
						elif max_base_update in db_all.values():
							base.update(table, key, columns=db_values)
							return True
		return False

	"""
		Função _sync_db:
			Faz a sincronização de dados novos na banco desatualizado.
	"""
	def _sync_db(self, table, db, base=base):
		if hasattr(db, 'insert') and hasattr(db, 'get') and hasattr(self.db_class[base], 'insert') and hasattr(self.db_class[base], 'get'):
			db=db
			base=self.db_class[base]
			for key, value in base.get(table).iteritems():
				if not key in db.get(table).keys():
					value[table+"_id"]=key
					db.insert(table, **value)
	"""
		Função _check_sync_dbsnc_dbs:
			Confere se há updates ou insert's para serem feitos.
	"""		
	def _check_sync_dbs(self):
		if len(self.db_class)>1 and hasattr(self.db_class[self.base], 'get'):
			base=self.db_class[self.base]
			for key, item_class_instance in self.db_class.iteritems():
				for table in base.models.keys():
					if hasattr(item_class_instance, 'get') and hasattr(base, 'get'):
						sync_insert_cql=self._sync_db(table, base, key)
						sync_insert_es=self._sync_db(table, item_class_instance)	
						sync_update=self._sync_update(table, item_class_instance)	

	"""
		Função run:
			Ela que inicia todos os "processos", citados há cima.
	"""
	def run(self):
		self._check_sync_dbs()
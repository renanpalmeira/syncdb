#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
	Arquivo connections.py:
		Este arquivo, apenas configura as conexões dos bancos de dados suportados.
"""
from cqlengine import connection
from elasticsearch_dsl.connections import connections

es_connect=connections.create_connection(hosts=['localhost'])
cql_connect=connection.setup(["127.0.0.1"], "simbiose_challenge")

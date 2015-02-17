# SyncDB (Sincronização  entre  ElasticSearch  e  Cassandra)

#### Sobre:

Descrição:
* Desafio Técnico (https://www.dropbox.com/s/k6lf1c4greuirqs/Desafio_T%C3%A9cnico_Simbiose_Sincroniza%C3%A7%C3%A3o_ElasticSearch_Cassandra.pdf)

Módulos:
* Cassandra-Driver (https://github.com/datastax/python-driver)
* Cqlengine (https://cqlengine.readthedocs.org)
* ElasticSearch-Py (http://www.elasticsearch.org/guide/en/elasticsearch/client/python-api/current/)
* Elasticsearch DSL (http://elasticsearch-dsl.readthedocs.org/)

Banco de dados suportados (até o momento):
* ElasticSearch
* Cassandra

# Instalação 
* Python
    * Versão: 2.7.x;
    * Se você não tiver os módulos, basta "rodar" na sua linha de comando `` sudo pip install -r requirements.txt ``
* Cassandra
    * http://cassandra.apache.org/
    * http://cassandra.apache.org/download/
    * https://wiki.apache.org/cassandra/GettingStarted
    * *Nota:* não esqueça de criar uma keyspace no Cassandra `` CREATE KEYSPACE simbiose_challenge `` (http://www.datastax.com/documentation/cql/3.0/cql/cql_reference/create_keyspace_r.html)
* ElastichSearch
    * http://www.elasticsearch.org/
    * http://www.elasticsearch.org/overview/elkdownloads/
    * http://www.elasticsearch.org/guide/en/elasticsearch/guide/current/getting-started.html
    
# Getting Started 

1. Para iniciar (start) `` sudo python sync_daemon.py start``
    * Parar (stop)  `` sudo python sync_daemon.py stop``
    * Reiniciar (restart)  `` sudo python sync_daemon.py restart``
2. `` python start_test.py `` 
    * Dentro desde arquivo (`` start_test.py ``), tem alguns exemplos de como fazer *insert's*, *get's*, *updated's*;
3. (Final) Abra os 2 bancos de dados, e eles estação sincronizados.
    * ***Sugestão***:
        *  Para "abrir" o Cassandra, o próprio cqlsh, já é de bom uso;
        *  Para o Elastic, a sugestão é o Postman - REST Client (http://www.getpostman.com/), extenção do Google Chrome, porém ele roda como aplicativo fora do browser;

# Executando o SyncDB
1. Depois de ter feito o teste, ele estará executando na forma de "daemon", ou seja, o SyncDB verifica periodicamente as alterações no banco (padrão: 10 segundos), porém caso queira que rode em determinado tempo, apenas mude os segundos em sycn_daemon.py (`` daemon_app = DaemonApp(10) ``), ao invés de 10, coloque o tempo desejado(em segundos);

# Leia Mais
* https://elasticsearch-py.readthedocs.org/en/master/api.html?highlight=get#elasticsearch.Elasticsearch.get
* http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/docs-update.html
* https://elasticsearch-py.readthedocs.org/en/master/
* https://github.com/elasticsearch/elasticsearch-py
* https://elasticsearch-py.readthedocs.org/en/master/api.html?highlight=update#elasticsearch.Elasticsearch.update
* https://pypi.python.org/pypi/python-daemon/
* http://nanvel.name/weblog/python-unix-daemon/
* http://www.jejik.com/articles/2007/02/a_simple_unix_linux_daemon_in_python/
* http://planetcassandra.org/getting-started-with-cassandra-and-python/
* https://datastax.github.io/python-driver/installation.html
* http://joelabrahamsson.com/elasticsearch-101/
* http://www.datastax.com/documentation/developer/python-driver/1.0/common/drivers/introduction/introArchOverview_c.html
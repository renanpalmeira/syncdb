#!/usr/bin/env python
# -*- coding: utf8 -*-

import os
import time
from datetime import datetime
from daemon import runner
from syncdb import SyncDB
from models import Cassandra, ElasticSearch

"""
    Class DaemonApp:
        Responsável por todas as configurações parar "rodar" o syncdb.py em forma de daemon.
"""
class DaemonApp():
    def __init__(self, time_daemon=int(10)):
        if time_daemon<5:
            self.time_daemon=int(5)
        self.time_daemon=int(time_daemon)
        # Variáveis para controle interno do daemon.
        self.stdin_path = '/dev/null'
        self.stdout_path = '/dev/tty'
        self.stderr_path = '/dev/tty'
        self.pidfile_path = '/var/run/syncdb_daemon.pid'
        self.pidfile_timeout = 5
    """
        Função sync_log:
            Apenas escritas os retornos da sincronização e salva em um arquivo de log temporário.
    """
    def sync_log(self, log_text=str()):
        content="%s - %s" % (datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S'), log_text)
        filepath = '/tmp/syncdb_daemon/syncdb.log'
        dirpath = os.path.dirname(filepath)
        if not os.path.exists(dirpath) or not os.path.isdir(dirpath):
            os.makedirs(dirpath)
        f = open(filepath, 'w')
        f.write(content)
        f.close()
    """
        Quando o comando sudo python syncdb_daemon.py start é executado:
            Importa o arquivo connections, nesse arquivo está presente, todos os bancos suportados. 
            Após o "import" a Sincronização entre os bancos inicia, que verifica a cada 10 (por padrão) segundos as alterações nos bancos.
    """
    def run(self):
        while True:
            import connections
            cql=Cassandra()
            es=ElasticSearch()
            sync=SyncDB(cql=cql, es=es)
            sync_result=sync.run()
            self.sync_log(sync_result)     
            if type(self.time_daemon) is int:
                time.sleep(self.time_daemon)
            else:
                time.sleep(10)

"""
    Quando o comando sudo python sync_daemon.py:
        Algumas rotinas (start, stop, restart) estão a disposição.
"""
if __name__=='__main__':
    daemon_app = DaemonApp(10)
    runnerd = runner.DaemonRunner(daemon_app)
    result = runnerd.do_action()
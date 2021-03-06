"""
File: consumer.py
Data creazione: 2019-02-13

<descrizione>

Licenza: Apache 2.0

Copyright 2019 AlphaSix

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

Versione: 0.1.0
Creatore: Timoty Granziero, timoty.granziero@gmail.com
Autori:
    <nome cognome, email>
    <nome cognome: email>
    ....
"""

# from kafka import KafkaConsumer
# import kafka.errors
from abc import ABC, abstractmethod
# import json
# from pathlib import Path

class Consumer(ABC):
    """Interfaccia Consumer"""

    @abstractmethod
    def listen(self):
        """Resta in ascolto del Broker"""
        pass

    @abstractmethod
    def send(self):
        """Invia il messaggio all'utente finale."""
        pass

# TP NEO4J avec Docker

## Installation de NEO4J avec Docker

1. Récupérez la dernière image Docker de NEO4J :

```bash
docker pull neo4j:latest
```
2.  Démarrer un conteneur Neo4j

```bash
docker run --name my-neo4j -p 7474:7474 -p 7687:7687 -d --env NEO4J_AUTH=neo4j/strongPassword neo4j:latest
```
3.  [Accéder à l'interface Neo4j](http://localhost:7474/browser/preview/)


4.  installation de la bibliothèque Neo4j pour Python

```bash
pip install neo4j 
```
5.  Exécuter mon script

```bash
python main.py
```
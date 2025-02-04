from neo4j import GraphDatabase

uri = "bolt://localhost:7687"
user = "neo4j"
password = "strongPassword"  # Remplace avec ton mot de passe

driver = GraphDatabase.driver(uri, auth=(user, password))

def run_query(query):
    with driver.session() as session:
        result = session.run(query)
        return [record for record in result]  # Retourne les résultats sous forme de liste

person1 = "CREATE (p:Person {name: 'Alice', age: 30})"
person2 = "CREATE (p:Person {name: 'Bob', age: 25})"
person3 = "CREATE (p:Person {name: 'Charlie', age: 35})"

run_query(person1)
run_query(person2)
run_query(person3)

relationship1 = "MATCH (a:Person {name: 'Alice'}), (b:Person {name: 'Bob'}) CREATE (a)-[:FRIEND]->(b)"
relationship2 = "MATCH (a:Person {name: 'Alice'}), (b:Person {name: 'Charlie'}) CREATE (a)-[:FRIEND]->(b)"
relationship3 = "MATCH (a:Person {name: 'Bob'}), (b:Person {name: 'Charlie'}) CREATE (a)-[:FRIEND]->(b)"

run_query(relationship1)
run_query(relationship2)
run_query(relationship3)


query_all_persons = "MATCH (p:Person) RETURN p.name, p.age"

results = run_query(query_all_persons)

for record in results:
    print(f"Name: {record['p.name']}, Age: {record['p.age']}")
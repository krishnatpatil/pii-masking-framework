import json
import argparse
import pprint
from collections import deque, defaultdict

# Example schema information
schema = {
    "tables": ["table1", "table2", "table3"],
    "columns": {
        "table1": ["id", "name", "table2_id"],
        "table2": ["id", "description", "table3_id"],
        "table3": ["id", "details"],
    },
    "foreign_keys": [
        {
            "from_table": "table1",
            "from_column": "table2_id",
            "to_table": "table2",
            "to_column": "id",
        },
        {
            "from_table": "table2",
            "from_column": "table3_id",
            "to_table": "table3",
            "to_column": "id",
        },
    ],
}


def build_schema_graph(schema):
    graph = defaultdict(list)
    for fk in schema["foreign_keys"]:
        graph[fk["from_table"]].append(
            (fk["to_table"], fk["from_column"], fk["to_column"])
        )
        graph[fk["to_table"]].append(
            (fk["from_table"], fk["to_column"], fk["from_column"])
        )
    pprint.pprint(graph)
    return graph


def find_shortest_path(graph, start, end):
    queue = deque([(start, [])])
    visited = set()

    while queue:
        current, path = queue.popleft()

        if current in visited:
            continue

        visited.add(current)
        print("***************************************")
        new_path = path + [current]
        pprint.pprint(new_path)
        print("***************************************")
        if current == end:
            return new_path

        for neighbor, _, _ in graph[current]:
            if neighbor not in visited:
                queue.append((neighbor, new_path))

    return None


def generate_select_query(path, schema, select_columns):
    select_clause = "SELECT "
    from_clause = f"FROM {path[0]}"
    join_clause = ""

    # Process columns
    columns = []
    for table, cols in select_columns.items():
        for col in cols:
            columns.append(f"{table}.{col}")
    select_clause += ", ".join(columns)

    # Process joins
    for i in range(len(path) - 1):
        current_table = path[i]
        next_table = path[i + 1]
        for fk in schema["foreign_keys"]:
            if (fk["from_table"] == current_table and fk["to_table"] == next_table) or (
                fk["from_table"] == next_table and fk["to_table"] == current_table
            ):
                join_clause += f" JOIN {next_table} ON {current_table}.{fk['from_column']} = {next_table}.{fk['to_column']}"
                break

    # Combine clauses to form the final query
    query = f"{select_clause} {from_clause} {join_clause}"
    return query


def main(config_file):
    with open(config_file, "r") as file:
        config = json.load(file)

    schema_graph = build_schema_graph(config["schema"])
    path = find_shortest_path(schema_graph, config["start_table"], config["end_table"])

    if path:
        query = generate_select_query(path, config["schema"], config["select_columns"])
        print(query)
    else:
        print("No path found between the specified tables.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate SQL SELECT statement by finding the shortest path between tables"
    )
    parser.add_argument("config_file", type=str, help="Path to the configuration file")
    args = parser.parse_args()
    main(args.config_file)

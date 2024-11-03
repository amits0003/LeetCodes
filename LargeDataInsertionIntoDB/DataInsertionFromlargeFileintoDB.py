import psycopg2
import psycopg2.extras


# Function to process large file and insert in chunks
def process_large_file_and_insert(file_path, conn, chunk_size=1024):
    with open(file_path, 'r') as file:
        data_chunk = []
        for line in file:
            # Process each line and prepare data (example split by comma)
            data = line.strip().split(',')
            data_chunk.append(data)

            # If chunk size is reached, insert data into the DB
            if len(data_chunk) >= chunk_size:
                bulk_insert_to_db(data_chunk, conn)
                data_chunk = []

        # Insert any remaining data
        if data_chunk:
            bulk_insert_to_db(data_chunk, conn)


# Bulk insert function using psycopg2
def bulk_insert_to_db(data, conn):
    with conn.cursor() as cursor:
        insert_query = "INSERT INTO my_table (column1, column2) VALUES %s"
        psycopg2.extras.execute_values(cursor, insert_query, data)
        conn.commit()


# Example usage
conn = psycopg2.connect(database="mydb", user="myuser", password="mypassword", host="localhost", port="5432")

process_large_file_and_insert('large_file.txt', conn)
conn.close()

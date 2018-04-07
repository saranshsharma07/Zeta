import boto3
import psycopg2


client = boto3.client(
    's3',
    aws_access_key_id='aws_access_key_id',
    aws_secret_access_key='aws_secret_access_key'
)

connection = psycopg2.connect(
    "host={0} dbname={1} user={2} password={3} port={4}".format(
        "localhost",
        'db_name',
        'user_name',
        'password',
        'port'
    )
)

query ='''CREATE TABLE public.test
          (
           id int,
           name varchar(255) 
          );'''

cursor = connection.cursor()
cursor.execute(query)
cursor.execute('COMMIT')

schema='public'
table='test'
file_path = 's3 path'
aws_access_key_id='aws_access_key_id'
aws_secret_access_key='aws_secret_access_key'

sql="""copy {}.{} from '{}'\
        credentials \
        'aws_access_key_id={};aws_secret_access_key={}' \
        DELIMITER ',' ACCEPTINVCHARS EMPTYASNULL ESCAPE COMPUPDATE OFF;commit;"""\
        .format(schema, table, file_path, aws_access_key_id, aws_secret_access_key)
cursor.execute(sql)
cursor.execute('end transaction')


import boto3
import pandas as pd
import os

BUCKET_NAME = os.environ['BUCKET_NAME']
file_name = 'datos.csv'

s3 = boto3.client('s3',
                  aws_access_key_id=os.environ['AWS_ACCESS_KEY'],
                  aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY']
                  )
obj = s3.get_object(Bucket= BUCKET_NAME, Key= file_name)

df = pd.read_csv(obj['Body'])

df_agrup = df.groupby(['segmento', 'categoria']).size().reset_index(name="Casos")
segmento = df['segmento'].unique()


def label_by_segment(segment):
    return df[df['segmento'] == segment]['label']

def fecha_by_segment(segment):
    return df[df['segmento'] == segment]['fecha']


def categ_by_segment(segment):
    return df_agrup[df_agrup['segmento'] == segment]['categoria']

def casos_by_segment(segment):
    return df_agrup[df_agrup['segmento'] == segment]['Casos']
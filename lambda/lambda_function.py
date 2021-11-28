# Masukan dependency Boto3 yang merupakan AWS SDK untuk Python dan OS untuk mengambil environment variable
import boto3, os

# Ambil informasi Region dan Instance ID environment variable
region = os.environ['Region']
instances = os.environ['InstanceId']
# Beberapa Instance ID yang diambil akan dirubah menjadi array
instances = instances.split(",")

# Menggunakan Boto3 agar aplikasi bisa komunikasi dengan service AWS di Region yang dipilih
ec2 = boto3.client('ec2', region_name=region)

# Fungsi main/default dari Lambda function
def lambda_handler(event, context):
# Mencoba mematikan beberapa Instance sesuai dengan jumlah Instance ID yang dikoleksi
  for instance in instances:
    try:
      ec2.stop_instances(InstanceIds=[instance])
# Simpan kedalam CloudWatch Log hasil dari eksekusi
      print('You have stopped an EC2 instance: ' + instance)
    except:
      print('You failed to stop an EC2 instance: ' + instance)

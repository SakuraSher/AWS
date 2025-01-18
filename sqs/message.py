import boto3
from  que_ue import createqueue

def createandgetmessage():
    try:
      print('Iam here')
      sqs = createqueue()
      readqueue = sqs.get_queue_by_name(QueueName='test')
      print(readqueue)
      enterstring = input('please enter the string that you want to transfer')
      response =readqueue.send_message(MessageBody=enterstring)
      print(response)
    except:
      print('errored')


if __name__ == '__main__':
    createandgetmessage()

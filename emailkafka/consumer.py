from confluent_kafka import Consumer

consumer=Consumer({
    'bootstrap.servers':'pkc-3w22w.us-central1.gcp.confluent.cloud:9092',
    'security.protocol':'SASL_SSL',
    'sasl.username':'SSVTF2RIAN2EPPYF',
    'sasl.password':'NEEByf0Pq34qzjVnLpwbVKmHSWAbo6Ka+5pM4ScACe0CZlc/nnVh0Mime9eKS/0c',
    'sasl.mechanism':'PLAIN',
    'group.id':'myGroup',
    'auto.offset.reset':'earliest'
})

consumer.subscribe(['default'])

while True:
    msg=consumer.poll(1.0)
    if msg is None:
        continue
    if msg.error():
        print("Consumer error: {}".format(msg.error()))
        continue
    print("Received message: {}".format(msg.value()))
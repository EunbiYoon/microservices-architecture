from confluent_kafka import Producer

producer=Producer({
    'bootstrap.servers':'pkc-3w22w.us-central1.gcp.confluent.cloud:9092',
    'security.protocol':'SASL_SSL',
    'sasl.username':'SSVTF2RIAN2EPPYF',
    'sasl.password':'NEEByf0Pq34qzjVnLpwbVKmHSWAbo6Ka+5pM4ScACe0CZlc/nnVh0Mime9eKS/0c',
    'sasl.mechanism':'PLAIN'
})
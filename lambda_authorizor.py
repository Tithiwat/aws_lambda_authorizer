# ---
# DemoAuthorizer
# ---
def lambda_handler(event, context):
    
    #1 - Log the event
    print('*********** The event is: ***************')
    print(event)
    
    #2 - See if the person's token is valid
    if event['authorizationToken'] == 'abc123':
        auth = 'Allow'
    else:
        auth = 'Deny'
    
    #3 - Construct and return the response
    authResponse = { "principalId": "abc123", "policyDocument": { "Version": "2012-10-17", "Statement": [{"Action": "execute-api:Invoke", "Resource": ["arn:aws:execute-api:YOUR_AWS_REGION:YOUR_ACCOUNTNUMBER:2ogoj2ul12/test/GET/customers"], "Effect": auth}] }}
    return authResponse

# Things that I assume

Read from SQL database data will all correct, do not have missing value or missing foreign key. For real life project, I would handle more edge cases and learn how is the data generated in db.

## Thing to be improved if deploy application on cloud

1. Better response messages, such as empty resource using search;
2. Add caching for state, like redis or dynamodb. And logic handle syncing cache and db;
3. User service and authentication service using Cognito;
4. More endpoint on messages, enable user to create, update and delete message as well;
5. More unit tests;
6. Dockerize application and build CI/CD pipeline, using terraform for example;
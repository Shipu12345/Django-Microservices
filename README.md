# Django-Microservices
There will be an auth service and a business service. They will communicate with each other with JWT token.


Prerequisites:

    1. docker
    2. docker-compose
    3. python3


Getting Started:

    1. Clone the repository
    2. Open the terminal and move to the Django-Microservices folder
    3. Run: `sudo chmod +x ./bin/deploy.sh`
    4. Run: `./bin/deploy.sh`

APIs:

    AUTH: There Are Login, Register, Refresh Token, Token Verify, Logout, Get User Details Apis.

    Business: There are only one Api, Get Stores. Which returns all the stores within a Certain Range.

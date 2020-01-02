### In progress

- Drop support for python 3.4
- Added support for [`orders`](https://www.culqi.com/api/#/ordenes)
- Added complete set of tests

##### Breaking changes

- Complete refactor in API Client
- Use Client class instead to configure module directly

##### Development environment

- Moved to [poetry](https://poetry.eustace.io) for dependency management
- Use of [black](https://black.readthedocs.io/en/stable/) for linting
- Use of [tox](https://tox.readthedocs.io/en/latest/) for testing environments
- Added precomit hooks with [pre-comit](https://pre-commit.com/)
- Added code [coverage](https://coverage.readthedocs.io/en/stable/)

### 0.2.5 22-02-2017

- Change the default timeout of GET method 120 to 360
- rename COD_COMMERCE to public_key and API_KEY to secret_key

### 0.2.3 13-02-2017

- Fix capture method in Charge

### 0.2.2 13-02-2017

- Add Card
- Add Customer
- Add Event
- Add Transfer
- Add update method

### 0.2.1 26-01-2017

- Add: LIST, GET, DELETE for each Resource

### 0.1.8 17-01-2017

- Fix Create Token

### 0.1 05-01-2017

- Create Token
- Create Charge
- Create Plan
- Create Subscription
- Create Refund
- Unit Tests

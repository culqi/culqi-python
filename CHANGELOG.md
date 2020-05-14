### 1.0.4 In progress

- Support for python 3.8.x
- Updated dependecies
- Fixed conflict with pylint E1101 (no-member) error message
- Added tests for distinct cards
- Added tests for error responses

### 1.0.0 to 1.0.3 03-01-2020

- Drop support for python 3.4
- Added complete set of tests
- Added support for [`orders`](https://www.culqi.com/api/#/ordenes)
- Complete refactor in API Client
- Use Client class instead to configure module directly
- Moved to [poetry](https://poetry.eustace.io) for dependency management
- Use of [black](https://black.readthedocs.io/en/stable/) for linting
- Use of [tox](https://tox.readthedocs.io/en/latest/) for testing environments
- Added precomit hooks with [pre-comit](https://pre-commit.com/)
- Added code [coverage](https://coverage.readthedocs.io/en/stable/)
- Developer friendly nomneclature

### 0.2.5 22-02-2017

- Change the default timeout of GET method 120 to 360
- rename COD_COMMERCE to public_key and API_KEY to private_key

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

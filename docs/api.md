# Buber Dinner API

- [Buber Dinner API](#buber-dinner-api)
  - [Auth](#auth)
    - [Register](#register)
      - [Register Request](#register-request)
      - [Register Response](#register-response)
    - [Login](#login)
      - [Login Request](#login-request)
      - [Login Response](#login-response)

## Auth

### Register

```js
POST {{host}}/auth/register
```

#### Register Request

```json
{
  "first_name": "John",
  "last_name": "Doe",
  "email": "john.doe@email.com",
  "password": "jd123"
}
```

#### Register Response

```js
200 OK
```

```json
{
  "id": "00000000-0000-0000-0000-000000000000",
  "first_name": "John",
  "last_name": "Doe",
  "email": "john.doe@email.com",
  "token": "00000000-0000-0000-0000-000000000000"
}
```

### Login

```js
POST {{host}}/auth/login
```

#### Login Request

```json
{
    "email": "john.doe@email.com",
    "password": "jd123"
}
```

#### Login Response
```js
200 OK
```

```json
{
  "id": "00000000-0000-0000-0000-000000000000",
  "first_name": "John",
  "last_name": "Doe",
  "email": "john.doe@email.com",
  "token": "00000000-0000-0000-0000-000000000000"
}
```
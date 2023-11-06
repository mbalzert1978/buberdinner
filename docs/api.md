# Buber Dinner API

- [Buber Dinner API](#buber-dinner-api)
  - [Auth](#auth)
    - [Register](#register)
      - [Register Request](#register-request)
      - [Register Response](#register-response)

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
  "id": "d89c2d0a-eb3e-4075-95ff-b920b55aa104",
  "first_name": "John",
  "last_name": "Doe",
  "email": "john.doe@email.com"
}
```

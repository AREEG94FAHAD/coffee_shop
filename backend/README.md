# Coffee Shop Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) are libraries to handle the lightweight sqlite database. Since we want you to focus on auth, we handle the heavy lift for you in `./src/database/models.py`. We recommend skimming this code first so you know how to interface with the Drink model.

- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

## Running the server

From within the `./src` directory first ensure you are working using your created virtual environment.

Each time you open a new terminal session, run:

```bash
export FLASK_APP=api.py;
```

To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.

## Tasks

### Setup Auth0

1. Create a new Auth0 Account
2. Select a unique tenant domain
3. Create a new, single page web application
4. Create a new API
    - in API Settings:
        - Enable RBAC
        - Enable Add Permissions in the Access Token
5. Create new API permissions:
    - `get:drinks-detail`
    - `post:drinks`
    - `patch:drinks`
    - `delete:drinks`
6. Create new roles for:
    - Barista
        - can `get:drinks-detail`
    - Manager
        - can perform all actions
7. Test your endpoints with [Postman](https://getpostman.com). 
    - Register 2 users - assign the Barista role to one and Manager role to the other.
    - Sign into each account and make note of the JWT.
    - Import the postman collection `./starter_code/backend/udacity-fsnd-udaspicelatte.postman_collection.json`
    - Right-clicking the collection folder for barista and manager, navigate to the authorization tab, and including the JWT in the token field (you should have noted these JWTs).
    - Run the collection and correct any errors.
    - Export the collection overwriting the one we've included so that we have your proper JWTs during review!

### Implement The Server

There are `@TODO` comments throughout the `./backend/src`. We recommend tackling the files in order and from top to bottom:

1. `./src/auth/auth.py`
2. `./src/api.py`

## API Reference

### Getting Started

Base URL: At present this app can only be run locally and is not hosted as a base URL. The backend app is hosted at the default, http://127.0.0.1:5000/, which is set as a proxy in the frontend configuration. Authentication: This version of the application does  require authentication.

### Error Handling
Errors are returned as JSON objects in the following format:

The API will return four error types when requests fail:

 1. 404: resource not found

 ```
 {
    "success": False, 
    "error": 404,
    "message": "resource not found"
}
 ```

 2. 422: Not Processable

 ```
 {
     "success":False,
     "error":422,
     "message": "unprocessable"
}
 ```
 3. Unauthorized

 ```
 {
    "success": False, 
    "error": 401,
    "message": "Unauthorized"
}
 ```
 4. Forbidden
 ```
 {
    "success": False, 
    "error": 403,
    "message": "Forbidden"
}
 ```

### Endpoints

#### [hi baby](### GET '/drinks')
#### GET '/drinks-detail' require permission 
'get:drinks-detail'
#### POST '/drinks' require permission 
'post:drinks'
#### PATCH '/drinks/<drink_id>' require permission 
'patch:drinks'
#### DELETE '/drinks/<drink_id>' require permission 
'delete:drinks'

### GET '/drinks'
'curl http://127.0.0.1:5000/drinks'

```
{
  "drinks": [
    {
      "id": 1,
      "recipe": [
        {
          "color": "green",
          "parts": 1
        },
        {
          "color": "yellow",
          "parts": 1
        },
        {
          "color": "red",
          "parts": 1
        },
        {
          "color": "orange",
          "parts": 1
        },
        {
          "color": "black",
          "parts": 1
        }
      ],
      "title": "azbri"
    },
    {
      "id": 2,
      "recipe": [
        {
          "color": "orange",
          "parts": 5
        },
        {
          "color": "red",
          "parts": 1
        },
        {
          "color": "pink",
          "parts": 1
        },
        {
          "color": "black",
          "parts": 1
        }
      ],
      "title": "Udacity coffee"
    },
    {
      "id": 3,
      "recipe": [
        {
          "color": "white",
          "parts": 1
        },
        {
          "color": "red",
          "parts": 1
        },
        {
          "color": "blue",
          "parts": 1
        }
      ],
      "title": "russa"
    }
  ],
  "success": true
}
```
### GET '/drinks-detail' require permission 
'get:drinks-detail'

'curl -H "Authorization: bearer  <ACCESS_TOKEN>" http://www.example.com'

- Example

`curl -H "Authorization: bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik5Rcm1wQW1sNzZPQ2FvMWlRa1BITSJ9.eyJpc3MiOiJodHRwczovL2FyZWVnLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWI0MDljYTZiNjliYzBjMTJmZjFkNjMiLCJhdWQiOiJpbWFnZSIsImlhdCI6MTU4OTcyNTY0OCwiZXhwIjoxNTg5NzMyODQ4LCJhenAiOiJqcDBKMGdqUEdNbndIcWQ5UDhNSzNaZWJjNE9ocTJwUCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmRyaW5rcyIsImdldDpkcmlua3MtZGV0YWlsIiwicGF0Y2g6ZHJpbmtzIiwicG9zdDpkcmlua3MiXX0.L-fo09e31ze74_xMIUOQKOEPA67XVxPFsqb_2wqpNQRvrHt1lykEIShcRJqYCi8rNJouYEhO5KE_5scatJvCI1VtrVpuIT_wwP7J8ty-K1npUZ0FWMQnJgT84JfdWIze4ZES20Ly2EwqfUya3-9w4J4nXLJztPdwKFN2VDVLif18rdExLyNLR3E5cIeirmDtE9BQ8XFh9A7NjWyb_YTcEGrZA8Fyw5DuoXfor51ab2HbRfo9wu7iw1--2p0uFktvwn_9rWFhmxNEkT34BU7QlJZPnL9a56Q9sfon3a1pvwKBpxYZr5QmRzNDHrbGy-0-y4yL6qWuBqjAqE41Eq8k9w" http://127.0.0.1:5000/drinks-detail`


```
{
  "drinks": [
    {
      "id": 1,
      "recipe": [
        {
          "color": "green",
          "name": "",
          "parts": 1
        },
        {
          "color": "yellow",
          "name": "",
          "parts": 1
        },
        {
          "color": "red",
          "name": "",
          "parts": 1
        },
        {
          "color": "orange",
          "name": "",
          "parts": 1
        },
        {
          "color": "black",
          "name": "",
          "parts": 1
        }
      ],
      "title": "azbri"
    },
    {
      "id": 2,
      "recipe": [
        {
          "color": "orange",
          "name": "",
          "parts": 5
        },
        {
          "color": "red",
          "name": "",
          "parts": 1
        },
        {
          "color": "pink",
          "name": "",
          "parts": 1
        },
        {
          "color": "black",
          "name": "",
          "parts": 1
        }
      ],
      "title": "Udacity coffee"
    },
    {
      "id": 3,
      "recipe": [
        {
          "color": "white",
          "name": "",
          "parts": 1
        },
        {
          "color": "red",
          "name": "",
          "parts": 1
        },
        {
          "color": "blue",
          "name": "",
          "parts": 1
        }
      ],
      "title": "russa"
    }
  ],
  "success": true
}
```

### POST '/drinks' require permission 
'post:drinks'
`curl -H "Authorization: bearer <token>  http://127.0.0.1:5000/drinks -X POST -H "Content-Type: application/json" -d '{"title":"jjj","recipe":[{"name": "k","color": "pink", "parts": 2}]}'`


-Example
`curl -H "Authorization: bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik5Rcm1wQW1sNzZPQ2FvMWlRa1BITSJ9.eyJpc3MiOiJodHRwczovL2FyZWVnLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWI0MDljYTZiNjliYzBjMTJmZjFkNjMiLCJhdWQiOiJpbWFnZSIsImlhdCI6MTU4OTc0NTQzNywiZXhwIjoxNTg5NzUyNjM3LCJhenAiOiJqcDBKMGdqUEdNbndIcWQ5UDhNSzNaZWJjNE9ocTJwUCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmRyaW5rcyIsImdldDpkcmlua3MtZGV0YWlsIiwicGF0Y2g6ZHJpbmtzIiwicG9zdDpkcmlua3MiXX0.t-CLvJx0zc28MiN9O9q8fwOS4Plqgn8evWa8EKTchE7HmX54rK_J8Y55n8q888x1I6iXsZ6KIqZ0x9FvU3NSP8Xhh974wuZdvxED2yHDeESe3qX8QEycIS9BYmvKhmFgnS9d2a1YmSgABLltr2wTIVMkIgj8pDyqivncFR1m8iLgFodgpGmrczpZdvjwZZeIxF3nbios5o5nQHuhAllkfuLPALuB6h0jT1PYXtE_QFFDs8vfLvjiNitXsMgFe36e-45fSS_9-kSRqSG-DA_NjCy9fByWwArBjXEfRQLIw8hLaBm7EgFT-K4zAIHGlQV7laUwuSO7r1mH8d971kposQ" http://127.0.0.1:5000/drinks -X POST -H "Content-Type: application/json" -d '{"title":"jjj","recipe":[{"name": "k","color": "pink", "parts": 2}]}'`

```
{
  "drinks": [
    {
      "id": 1, 
      "recipe": [
        {
          "color": "green", 
          "name": "k", 
          "parts": 2
        }
      ], 
      "title": "jjjj"
    }, 
    {
      "id": 2, 
      "recipe": [
        {
          "color": "orange", 
          "name": "", 
          "parts": 5
        }, 
        {
          "color": "red", 
          "name": "", 
          "parts": 1
        }, 
        {
          "color": "pink", 
          "name": "", 
          "parts": 1
        }, 
        {
          "color": "black", 
          "name": "", 
          "parts": 1
        }
      ], 
      "title": "Udacity coffee"
    }, 
    {
      "id": 3, 
      "recipe": [
        {
          "color": "white", 
          "name": "", 
          "parts": 1
        }, 
        {
          "color": "red", 
          "name": "", 
          "parts": 1
        }, 
        {
          "color": "blue", 
          "name": "", 
          "parts": 1
        }
      ], 
      "title": "russa"
    }, 
    {
      "id": 4, 
      "recipe": [
        {
          "color": "pink", 
          "name": "k", 
          "parts": 2
        }
      ], 
      "title": "jjj"
    }, 
    {
      "id": 5, 
      "recipe": [
        {
          "color": "pink", 
          "name": "k", 
          "parts": 2
        }
      ], 
      "title": "jjooj"
    }
  ], 
  "success": true
}
```


### PATCH '/drinks/<drink_id>' require permission 
'patch:drinks'

`curl -H "Authorization: bearer <token>  http://127.0.0.1:5000/drinks/1 -X PATCH -H "Content-Type: application/json" -d '{"title":"jjj","recipe":[{"name": "k","color": "pink", "parts": 2}]}'`

-Example
`curl -H "Authorization: bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik5Rcm1wQW1sNzZPQ2FvMWlRa1BITSJ9.eyJpc3MiOiJodHRwczovL2FyZWVnLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWI0MDljYTZiNjliYzBjMTJmZjFkNjMiLCJhdWQiOiJpbWFnZSIsImlhdCI6MTU4OTczNjA3MywiZXhwIjoxNTg5NzQzMjczLCJhenAiOiJqcDBKMGdqUEdNbndIcWQ5UDhNSzNaZWJjNE9ocTJwUCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmRyaW5rcyIsImdldDpkcmlua3MtZGV0YWlsIiwicGF0Y2g6ZHJpbmtzIiwicG9zdDpkcmlua3MiXX0.Ywoe54ttAxguNRpKF5bSg-aUwLiJUlONBbDrIPcX9BdXN3t21L8gAgDeCoHFbjgBaU_7kx_WWO6oOuagMQ2DnSkn7Ka4NtfPXg_RHH25T3CZzuAm6nt5_65h8T7GHeSbx9wpPOtfeTQ5ZgjCOe57Zk5wLjAergt5deo7UKXoYVtTvtruUkRNoKVxlUyzzaqFC43Fw6jzuyILW4WYFwJNeZFXHm97LFv23V47AzGOf0oMBk6Tx8dUjWkSr5B-QdoE8LWzw0seijL5M09Y8oYqrXMZDoswLtQ6j7aa0FbnhKpVojjE5KGC00OrS6zdsTJsX8oTi6jR8xI6cmByvTYq0g" http://127.0.0.1:5000/drinks/1 -X PATCH -H "Content-Type: application/json" -d '{"title":"jjjj","recipe":[{"name": "k","color": "green", "parts": 2}]}'`

```
{
  "drinks": [
    {
      "id": 1, 
      "recipe": [
        {
          "color": "green", 
          "name": "k", 
          "parts": 2
        }
      ], 
      "title": "jjjj"
    }, 
    {
      "id": 2, 
      "recipe": [
        {
          "color": "orange", 
          "name": "", 
          "parts": 5
        }, 
        {
          "color": "red", 
          "name": "", 
          "parts": 1
        }, 
        {
          "color": "pink", 
          "name": "", 
          "parts": 1
        }, 
        {
          "color": "black", 
          "name": "", 
          "parts": 1
        }
      ], 
      "title": "Udacity coffee"
    }, 
    {
      "id": 3, 
      "recipe": [
        {
          "color": "white", 
          "name": "", 
          "parts": 1
        }, 
        {
          "color": "red", 
          "name": "", 
          "parts": 1
        }, 
        {
          "color": "blue", 
          "name": "", 
          "parts": 1
        }
      ], 
      "title": "russa"
    }, 
    {
      "id": 4, 
      "recipe": [
        {
          "color": "pink", 
          "name": "k", 
          "parts": 2
        }
      ], 
      "title": "jjj"
    }
  ], 
  "success": true
}
```

### DELETE '/drinks/<drink_id>' require permission 
'delete:drinks'

`curl -H "Authorization: bearer <token>  http://127.0.0.1:5000/drinks/1 -X DELETE -H "Content-Type: application/json" -d '{"title":"jjj","recipe":[{"name": "k","color": "pink", "parts": 2}]}'`

- Example
`curl -H "Authorization: bearer eyJhbGciOi
JSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik5Rcm1wQW1sNzZPQ2FvMWlRa1BITSJ9.eyJpc3MiOiJodHRwczovL2FyZWVnLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWI0MDljY
TZiNjliYzBjMTJmZjFkNjMiLCJhdWQiOiJpbWFnZSIsImlhdCI6MTU4OTc0NTQzNywiZXhwIjoxNTg5NzUyNjM3LCJhenAiOiJqcDBKMGdqUEdNbndIcWQ5UDhNSzNaZWJjNE9ocTJwU
CIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmRyaW5rcyIsImdldDpkcmlua3MtZGV0YWlsIiwicGF0Y2g6ZHJpbmtzIiwicG9zdDpkcmlua3MiXX0.t-CLvJx0zc28M
iN9O9q8fwOS4Plqgn8evWa8EKTchE7HmX54rK_J8Y55n8q888x1I6iXsZ6KIqZ0x9FvU3NSP8Xhh974wuZdvxED2yHDeESe3qX8QEycIS9BYmvKhmFgnS9d2a1YmSgABLltr2wTIVMkI
gj8pDyqivncFR1m8iLgFodgpGmrczpZdvjwZZeIxF3nbios5o5nQHuhAllkfuLPALuB6h0jT1PYXtE_QFFDs8vfLvjiNitXsMgFe36e-45fSS_9-kSRqSG-DA_NjCy9fByWwArBjXEfR
QLIw8hLaBm7EgFT-K4zAIHGlQV7laUwuSO7r1mH8d971kposQ" http://127.0.0.1:5000/drinks/1 -X DELETE`

```
{
  "delete": "1", 
  "success": true
}
```

# Author AREEG FAHAD  
#### M.S in Newtwork Engineering Al-Nahrain University
#### B.A in Network Engineering Al-Iraqi University 

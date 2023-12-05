## Endpoints needed


Create CustomerTicket, Create Menu Items, Create Waiters,

URL/path            | HTTP Method | Description                                                         | Payload
---------           | ----------- | ------------------------------------------------------------------- | ----
ticket              | POST        | Creates a new ticket
ticket              | GET         | Gets all customer tickets
menu item           | POST        | Creates a new menu item
menu item           | GET         | Gets all menu items
waiter              | POST        | Creates a new waiter
waiter              | GET         | Gets all waiters

ticket/total        | POST        | Gets the total sum for menu items of a given table                 | `{table_id:int}`
total_revenue       | GET         | Gets the total revenue from all items on customer tickets


## Requests

### Hello World
```rest
GET http://127.0.0.1:5000 HTTP/1.1
```

### Ticket Total Test
```rest
POST http://127.0.0.1:5000/ticket/total HTTP/1.1
content-type: application/json

{
    "table_id": 10
}
```

### Total Revenue

```rest
GET http://127.0.0.1:5000/total-revenue HTTP/1.1
```

### Waiter

#### Create

```rest
POST http://127.0.0.1:5000/waiter HTTP/1.1
content-type: application/json

{
    "first_name": "John",
    "last_name": "Smith",
    "tax_number": "123456"
}
```

#### List

```rest
GET http://127.0.0.1:5000/waiter HTTP/1.1
```

### Menu Item
#### List
```rest
GET http://127.0.0.1:5000/menu HTTP/1.1
```

#### Create

```rest
POST http://127.0.0.1:5000/menu HTTP/1.1
content-type: application/json

{
    "item_name": "Burger",
    "description": "A tasty burger",
    "price": 6.99
}
```

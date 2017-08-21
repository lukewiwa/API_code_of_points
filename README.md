# MAG 2020 Code of Points REST API

An implementation of a REST API using the Bottle framework and PonyORM as the database abstraction layer. 

**Show User**
----
  Returns json data about a set of skills.

* **URL**

  /  
  /Skills

* **Method:**

  `GET`
  
*  **URL Params**

   **Optional:**
 
   `app=Floor Exercise|Pommel Horse|Rings|Vault|Parallel Bars|Horizontal Bar`  
   `eg=[integer]`  
   `value=[A..I]`

* **Data Params**

  None

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{ success : true, skills : [Skills] }`
 
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Content:** `{ success : false }`

* **Sample Call:**

  ```javascript
    $.ajax({
      url: "/skills?app=Vault&eg=2",
      dataType: "json",
      type : "GET",
      success : function(r) {
        console.log(r);
      }
    });
  ```

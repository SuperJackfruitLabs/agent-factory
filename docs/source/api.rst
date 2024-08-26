API Documentation
=================

This document outlines the API endpoints for the AI Agent Framework.

Base URL
--------

All API requests should be made to: ``http://your-domain.com/api/v1/``

Authentication
--------------

Authentication is required for all API endpoints. Use Bearer token authentication:

.. code-block::

   Authorization: Bearer <your_access_token>

Endpoints
---------

Create Agent
~~~~~~~~~~~~

Create a new AI agent.

- **URL:** ``/agents``
- **Method:** ``POST``
- **Request Body:**

  .. code-block:: json

     {
       "name": "My Assistant",
       "description": "A helpful AI assistant",
       "model": "gpt-3.5-turbo"
     }

- **Success Response:**

  - **Code:** 201 CREATED
  - **Content:**

    .. code-block:: json

       {
         "id": "agent_123456",
         "name": "My Assistant",
         "description": "A helpful AI assistant",
         "model": "gpt-3.5-turbo",
         "created_at": "2024-08-26T12:00:00Z"
       }

Get Agent
~~~~~~~~~

Retrieve details of a specific agent.

- **URL:** ``/agents/{agent_id}``
- **Method:** ``GET``
- **Success Response:**

  - **Code:** 200 OK
  - **Content:**

    .. code-block:: json

       {
         "id": "agent_123456",
         "name": "My Assistant",
         "description": "A helpful AI assistant",
         "model": "gpt-3.5-turbo",
         "created_at": "2024-08-26T12:00:00Z"
       }

Update Agent
~~~~~~~~~~~~

Update an existing agent's details.

- **URL:** ``/agents/{agent_id}``
- **Method:** ``PUT``
- **Request Body:**

  .. code-block:: json

     {
       "name": "Updated Assistant Name",
       "description": "An even more helpful AI assistant"
     }

- **Success Response:**

  - **Code:** 200 OK
  - **Content:**

    .. code-block:: json

       {
         "id": "agent_123456",
         "name": "Updated Assistant Name",
         "description": "An even more helpful AI assistant",
         "model": "gpt-3.5-turbo",
         "created_at": "2024-08-26T12:00:00Z",
         "updated_at": "2024-08-26T14:30:00Z"
       }

Delete Agent
~~~~~~~~~~~~

Delete an existing agent.

- **URL:** ``/agents/{agent_id}``
- **Method:** ``DELETE``
- **Success Response:**

  - **Code:** 204 NO CONTENT

Send Message
~~~~~~~~~~~~

Send a message to an agent and get a response.

- **URL:** ``/agents/{agent_id}/chat``
- **Method:** ``POST``
- **Request Body:**

  .. code-block:: json

     {
       "message": "Hello, can you help me with a task?"
     }

- **Success Response:**

  - **Code:** 200 OK
  - **Content:**

    .. code-block:: json

       {
         "agent_id": "agent_123456",
         "message": "Hello, can you help me with a task?",
         "response": "Of course! I'd be happy to help. What kind of task do you need assistance with?",
         "timestamp": "2024-08-26T15:45:00Z"
       }

Error Responses
---------------

- **400 Bad Request:** Invalid request body or parameters
- **401 Unauthorized:** Authentication failure
- **404 Not Found:** Resource not found
- **500 Internal Server Error:** Server-side error

This API documentation will be continuously updated as the AI Agent Framework evolves.

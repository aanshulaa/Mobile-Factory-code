
# Mobile Factory code challenge

To tackle the Mobile Factory code challenge, I utilized FastAPI, a modern Python web framework, to build the API. FastAPI offers high performance and easy-to-use asynchronous capabilities, making it well-suited for developing efficient web applications. Additionally, I employed tools such as cURL, a command-line tool for making HTTP requests, to test and interact with the API endpoints during development.

The challenge involved creating an endpoint for creating mobile phone orders, which I implemented using FastAPI's intuitive routing system. This allowed me to define the HTTP POST endpoint ("/orders") and handle incoming requests with ease. With FastAPI's built-in validation features, I ensured that the input payload adhered to the expected format, validating the component codes provided by the customer against the predefined set of options.

Furthermore, I leveraged cURL, a versatile command-line tool, to make HTTP requests to the API endpoints for testing purposes. cURL provided a convenient way to simulate client interactions with the API and verify its functionality across different scenarios. By crafting custom requests with cURL, I could thoroughly evaluate the API's behavior and troubleshoot any issues encountered during development.

To run the project, simply follow these steps: Clone the repository to your local machine, install any necessary dependencies (including FastAPI), and start the server. Once the server is up and running, you can use cURL or other HTTP client tools to make POST requests to the designated endpoint ("/orders"). Provide the selected component codes in the request payload, and upon success, you'll receive a response containing the order details.

Overall, by harnessing the power of FastAPI and tools like cURL, I effectively addressed the Mobile Factory code challenge, delivering a robust API solution for creating mobile phone orders. This approach ensured efficient development and thorough testing, resulting in a reliable and scalable application.
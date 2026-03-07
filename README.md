# Getting started with Flask

1. REQUEST: reads what the user sends to the server and processes it
It can be a GET, POST, PUT, DELETE, etc. request.
request.form['username'] - to get the value of the username field from a form submission

2. RESPONSE: after processing the request, the server sends back a response to the user
It can be an HTML page, JSON data, a redirect, etc.
return response("Hello, World!") - to send a simple text response back to the user
Return is easily handled by flask however Response is used to make the things more customiseable and flexible. 
You can return different types of responses based on the needs of your application, such as rendering a template, returning JSON data, or redirecting to another URL.

3. ROUTING: defines how the application responds to a specific URL or endpoint
@app.route('/hello') - to define a route that responds to the /hello URL

4. REDIRECT: sends the user to a different URL 
redirect('/login') - to redirect the user to the /login page
Redirect is a specific type of response that instructs the client's browser to navigate to a different URL. It is used when you want to send the user to another page after performing an action, such as after a successful login or form submission.
In contrast, return is a more general way to send a response back to the client, which can include various types of content, such as HTML, JSON, or plain text. Response is a more flexible way to create custom responses with specific headers, status codes, and content types. Redirect is a specific use case of return that focuses on sending the user to a different URL.   

5. URL_FOR: generates a URL for a given endpoint and arguments
url_for('login') - to generate the URL for the login endpoint

6. SESSION: a way to store information about the user across requests
session['username'] = 'John' - to store the username in the session
Sessions are a way to store information about the user across multiple requests.
They are typically used to keep track of user authentication status, preferences, or other data that needs to persist across different pages of the application.
Sessions are stored on the server side and are associated with a unique session ID that is sent to the client's browser as a cookie. 
When the user makes subsequent requests, the session ID is sent back to the server, allowing the application to retrieve the stored session data and maintain state across different pages.

7. TEMPLATE: a way to generate HTML pages dynamically
render_template('index.html', username='John') - to render the index.html template with the username variable set to 'John'
Templates are a way to generate HTML pages dynamically by combining static HTML with dynamic data.
They allow you to create reusable HTML structures and insert dynamic content based on the data passed to the template.
In Flask, you can use the render_template function to render a template and pass variables to it.
This allows you to create dynamic web pages that can display different content based on user input or other data. 
Templates are typically stored in a separate directory called "templates" within your Flask application.


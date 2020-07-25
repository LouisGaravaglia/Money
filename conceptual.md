### Conceptual Exercise

Answer the following questions below:

- **What are important differences between Python and JavaScript?** // Python has mutable and immutable data types, where Javascript does not have a concept of that. Javascript has only floating point numbers, while Python has several different numberic types. Python has built in hash tables, while Javascript does not. Python has a built in REPL, whereas Javascript needs to be run in a browser, or download node. Python uses class base inheritance, while Javascript uses prototype based inheritance.

- **Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you can try to get a missing key (like "c") *without* your programming crashing.** // dict.get("c", 0) or dict.setdefault("c", 0). The get method will return a value of 0 if there is no "c" key, while setdefault will create a key of "c" and add it's value to be "0" if there is no key of "c" element.

- **What is a unit test?** // A unit test is a method of testing a smaller isolated piece of code, say just one function within a larger set of code. It's the mose speficic way of testing before including more comprehensive methods like intergration testing and system testing.

- **What is an integration test?** // Intergration testing is when you combine separate unit tests to then see if they work together as a whole as well as individually to reproduce what you expect.

- **What is the role of web application framework, like Flask?** // A framework like flask makes the life of a developer much easier by handling a lot of tasks behind the scene in order to connect to a server and launch a web app. 

- **You can pass information to Flask either as a parameter in a route URL(like '/foods/pretzel') or using a URL query param (like 'foods?type=pretzel'). How might you choose which one is a better fit for an application?** // Passing parameters as a query param is better for not sensitive info like searching/sorting within the web app. Whereas using parameters in a route URL would be helpful in the instance of creating dynamic variables based off a username or something that could be different for everyone.

- **How do you collect data from a URL placeholder parameter using Flask?** // By inserting a path variable name between angle brackets in the route, and then anything you type in that route will trigger it and then the text entered by the user for the route will be passed to the view function to be used. You just need to make sure you pass the path variable used in the app.route to the view function.

- **How do you collect data from the query string using Flask?** // You use request.args.get('variable') in order to collect which values they input into the form/search.

- **How do you collect data from the body of the request using Flask?** // You can use the request method by calling request.form or request.args.

- **What is a cookie and what kinds of things are they commonly used for?** // A cookie is a way of storing key value pairs using HTML requst and responses. They interact with the server, but are only stored within HTML. They can be used to store useful information like username and login info so that users don't have to resubmit the same info multiple times when visiting a site.

- **What is the session object in Flask?** // The session object is similar to cookies but lives on the server side. It has a larger storage capacity than cookies, but only lives for the life of the browser tab, so once it closes, all session info is lost.

- **What does Flask's `jsonify()` do?** // It turns any python specific, or non python specific items, into a string that can be read by any program and framework, and be parsed back into it's original content.

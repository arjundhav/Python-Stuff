## CSRF(Cross Site Request Forgery)
   A Cross-Site Request Forgery (CSRF) is an attack that forces an end user to execute unwanted actions on a web application in which they’re currently authenticated. With a little help of social engineering (such as sending a link via email or chat), an attacker may trick the users of a web application into executing actions of the attacker’s choosing. If the victim is a normal user, a successful CSRF attack can force the user to perform state changing requests like transferring funds, changing their email address, and so forth. If the victim is an administrative account, CSRF can compromise the entire web application.   
<a href="https://learn.snyk.io/lessons/csrf-attack/javascript/#:~:text=What%20is%20CSRF%3F,pizza%20to%20an%20attacker%27s%20address!">To get more view about CSRF, click here</a>

### Working:

   <img src="https://secumantra.com/wp-content/uploads/2020/06/csrf-token-1.png">
    When user requests a page from server & when server responds, it has a token in hidden field in the form and it also has a token in response header via a cookie.
 
    Now when form is submitted,token in hidden form field & token in form cookie is also sent along. We know that any cookie set against the domain name is automatically sent, 
    but now the hidden form field is also sent. This is the randomness because attacking site doesn’t know what value token should be in the hidden form field.
    
    When a request with Anti-CSRF token is received by the web application, it first verifies the CSRF token. If it is correct, then only request is processed by the web application.

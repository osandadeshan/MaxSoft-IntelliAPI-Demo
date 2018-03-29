Send A Feedback - Positive Tests Specification
==============================================
Date Created    : 03/04/2018
Version         : 1.0.0
Owner      	    : Osanda Deshan
Description  	: This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.


tags: feedback, send_feedback-positive_tests, positive



* Given that a user needs to invoke "Send A Feedback"
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |Yes                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |



Send a feedback using an invalid email
--------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set               |
     |--------------------------------|----------------------------------------|
     |#comment                        |This is the comment                     |
     |#username                       |Osanda                                  |
     |#rating                         |Awesome                                 |
     |#appId                          |sfc_mvp                                 |
     |#email                          |osanda.com                              |
     |#appName                        |sfc_mvp_ios                             |
* When the user invokes the API
* Then the status code for the request is "201"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                          |Value                                   |
     |-----------------------------------|----------------------------------------|
     |$.status                           |Success                                 |
     |$.code                             |201                                     |
     |$.message.n                        |1                                       |
     |$.message.ok                       |1                                       |



Send a feedback using email as empty
------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set               |
     |--------------------------------|----------------------------------------|
     |#comment                        |This is the comment                     |
     |#username                       |Osanda                                  |
     |#rating                         |Awesome                                 |
     |#appId                          |sfc_mvp                                 |
     |#email                          |                                        |
     |#appName                        |sfc_mvp_ios                             |
* When the user invokes the API
* Then the status code for the request is "201"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                          |Value                                   |
     |-----------------------------------|----------------------------------------|
     |$.status                           |Success                                 |
     |$.code                             |201                                     |
     |$.message.n                        |1                                       |
     |$.message.ok                       |1                                       |



Send a feedback without email attribute
---------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set               |
     |--------------------------------|----------------------------------------|
     |#comment                        |This is the comment                     |
     |#username                       |Osanda                                  |
     |#rating                         |Awesome                                 |
     |#appId                          |sfc_mvp                                 |
     |"email": "#email",              |                                        |
     |#appName                        |sfc_mvp_ios                             |
* When the user invokes the API
* Then the status code for the request is "201"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                          |Value                                   |
     |-----------------------------------|----------------------------------------|
     |$.status                           |Success                                 |
     |$.code                             |201                                     |
     |$.message.n                        |1                                       |
     |$.message.ok                       |1                                       |



Send a feedback using appName as empty
--------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set               |
     |--------------------------------|----------------------------------------|
     |#comment                        |This is the comment                     |
     |#username                       |Osanda                                  |
     |#rating                         |Awesome                                 |
     |#appId                          |sfc_mvp                                 |
     |#email                          |osanda@maxsoftlk.com                    |
     |#appName                        |                                        |
* When the user invokes the API
* Then the status code for the request is "201"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                          |Value                                   |
     |-----------------------------------|----------------------------------------|
     |$.status                           |Success                                 |
     |$.code                             |201                                     |
     |$.message.n                        |1                                       |
     |$.message.ok                       |1                                       |



Send a feedback without appName attribute
-----------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set               |
     |--------------------------------|----------------------------------------|
     |#comment                        |This is the comment                     |
     |#username                       |Osanda                                  |
     |#rating                         |Awesome                                 |
     |#appId                          |sfc_mvp                                 |
     |"#email",                       |"osanda@maxsoftlk.com"                  |
     |"appName": "#appName"           |                                        |
* When the user invokes the API
* Then the status code for the request is "201"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                          |Value                                   |
     |-----------------------------------|----------------------------------------|
     |$.status                           |Success                                 |
     |$.code                             |201                                     |
     |$.message.n                        |1                                       |
     |$.message.ok                       |1                                       |

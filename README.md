# Microservice multi tenant example

Example implementation of a multi-tenant microservice. Microservice can be deployed in an enterprise tenant. The microservice can then be used, for example, to read out the EPL apps of the tenants that have also subscribed to the micro service.

Existing addresses

/environment - returns the environment variables of the microservice

/<tenant_id>/epl_files - returns  the deployed epl files of the tenant <tenant_id>.


To debug the microservice locally, read enivironment variables of the microservice via /environment and add them to the .devcontainer/devcontainer.env file.

______________________


Cumulocity is an IoT platform that enables rapid connections of many, many different devices and applications. It allows you to monitor and respond to IoT data in real time and to spin up this capability in minutes. More information on Cumulocity IoT and how to start a free trial can be found [here](https://www.softwareag.cloud/site/product/cumulocity-iot.html#/).

Cumulocity IoT enables companies to quickly and easily implement smart IoT solutions.

______________________


For more information you can Ask a Question in the [TECHcommunity Forums](http://tech.forums.softwareag.com/techjforum/forums/list.page?product=webmethods-io-b2b).

You can find additional information in the [Software AG TECHcommunity](http://techcommunity.softwareag.com/home/-/product/name/webmethods-io-b2b).


______________________

These tools are provided as-is and without warranty or support. They do not constitute part of the Software AG product suite. Users are free to use, fork and modify them, subject to the license agreement. While Software AG welcomes contributions, we cannot guarantee to include every contribution in the master project.

Contact us at [TECHcommunity](mailto:technologycommunity@softwareag.com?subject=Github/SoftwareAG) if you have any questions.
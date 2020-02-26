Goal
=====

This aims to establish a QA process in team. The team builds a front-end application using REST APIs. In this specific project to build a UI application with this [REST APIs](https://reqres.in/api)

First steps
-----------

- To gather all needed documentations of front-end app and BE app.
- To understand how the communications between FE and BE.
- To find out the environments such as sandbox, staging, etc.
- To make sure the APIs that FE needs to be ready or they can be mocked.
- To make sure unit tests are covered.
- To do ah-hoc testings to understand the BE flows.
- To write the test cases to cover the requirements of features.
- To consider if the automation tests could be implementation at the first place.

Types of tests
--------

- Unit tests are covered: to make sure at the unit function works properly.
- Integration tests are covered: to make sure the integrations between internal or third-parties services work properly.
- End to end tests are covered: to help us validate the flow of data and information.
- Performance tests: to understand how good performance our app is.

Process
-------

- When a new feature is ready to be tested, reading through requirements to perform tests, once they are good, trying to think of out the box to test something outside the requirements. Communicating with other QAs, devs or PMs to consider if the new found issues are good to be logged in backlog or just ignore it in the meantime.
- Implementing the automation tests for that feature if possible.
- Performing a regression tests to make sure it won't cause any regression issue.
- Signing off the feature.

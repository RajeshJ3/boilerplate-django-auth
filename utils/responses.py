from drf_yasg2 import openapi

GET_RESPONSES = {
    200: openapi.Response("OK- Successful GET Request"),
    401: openapi.Response("Unauthorized- Authentication credentials were not provided. || Token Missing or Session Expired"),
    500: openapi.Response("Internal Server Error- Error while processing the GET Request Function.")
}

POST_RESPONSES = {
    200: openapi.Response("OK- Successful POST Request"),
    401: openapi.Response("Unauthorized- Authentication credentials were not provided. || Token Missing or Session Expired"),
    422: openapi.Response("Unprocessable Entity- Make sure that all the required field values are passed"),
    500: openapi.Response("Internal Server Error- Error while processing the POST Request Function.")
}

PUT_RESPONSES = {
    200: openapi.Response("OK- Successful PUT Request"),
    401: openapi.Response("Unauthorized- Authentication credentials were not provided. || Token Missing or Session Expired"),
    422: openapi.Response("Unprocessable Entity- Make sure that all the required field values are passed"),
    500: openapi.Response("Internal Server Error- Error while processing the PUT Request Function.")
}

DELETE_RESPONSES = {
    200: openapi.Response("OK- Successful DELETE Request"),
    500: openapi.Response("Internal Server Error- Error while processing the DELETE Request Function.")
}

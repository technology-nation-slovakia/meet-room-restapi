Technology Nation Bratislava/ Campus 0101/ CS50 Final project
=============================================================
# Meet Room Watch Project
## RESTful API Server

Test Server <https://meet-room-restapi.eu-gb.mybluemix.net/>

#### CHANGE LOG
* ver. 0.1.0 Scaffold RESTful API Server code base
* ver. 0.2.0 Completed /items & /places endpoints
    ```
    /api/items
    /api/items/:id
    /api/items/dates/:start_date
    /api/items/dates/:start_date/:end_date
    /api/items/now
    /api/places
    /api/places/:place_id
    /api/places/:place_id/items
    /api/places/:place_id/items/dates/:start_date
    /api/places/:place_id/items/dates/:start_date/:end_date
    /api/places/:place_id/items/now
    ```
* ver. 0.3.0 Events from linked Google Calendar. Test only endpoint
    ```
    /api/places/:place_id/google-calendar
    ```
* ver. 0.3.1 Google Calendar: Handle calendar's time zone difference between server UTC time and client local time
* ver. 0.4.0 Google Calendar synchronization with DB. Endpoints date changed to datetime. CORS enabled
    ```
    /api/places/:place_id/items/dates/:start_datetime
    /api/places/:place_id/items/dates/:start_datetime/:end_datetime
    ```
* ver. 0.4.1 Fix datetime in JSON response according to ISO-8601. Limit minimal re-sync time interval for GC

# Plant Helpe


This is an app for collecting information about plants from the permapeople database, storing, categorizing, and using ai agents / programs to analyze the data.

The information gathered from permapeople can be used to cross reference with plant sensors and determine plant needs (water, sun, ph, etc.)

The software stack is as follows:

Languages:
    Python
    SQL

Software:
    Flask (potential to move to django in future)
    PostgreSQL
    Docker / Podman for development -> linux
    Ollama -> linux
    Openai-agents
    pytest
    coverage
    SQLAlchemy
    MQTT for transmitting data between sensors and the server

Workflow:
    Server schedules API calls (Perma people, sensors) concurrently -> Sanitizes and stores in DB ->
    Logic compares differences in sensor values and nominal values -> Sends to agent ->
    Agent determines plant needs -> Output AI summary to web page and value differences per plant

Entities:
    User:
    user_id:int name:str password:hash

    Plant:
    plant_id:str type:str scientific_name:str name:str desc:text/string link:str slug:str updated:date created:date
    growth:str water_requirement:str light_requirement:str USDA_hardiness:str soil_type:str family:string

    Plant_Sensor:
    id:str plant_id:foreign type:str name:str light_reading:float water_reading:float soil:str

    AI_Output:
    id:str plant_id:foreign created_at:date severity:string message:text/string

**note: PermaPeople uses strings for light, soil, and water, will need to map values to ambiguous strings
    i.e:
    full_sun = +100%
    partial_sun = +75%
    partial_shade = +50%
    full_shade = +25%

Behaviours:
    
    NO ACCOUNT:
        User navigates to index page -> page prompts for login
        User registers account -> user info added to db

    LOGGED IN:
        User navigates to index page -> dashboard is displayed
        User requests information refresh -> server queries plant DB and sensors
        plant info retrieved -> stored in local DB
        Agent queries info from local DB -> outputs analyses

Tests:

    Database:
        Test tables, columns, indexes exist
        Test insert into database
        Test retrieve from database

        Test invalid insert
        Test invalid query




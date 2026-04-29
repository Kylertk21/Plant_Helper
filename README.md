# Plant Helper

This is an app for collecting information about plants from the permapeople database, storing, categorizing, and using ai agents / programs to analyze the data.

The information gathered from permapeople can be used to cross reference with plant sensors and determine plant needs (water, sun, ph, etc.)

The software stack is as follows:

Languages:
    Python
    SQL

Software:
    Flask (potential to move to django in future)
    PostgreSQL
    Docker / Podman for development
    Ollama
    Openai-agents
    pytest
    MQTT for transmitting data between sensors and the server

Workflow:
    Server schedules API calls (Perma people, sensors) concurrently -> Sanitizes and stores in DB ->
    Logic compares differences in sensor values and nominal values -> Sends to agent ->
    Agent determines plant needs -> Output AI summary to web page and value differences per plant

Entities:
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

Testing:
    For now I am employing a simple testing strategy as this app is mainly for personal use, I may expand tests in the future

    Sync:
        Mock permapeople API responses assert correct rows upsert to Postgres
        Assert no duplicates

    Sensors:
        POST a reading for a known plant, assert it's stored correctly
        POST a reading for a fake plant, assert it fails gracefully

    Comparison:
        Assert comparison between nominal plant + poor plant = sub_nominal reading
        Assert comparison between nominal plant + nominal plant = nominal reading
        Assert if either reading missing = failed comparison 

    Agent:
        Assert agent creates correct response for given reading
    

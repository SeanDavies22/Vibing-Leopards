## Purpose is to create a Class that will contain each row's info from the database.

The following is the general blueprint for how the class will look; however things may change.

I would make this a Struct, but apparently python doesn't need them.  

```
VulnInfo {
cve_id
cost_hour
total_hours
item_name
item_cost 
description
bussiness_info [] <sub> 0 for size, 1 for type </sub>
DbHandler db_handler <sub> I might end gutting the DbHandler class and push funtions into this class </sub>
}
```

# CRC_P1_20-21
Analizing a terrorist events dataset

Description of file:

> record (integer)
Unique five-digit number indicating the RAND-MIPT record number of the event. Use this to join with other sources of data from RAND-MIPT.

> YYYY (integer)
Year of the event.

> deaths (integer)
Number of deaths. All events with deaths=0 have been dropped.

> weapon (integer)
Type of weapon used:
1 = biological or chemical agents
2 = explosives or remote detonated explosives
3 = fire, firebomb or arson
4 = firearms
5 = knives or sharp objects
6 = other or unknown

> OECD (binary)
1 = event occurred within an OECD nation (defined as the member nations  as of the 31 December 2007)
0 = elsewhere

> Iraq/Afghan (binary)
1 = event occurred within either Iraq or Afghanistan
0 = elsewhere

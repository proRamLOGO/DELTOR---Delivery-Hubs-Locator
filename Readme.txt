EFFORTS By :-

1. Shubh Bansal 	 : XIl - A	
2. Harshit Jain	 : XII - A
3. Sumedha Mahajan  : XII - D 
.
Class XII, 2017 - 18 Batch
Rukmini Devi Public School
Pitampura, Delhi, 110034

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

A. ) DESCRIPTION

There is a city with some sub-cities in it. The city is represented as a graph, and the position of each sub-city is identified with it's coordinates(x,y). There are no two sub-cities in the same position. It is not necessary that all sub-cities are linked to each other. The distance between two sub-cities is the distance formula for distance between 2 points in a coordinate axis.

There is an organization which sells products. The company wants to setup its multiple delivery hubs in a city. A sub-city and delivery hub in it it(if assigned to it) will have same coordinates. 

The above task depends upon DISTANCE factor and POPULATION Factor. The Population factor has been handled by the organization itself and they have found the cities in which placing delivery hubs will benefit them maximum. They now just need to deal with the distance factor.    

For setting up delivery hubs, their positions should be chosen so that the average distance from each sub-city to its delivery hub is minimized.

CONSTRAINTS

•	No. of Delivery Hubs <= No. of sub-cities.
•	There should be ATLEAST 2 sub-cities which are linked with only 1 sub-city.

INPUT

Given the positions of the sub-cities, roads and the number of delivery hubs to be set-up, compute the positions/sub/cities where the hubs should be installed so that the average distance from each sub-city to its nearest delivery hub  is minimized for the entire city.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

B. ) ALGORITHM

1.	Start
2.	Input city by taking cities input as their cooordinate axis.
3.	Create Edges between sub-cities by inputting the 2 sub-cities and distance between them.
4.	Input the no. of delivery hubs to be installed.
5.	We have 3 types of sub-cities now:
	-	With one neighbour sub-city : Sink
	-	With 2 neighbour sub-cities : Connector
	-	With more than 2 neoghbour sub-cities : junctions
6.	Iterate over all the sinks 
7.	Apply Depth-First-Search (Searching algorithm in a Graph) on each sink.
8.	End the search where first sink is obtained.
9.	Store the starting sub-city, ending sub-city and all the sub-cities in way in a container.
10.	Store all possible paths in same manner. Call a path a Road.
11.	Count the no. of junctions and length of each road.
12.	Sort the Roads in decreasing order of no. of junctions. If equal no. of junctions then compare the lengths. The lengthier Road will win the comparison.
13.	Traverse through all the Roads now.
14.	If no. of delivery hubs is greater than or equal to the no of junctions in the road then place all the stations in those junctions.
15.	Repeat 12 till no. no. of metro sttions is < then no. of sub cities.
16.	If no. of delivery hubs  not equal to 0 the again traverse through all roads.
17.	Pick up one road now consider it in one dimension. 
18.	Apply the dynamic programming algorithm for finding the sub-cities for remaining no. of cities in the road. Ignore all the junctions where delivery hubs have been already placed.
19.	Output the coordinates of delivery hubs.
20.	End

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
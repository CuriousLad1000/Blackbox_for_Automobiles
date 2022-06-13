You're not shifting a huge amount of data, so I don't think higher data rates than that are going to make much of a difference. 
If that doesn't work, try 38400.

The next optimization would be to only poll the values that don't need to be updated as quickly every 5th, 10th or 20th time the loop is executed. 
No need to update the temperatures several times a second, for example.

Then you will probably want to look into internal timeouts. The ELM327 datasheet talks about them on page 31. Basically if you send '01 05', 
it will wait for a response from the car, and then wait some more, in case more reponses are coming. 
It will only return the response after a certain timeout (200 ms or so).

If you send '01 05 1' instead, it will know that only one response from the car is forthcoming, so it returns it right away. 
I'm guessing the STN chip has a similar feature.





Also, refer to Talking to vehicle (pg32) in ELM327DS DATASHEET
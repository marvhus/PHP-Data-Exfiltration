# PHP Data Exfiltration
Solution for a Ctf challenge JohnHammond showed in a [video](https://youtu.be/XyEmZUpNVcI)  

## Start the php server
First make sure you have php installed.  
Then you can run this:  
```sh
php -S 0.0.0.0:8000
```
or just run the `run.sh` file  

## Run the solver
Make sure you have python 3 installed  
and that you have the `requests` package installed.  

To install the `requests` package  
run this:
```sh
python3 -m pip install request
```

You can now run the solver.  
You can do this by runing the python script,  
like this:
```sh
python3 solve.py
```

## How it works
the challenge takes a get request input, which will be a directory.  
It will then return all the sizes of the files in that directory.  
By using `glob://` we can select files too, so we can iterate over the name.  
And since it tells you the format is `flag[a-fA-F0-9]{15}.txt` (essentialy 15 chars of hex)  
we can just use that to iterate over it.  
And we get an answer in only a second or two if you run in localy.  

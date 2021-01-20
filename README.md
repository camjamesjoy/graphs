# graphs
make and traverse graphs

To run on a windows machine first launch the command line and run clone the repo.

Then run the create_env.cmd script. This will install all needed dependencies.
to run tpye:
create_env.cmd
In the command line.

Next you will need to activate the virtual environment. To do navigate to the graphs directory and run the following command
env\graphs\scripts\activate

Once the virtual environment is activated you should see (graphs) on the left side of the command line if everything is working correctly

Lastly run the following line to make sure that all tests are passing
python -m pytest graphs\tests\

If all tests pass you are now free to implement any graph functions you want!

Note: if you run into any bumps along the way it is possible that your version of python is out of date. This repo
requires python 3.8+

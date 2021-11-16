# Kasetsart University Polls
[![Build Status](https://app.travis-ci.com/chayayot123/ku-polls.svg?branch=iteration2)](https://app.travis-ci.com/chayayot123/ku-polls)
[![codecov](https://codecov.io/gh/chayayot123/ku-polls/branch/iteration3/graph/badge.svg?token=CEvubd2fk6)](https://codecov.io/gh/chayayot123/ku-polls)

This assignment is the project to conducting the polls or surveys within KU community.

* [Wiki Home](../../wiki/Home)
* [Vision Statement](https://github.com/chayayot123/ku-polls/wiki/Vision-Statement)
* [Requirements](https://github.com/chayayot123/ku-polls/wiki/Requirements)
* [Iteration 1 Plan](https://github.com/chayayot123/ku-polls/wiki/Iteration-1-Plan) and [Task Board](https://github.com/chayayot123/ku-polls/projects/2)
* [Iteration 2 Plan](https://github.com/chayayot123/ku-polls/wiki/Iteration-2-Plan) and [Task Board](https://github.com/chayayot123/ku-polls/projects/3)
* [Iteration 3 Plan](https://github.com/chayayot123/ku-polls/wiki/Iteration-3-Plan) and [Task Board](https://github.com/chayayot123/ku-polls/projects/4)

## Running KU Polls

After you clone the ku polls work please use this command to run the work.
```
python manage.py migrate
python manage.py loaddata users polls
```

After you run this command.Use this command to run in your local machine.
```
python manage.py runserver
```


Users provided by the initial data (users.json):

| Username  | Password    |
|-----------|-------------|
| demo01     | Howl4251   |
| demo02     | Howl4421   |

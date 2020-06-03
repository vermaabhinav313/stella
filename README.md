# Stella // @MissStella_bot 
>A modular telegram Python bot running on python3 with an sqlalchemy database.

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/e96f7c790e574fa0ab2f774ceff6b8ef)](https://app.codacy.com/manual/anilchauhanxda/stella?utm_source=github.com&utm_medium=referral&utm_content=anilchauhanxda/allukabot&utm_campaign=Badge_Grade_Dashboard)
[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.png?v=103)](https://github.com/ellerbrock/open-source-badges/)  
[![GPLv3 license](https://img.shields.io/badge/License-GPLv3-blue.svg)](http://perso.crans.org/besson/LICENSE.html)

[![GitHub forks](https://img.shields.io/github/forks/anilchauhanxda/stella.svg?style=social&label=Fork&maxAge=2592000)](https://GitHub.com/anilchauhanxda/stella/network/) [![GitHub stars](https://img.shields.io/github/stars/anilchauhanxda/stella.svg?style=social&label=Star&maxAge=2592000)](https://GitHub.com/anilchauhanxda/stella/stargazers/)

[![stella](https://telegra.ph/file/d5a2e552ba53871952547.jpg)](https://heroku.com/deploy) 

Originally a simple group management bot with multiple admin features, it has evolved, becoming extremely modular and simple to use.
Can be found on telegram as [Stella](https:telegram.dog/MissStella_bot)

### Setting up the stella
Please make sure to use python3.6, as I cannot guarantee everything will work as expected on older python versions! This is because markdown parsing is done by iterating through a dict, which are ordered by default in 3.6.

## Configuration
Remove this line first before doing anything else
`___________PLOX_______REMOVE_____THIS_____LINE__________=True`
# Required
- `API_KEY`: Your bot token.

- `DEV_USERS`: List of id's - (not usernames) for developers who will have the same perms as the owner

- `OWNER_ID`: Bot owner id if you dont know, run the bot and do /id in your private chat with it.

- `OWNER_USERNAME`: Bot owner username. eg.`meanii`

- `SQLALCHEMY_DATABASE_URI`: Needed for any database modules eg. `postgres://meanii:6969@127.0.0.1:5432/meaniidb`

- `MESSAGE_DUMP`: Needed to make sure 'save from' messages persist.

- `GBAN_LOGS`: Needed for /gban users logs.

- `SUDO_USERS`: List of id's -  (not usernames) for users. eg. `[604968079, 802002142]`

- `SUPPORT_USERS`: List of id's (not usernames) for users which are allowed to gban, but can also be banned.

- `WHITELIST_USERS`: List of id's (not usernames) for users which WONT be banned/kicked by the bot.

- `DEL_CMDS`: Whether or not you should delete "blue text must click" commands.


### Python dependencies

Install the necessary python dependencies by moving to the project directory and running:

`pip3 install -r requirements.txt`.

This will install all necessary python packages.

### Database

If you wish to use a database-dependent module (eg: locks, notes, userinfo, users, filters, welcomes),
you'll need to have a database installed on your system. I use postgres, so I recommend using it for optimal compatibility.

In the case of postgres, this is how you would set up a the database on a debian/ubuntu system. Other distributions may vary.

- install postgresql:

`sudo apt-get update && sudo apt-get install postgresql`

- change to the postgres user:

`sudo su - postgres`

- create a new database user (change YOUR_USER appropriately):

`createuser -P -s -e YOUR_USER`

This will be followed by you needing to input your password.

- create a new database table:

`createdb -O YOUR_USER YOUR_DB_NAME`

Change YOUR_USER and YOUR_DB_NAME appropriately.

- finally:

`psql YOUR_DB_NAME -h YOUR_HOST YOUR_USER`

This will allow you to connect to your database via your terminal.
By default, YOUR_HOST should be 0.0.0.0:5432.

You should now be able to build your database URI. This will be:

`sqldbtype://username:pw@hostname:port/db_name`

Replace sqldbtype with whichever db youre using (eg postgres, mysql, sqllite, etc)
repeat for your username, password, hostname (localhost?), port (5432?), and db name.

### Credits:
[@SonOfLars](https://github.com/PaulSonOfLars) (Marie's creator)
[@SaitamaRobot](https://github.com/AnimeKaizoku) (for anime module) 

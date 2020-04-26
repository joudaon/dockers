# RPG BATTLE

No interface video game

https://github.com/onurcokyasar/Python-RPG-BattleScript-

## Using requirements file

```sh
# Getting used pip packages list
$> pip freeze > requirements.txt
# Installing used pip packages list
$> pip install -r requirements.txt
```

## Running with docker

```sh
# Run with docker
$> docker build -t rpg-battle .
$> docker run -it --rm --name rpg-battle rpg-battle

# Run with docker-compose
$> docker-compose run --rm rpg-battle
```
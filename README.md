# arma server tools

Tools to manage running content on arma3server.

Originally developed for Linux dedicated servers. Not all systems will function on windows.

## reference material

### commands

    poetry run arma_server --help
    poetry run steam_pull --help
    poetry run preset_parser --help
    poetry run yaml_setup --help

### Arma server stuff

- <https://community.bistudio.com/wiki/Arma_Dedicated_Server>
- <https://community.bistudio.com/wiki/server.cfg>
- <https://community.bistudio.com/wiki/Arma_3:_Difficulty_Settings>

### Steam / Steamcmd stuff

- <https://developer.valvesoftware.com/wiki/SteamCMD>
- <https://developer.valvesoftware.com/wiki/Arma_3_Dedicated_Server>


### python libraries


- [poetry](https://python-poetry.org)
- [click](https://click.palletsprojects.com/en/7.x/)
- [click_log](https://click-log.readthedocs.io)
- [rich](https://rich.readthedocs.io/en/stable/introduction.html)
- [PyYAML](https://pyyaml.org/wiki/PyYAMLDocumentation)
- [pytest](https://docs.pytest.org/en/stable/)


### articles references

- <https://docs.python.org/3/library/subprocess.html>
- <https://docs.python.org/3/library/shutil.html>
- <https://docs.python.org/3/library/os.html?highlight=os%20symlink#os.symlink>

## yaml files

### yaml config in home dir

~~~
--- # ~/arma_server.yaml
username: steam_username
password: steam_password
workshop: "/home/steam/.steam/steamapps/workshop/content/107410"
arma_home: "/home/steam/.steam/steamcmd/arma3"
server_executable: "arma3server_64"
arma_configs: "/home/steam/arma_configs"
~~~

### yaml config for specific server

- name: name of the server
- config: relative path to the arma cfg file, starting from the arma_configs folder
- port: port the server is on, defaults to 2302 if nothing is set
- mods: list of mods to load

without mods

~~~
--- # example without mods
name: direct_action_altis
config: direct_action/direct_action_altis.cfg
port: 2302
~~~

with mods

~~~
--- # example with some mods 
name: survival_altis
config: survival/survival_altis.cfg
mods: 
  - cba_a3 
  - niarms_all
~~~


## paths and discovery

~~~ windows 7 commandline
C:\Program Files (x86)\Steam\steamapps\common\Arma 3 Server
arma3server.exe*
arma3server_x64.exe*
~~~


~~~ windows 7 bash commandline
/c/Program Files (x86)/Steam/steamapps/common/Arma 3 Server
arma3server.exe*
arma3server_x64.exe*
~~~

~~~ linux steam user
/home/steam/.steam/steamcmd/arma3
arma3server
arma3server_x64
~~~
from fabric.api import task, prefix, run, env, settings, sudo

env.use_ssh_config = True

PROJECT = 'law.co.il'
APACHE_DIRS = ['jolybar_co_il', 'jolybar_com']
HOME_DIR = '/home/tamarinoam/'
WORKON = '. /usr/share/virtualenvwrapper/virtualenvwrapper.sh'


@task
def pull():
    with prefix('{0}; workon {1}'.format(WORKON, PROJECT)):
        run('git pull')


@task
def restart_uwsgi():
    sudo('service uwsgi restart')


@task
def update():
    pull()
    with prefix('{0}; workon {1}'.format(WORKON, PROJECT)):
        run('pip install -r requirements/base.txt')
        run('./manage.py migrate')
        run('./manage.py collectstatic --noinput')
    # restart_uwsgi()

from fabric.api import env, run, sudo, local
from fabric.context_managers import cd
#from fabric.api import env, run, cd, sudo, put, require, settings, hide, puts, local
from fabric.decorators import roles
from fabric.contrib import project, files

STAGING_DIRECTORY = "/var/www/vhosts/twy_production"
PRODUCTION_DIRECTORY = "/var/www/vhosts/twy_production"

# This is for the deployed app, not the vagrant version for dev
env.user = 'powellc'
env.home_dir = STAGING_DIRECTORY
env.project_name = "timberwyckfarm_com"  # Update the vagrant recipe if you change this.
env.git_repo = "ssh://git@bitbucket.org/powellc/timberwyckfarm_com.git"
env.deploy_user = "twy_production"
env.deploy_branch = "develop"
env.project_dir = env.home_dir + '/' + env.project_name

def local():
    env.home_dir = '~/projects/1c/'
    env.deploy_user='powellc'
    env.hosts = ['localhost']
    env.project_dir = env.home_dir + '/' + env.project_name
    env.venv = env.project_name + '/venv'

def production():
    env.hosts = ['lynmayewski.com']
    env.directory = PRODUCTION_DIRECTORY
    env.activate = "source /var/www/vhosts/twy_production/venv/bin/activate"
    env.deploy_user = "twy_production"
    env.name = "Production"
    env.branch = "master"
    env.venv = 'venv'


##### Deployment related commands #####
def ve(command):
    """A utility command to activate the virtualenv and run a user command as the 
    env.deploy_user value."""
    # TODO: add a switch to change into the given directory, too, for staging.
    with cd(env.project_dir):
        sudo(("source %s/%s/bin/activate" % (env.home_dir, env.venv) + " && " + command), user=env.deploy_user)

def hupserver():
    sudo('sudo supervisorctl restart twy',  user=env.user)
    #if env.celery_task:
    #    sudo('sudo supervisorctl restart %s' % env.celery_task, user=env.user)

def update(create_db=False):
    """Update the code after a pull: update requirements, migrate db, and collect static."""
    # Update the project
    with cd(env.project_dir):
        sudo('git pull', user=env.deploy_user)
    ve('pip install -r reqs/production')
    ve('python manage.py validate')  # A gut check before we try and migrate
    # Typically we just want to migrate the database, but for a brand new 
    # project we want to syncdb and fake the migrations
    if create_db:
        ve('python manage.py syncdb --all')
        #ve('python manage.py migrate --fake')
    else:
        ve('python manage.py syncdb')
    #ve('python manage.py collectstatic --noinput')
    #ve('python manage.py rebuild_index --noinput')
    hupserver()

def free():
    """Check free memory."""
    run('free -m')

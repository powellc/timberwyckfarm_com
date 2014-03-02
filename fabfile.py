from fabric.api import env, run, sudo, local, settings
from fabric.context_managers import cd, prefix
#from fabric.api import env, run, cd, sudo, put, require, settings, hide, puts, local
from fabric.decorators import roles
from fabric.contrib import project, files
import re

######## CHANGE BELOW TO SUIT YOUR PROJECT #######

env.prod_user = 'powellc'

env.deploy_user = "twy_production"
env.code_dir = "timberwyckfarm_com"

env.git_repo = "git@github.com:powellc/timberwyckfarm_com.git"
env.host = env.prod_host = "timberwyckfarm.com"
env.stage_host = "staging.timberwyckfarm.com"
env.local_host = "11.0.0.21"
env.dbdump_file = 'timberwyckfarm_com-nightly.sql'
env.home_dir = "/var/www/vhosts/" + env.deploy_user + "/"

######### DO NOT EDIT BELOW THIS LINE ############

def provision():
    # Before we can vagrant up, we just need to grab a prod copy of the DB
    with settings(warn_only=True):
        local('scp %s:/var/backups/databases/latest/%s.bz2 .' % (env.host, env.dbdump_file))
        local('bunzip2 %s.bz2' % env.dbdump_file)

    with settings(warn_only=True):
        local('git clone git@bitbucket.org:timberwyckfarm/houston.git')
        with cd('./houston'):
            local('git pull')

    with settings(warn_only=True):
        # Because our playbook needs to live with our ansible roles
        local('cp ansible/vagrant.yml houston/ansible/')
        local('cp ansible/local_settings.py.j2 houston/ansible/roles/django/templates/')
        local('vagrant up')
        local('vagrant provision')

    # Clean up our DB files
    with settings(warn_only=True):
        local('rm %s.bz2' % env.dbdump_file)
        local('rm %s' % env.dbdump_file)

def get_media():
    with cd(env.home_dir + env.code_dir + '/'):
        sudo("rsync -av --exclude='*.mp4' --exclude='*.flv' --exclude='*.m4v' --exclude='*.mp3'  {0}@{1}:/var/www/vhosts/5q/timberwyckfarm_com/public/media/ public/media".format(env.prod_user, env.prod_host, env.code_dir), user=env.deploy_user)

def start():
    local('node ansible/proxy.js &')
    local('vagrant up')

def v():
    """Use Vagrant for testing"""
    env.user = 'vagrant'
    env.hosts = [env.local_host]   # Update the Vagrantinit file if you change this
    env.code_dir = 'timberwyckfarm_com'

    # retrieve the IdentityFile:
    result = local('vagrant ssh-config | grep IdentityFile', capture=True)
    env.key_filename = re.sub(r'^"|"$', '', result.split()[1])  # parse IdentityFile
    env.venv = 'venv'

def prod():
    """Our Production Server"""
    env.deploy_user = "twy_production"
    env.user = env.prod_user
    env.hosts = [env.prod_host]
    env.home_dir = "/var/www/vhosts/twy_production/"
    env.venv = 'venv'

def stage():
    """Our Production Server"""
    env.deploy_user = "staging_timberwyckfarm"
    env.user = env.prod_user
    env.hosts = [env.stage_host]
    env.home_dir = "/var/www/vhosts/" + env.deploy_user + "/"
    env.venv = 'virtualenv'

def ve(command):
    with cd(env.home_dir + env.code_dir + '/'):
        sudo("source %s%s/bin/activate" % (env.home_dir, env.venv) + " && " + command, user=env.deploy_user)


def deploy(branch=None):
    """Deploy changes to production or staging. Does four things:
     1. pulls new code from branch specified in fabfile config
     2. install reqs
     3. migrate
     4. collectstatic
     5. validate
     6. restart gunicorn/supervisor task
    """
    pull(branch)
    collect()
    #syncdb()
    migrate()
    validate()
    hup()
    
def pull(branch=None):
    with cd(env.home_dir + env.code_dir + '/'):
        sudo("git pull", user=env.deploy_user)
        if branch:
            sudo("git checkout {0}".format(branch), user=env.deploy_user)

def collect():
    """
    Run collect static.
    """
    with cd(env.home_dir + env.code_dir + '/'):
        ve('python manage.py collectstatic --noinput')

def manage(cmd="", extra=""):
    '''
    Run a django management command
    '''
    with cd(env.home_dir + env.code_dir + '/'):
        ve('python manage.py {0} {1}'.format(cmd, extra))

def syncdb():
    """
    Run syncdb.
    """
    ve('python manage.py syncdb --noinput')

def migrate():
    """
    Migrate the db.
    """
    ve('python manage.py migrate --fake')

def validate():
    """
    Run validation, just a gut check
    """
    ve('python manage.py validate')

def reqs(cmd="", extra=""):
    '''
    Re install requirements.txt file
    '''
    with cd(env.home_dir + env.code_dir + '/'):
        ve('pip install -r requirements.txt')

def log():
    """
    View our logs
    """
    with cd(env.home_dir):
        sudo('tail -n 30 logs/supervisord.log')

def hup():
    '''
    HUP gunicorn
    '''
    if env.user == 'vagrant':
        sudo("supervisorctl restart twy_local")
    else:
        sudo("supervisorctl restart twy_production")


def test(apps=''):
    '''
    Test our django app
    '''
    with cd(env.home_dir + env.code_dir + '/'):
        ve('python manage.py test %s' % apps) 

def free():
    """Check free memory."""
    run('free -m')
